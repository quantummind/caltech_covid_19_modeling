# Adapted from
# https://gist.github.com/Amarang/3341c9a24da4556def7c3a03a12949b8
# ^ His stuff is broken though so you should refer to my script
import numpy as np
import pandas as pd
import glob
import os
import sys
from collections import defaultdict
# pip3 install --user PyMuPDF
import fitz
import git
import shutil
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
csvdir = f"{homedir}/data/google_mobility/"
datadir = f"{homedir}/data/google_mobility/pdfs"
destination = csvdir + "/extrapolated_mobility_report_US.csv"

# Interpolate a graph on a PDF page
def parse_stream(stream):
    data_raw = []
    data_transformed = []
    rotparams = None
    npatches = 0
    for line in stream.splitlines():
        if line.endswith(" cm"):
            # page 146 of https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/pdf_reference_archives/PDFReference.pdf
            rotparams = list(map(float, line.split()[:-1]))
        elif line.endswith(" l"):
            x, y = list(map(float, line.split()[:2]))
            a, b, c, d, e, f = rotparams
            xp = a*x+c*y+e
            yp = b*x+d*y+f
            data_transformed.append([xp, yp])
            data_raw.append([x, y])
        elif line.endswith(" m"):
            npatches += 1
        else:
            pass
    
    # Make sure our scraped graph has good enough data before returning
    if len(data_raw) == 0:
        return dict(good=False)
    data_raw = np.array(data_raw)
    basex, basey = data_raw[-1]
    good = False
    if basex == 0.:
        data_raw[:, 1] = basey - data_raw[:, 1]
        data_raw[:, 1] *= 100/60.
        data_raw = data_raw[data_raw[:, 1] != 0.]
        if npatches == 1:
            good = True
    return dict(data=np.array(data_raw), npatches=npatches, good=good)

# Parse a given page's graphs for all categories
def parse_page(doc, ipage, verbose=False):
    categories = [
        "Retail & recreation",
        "Grocery & pharmacy",
        "Parks",
        "Transit stations",
        "Workplace",
        "Residential",
    ]

    counties = []
    curr_county = None
    curr_category = None
    data = defaultdict(lambda: defaultdict(list))
    pagetext = doc.getPageText(ipage)
    lines = pagetext.splitlines()
    tickdates = list(filter(lambda x: len(x.split()) == 3, set(lines[-10:])))
    for line in lines:
        # don't need these lines at all
        if ("* Not enough data") in line:
            continue
        if ("needs a significant volume of data") in line:
            continue

        # if we encountered a category, add to dict, otherwise
        # push all seen lines into the existing dict entry
        if any(line.startswith(c) for c in categories):
            curr_category = line
        elif curr_category:
            data[curr_county][curr_category].append(line)

        # If it doesn't match anything, then it's a county name
        if (all(c not in line for c in categories)
                and ("compared to baseline" not in line)
                and ("Not enough data" not in line)
            ):
            # saw both counties already
            if len(data.keys()) == 2:
                break
            counties.append(line)
            curr_county = line

    newdata = {}
    for county in data:
        newdata[county] = {}
        for category in data[county]:
            # if the category text ends with a space, then there was a star/asterisk there
            # indicating lack of data. we skip these.
            if category.endswith(" "):
                continue
            temp = [x for x in data[county][category]
                    if "compared to baseline" in x]
            if not temp:
                continue
            percent = int(temp[0].split()[0].replace("%", ""))
            newdata[county][category.strip()] = percent
    data = newdata

    tomatch = []
    for county in counties:
        for category in categories:
            if category in data[county]:
                tomatch.append([county, category, data[county][category]])
    if verbose:
        print(len(tomatch))
        print(data)

    goodplots = []
    xrefs = sorted(doc.getPageXObjectList(ipage),
                   key=lambda x: int(x[1].replace("X", "")))
    for i, xref in enumerate(xrefs):
        stream = doc.xrefStream(xref[0]).decode()
        info = parse_stream(stream)
        if not info["good"]:
            continue
        goodplots.append(info)
    if verbose:
        print(len(goodplots))

    ret = []

    if len(tomatch) != len(goodplots):
        return ret

    for m, g in zip(tomatch, goodplots):
        xs = g["data"][:, 0]
        ys = g["data"][:, 1]
        maxys = ys[np.where(xs == xs.max())[0]]
        maxy = maxys[np.argmax(np.abs(maxys))]

        # parsed the tick date labels as text. find the min/max (first/last)
        # and make evenly spaced dates, one per day, to assign to x values between
        # 0 and 200 (the width of the plots).
        ts = list(map(lambda x: pd.Timestamp(
            x.split(None, 1)[-1] + ", 2020"), tickdates))
        low, high = min(ts), max(ts)
        dr = list(map(lambda x: str(x).split()[
                  0], pd.date_range(low, high, freq="D")))
        lutpairs = list(zip(np.linspace(0, 200, len(dr)), dr))

        dates = []
        values = []
        asort = xs.argsort()
        xs = xs[asort]
        ys = ys[asort]
        for x, y in zip(xs, ys):
            date = min(lutpairs, key=lambda v: abs(v[0]-x))[1]
            dates.append(date)
            values.append(round(y, 3))

        ret.append(dict(
            county=m[0], category=m[1], change=m[2],
            values=values,
            dates=dates,
            changecalc=maxy,
        ))
    return ret


def parse_state(filename, existing_df=False, old_df=None, verbose=False):

    # Extract the state name and replace _ with a space 
    name_start_ind = filename.index("_US_") + len("_US_")
    name_end_ind = filename.index("_Mobility_")
    state = filename[name_start_ind: name_end_ind]
    state = state.replace("_", " ")

    # Parse each individual PDF page of the state document
    doc = fitz.Document(filename)
    data = []
    for i in range(2, doc.pageCount-1):
        for entry in parse_page(doc, i):
            entry["state"] = state
            entry["page"] = i
            data.append(entry)
    df = pd.DataFrame(data)

    # Handle regions that don't have counties
    if (len(df)) == 0:
        return old_df
    ncounties = 0
    if 'county' in df.columns:
        ncounties = df['county'].nunique()
    else:
        df['county'] = ""

    if verbose:
        print(f"Parsed {len(df)} plots for {ncounties} counties in {state}")
    df = df[["state", "county", "category", "change",
             "changecalc", "dates", "values", "page"]]
    if existing_df:
        df = pd.concat([old_df, df])

    return df

# Populate a given row entry with the value corresponding to the date
def split_date(row, date):
    row_dates = row["dates"]
    if date not in row_dates:
        return ""
    date_index = row_dates.index(date)

    date_values = row["values"]
    if date_index >= len(date_values):
        return ""

    return date_values[date_index]

def extrapolate_all_states():
    state_pdf_names = [f for f in glob.glob(datadir + "/*_US_*_Mobility_Report_en.pdf")]
    
    # Build the initial dataframe for all states
    print("Extrapolating data from Google Mobility PDF Graphs, Takes around a minute")
    df = parse_state(state_pdf_names[0])
    for i in range(1, len(state_pdf_names)):
        df = parse_state(state_pdf_names[i], True, df)

    # Create a column for each date value and populate with corresponding values
    all_dates = df["dates"].all()
    for date in all_dates:
        df[date] = df.apply(lambda row: split_date(row, date), axis=1)

    # Drop old columns
    df = df.drop(columns=["dates", "values", "page"])

    df.to_csv(destination, index=False)
    print("Finished Google Mobility PDF Graph Extrapolation")


if __name__ == '__main__':
    extrapolate_all_states()
