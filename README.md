# Caltech COVID-19 Prediction

## Overview
This repository contains all of the code generated during our efforts to
understand and model the COVID-19 outbreak. Organized by the
[Caltech Data Science Organization](http://datascience.caltech.edu/) and run in Prof.
Yaser Abu-Mostafa's [CS 156b](http://cs156.caltech.edu/) class, the competition seeks to
address the pandemic and help estimate the needs for medical resources, reducing uncertainty
in the crisis response. Specifically, teams predict COVID-19 deaths at the county level in
the U.S. on a two-week timescale. The competition is open to the entire Caltech campus — register [here](https://docs.google.com/forms/d/e/1FAIpQLSeq5ncLFDATIefqU--68OlSQ4pCae-Gww1ZQuf2T-mIZ2f9ng/viewform?usp=sf_link)!

**IMPORTANT: at this time, we can only accommodate Caltech students and researchers in the competition. Over 10% of the student body is competing!**
CS 156b competition page: http://cs156.caltech.edu/covid/

## Purpose

Modeling the spread of disease is a central issue to protect lives around the world. The field of epidemiology seeks to 
quantify predictions, enabling better policies to be formed in response to tragic outbreaks. The projects
held in CS 156b this term directly support this response, introducing novel data science methods to address
a critical problem. Models such as these have informed decisions [about Ebola, Zika, and other major
crises](https://www.npr.org/sections/health-shots/2020/03/04/811146915/how-computer-modeling-of-covid-19s-spread-could-help-fight-the-virus). Indeed, early models introduced by Imperial College London [shaped U.K. policy](https://www.sciencemag.org/news/2020/03/mathematics-life-and-death-how-disease-models-shape-national-shutdowns-and-other). The vital
importance of these models has brought a recent [call to action](https://epcced.github.io/ramp/) from the Royal Society to produce
better prediction models using techniques including data science; this announcement follows only a few months after a similar CDC $3 million mission to [forecast the flu](https://www.wsj.com/articles/scientists-crunch-data-to-predict-how-many-people-will-get-coronavirus-11584479851).
CS 156b seeks to improve such results and make them more robust, more effectively tracking the pandemic to
save lives.

## Data

We provide curated datasets including both US data (mostly at the county level) and international data. Detailed information on each of the datasets is provided both in the README files of `data/international` and `data/us`.

### Getting started with U.S. data

For the most curated dataset of COVID-19 cases, see `covid/nyt_us_counties.csv`. This dataset will be used to score predictions of COVID-19. Additional variables can be merged in from the appropriate subdirectories, and we also provide useful aggregate datasets of relevant variables (demographics, health, etc.) in `aggregate_berkeley.csv` and `aggregate_jhu.csv`.

### Getting started with international data
If you are beginning international data analysis, an excellent place to start is `aggregated_our_world_in_data.csv`, which includes COVID-19 data per country and helpful related variables (demographics, health, etc.) all cleaned and organized with ISO variables.

If you are beginning a case study of a country that faced the pandemic earlier than the U.S., a good place to start is `italy/covid-regions.csv` for region-level COVID-19 data and `italy/aggregate_italy.csv` for related demographic, economic, and health variables.

### Other data

In order to help with this research, Unacast has agreed to provide us with proprietary social distancing data which are not publicly available. Instructions for accessing these data will be posted on the Piazza page. These data should not be distributed outside of Caltech or used for any purpose outside of COVID-19 research.

Teams are also welcome to use any additional publicly accessible datasets they find which they think may be useful. This does come with some conditions:
* Any non-canonical dataset used in the generation of a weekly prediction submission must be publicly disclosed on the Piazza page under the covid_datasets section in the form of a post containing a brief description of the dataset and a link to it.
* Additional datasets will generally not be accessible on the HPC instance provided to CS 156b students. If many teams begin to use the same additional dataset we may consider adding it to the HPC.


## Logistics

Teams of up to four members may compete. Instructions for setting up a private repository from the curated datasets of the CS 156b TAs are available at [Git Repo Initial Setup](https://docs.google.com/document/d/1l2QBnAZp54fhLm-oFgD6_9dBO-1exE8K_-mE_FeQ90A/edit?usp=sharing).

Teams outside of the class will be provided with access info for the Piazza page, which will contain links to useful resources and additional datasets as well as a forum for discussing modeling approaches with other teams.

### Leaderboard

The [leaderboard](http://datascience.caltech.edu/covid/leaderboard.html) is updated daily based on data from the previous two weeks. For prizes, all predictions will be frozen two weeks prior the deadline; the data that accumulates over that two-week period will decide the final scores and prizes.

### Sample Submission

Submissions are made on the [EvalAI competition page](https://evalai.cloudcv.org/web/challenges/challenge-page/582/overview). `sample_submission.csv` shows the expected format of predictions. Predictions should have 10 columns titled ``['id', '10', '20', '30', '40', '50', '60', '70', '80', '90']``. Each entry of the `id` column should be in `yyyy-mm-dd-FIPS` format, where `yyyy` is the year of the prediction (2020 in this case), `mm` is the 2-digit month, `dd` is the 2-digit day, and `FIPS` indicates the entire FIPS code of predicted the county. The other columns should hold a numeric prediction for the corresponding quantile. For example `10` corresponds to the 0.1 quantile, or the bottom 10% of expected outcomes. A prediction should be made for every quantile for every county for every day from April 1st to June 30th inclusive. 

### Evaluation

A pinball loss will be used to evaluate scores, encouraging predicted distributions to be both accurate and confident. An introduction to this metric can be found at [this webpage](https://www.lokad.com/pinball-loss-function-definition#Formula_0), and more formal descriptions are provided in the introduction of [this paper](https://projecteuclid.org/euclid.bj/1297173840) and in [this paper](http://www.lsta.upmc.fr/BIAU/bp.pdf). If the metric proves unreliable in some way during the course of the competition, it may be substituted for a better metric.

## Collaboration and external code

As this research problem relates to an immediate public health concern, we do not wish to restrict teams from using whatever resources possible to construct the best models they can. As such, teams are allowed to collaborate as much as they want, up to and including exchange of code. Students are also allowed to examine and make use of code which has been publicly posted by research groups from other universities who have been working on COVID modeling. The only condition is that if a team uses any code they did not write (outside of standard data science or ML packages), they must post a link to that code publicly on the Piazza forum and also mention it in their progress report. We ask under the honor code that participants do not blindly copy and paste code which they do not understand. 

# License Information

<img src="https://licensebuttons.net/l/by-nd/3.0/88x31.png"> This work is
licensed under [CC-BY-ND](https://creativecommons.org/licenses/by-nd/4.0/). All
software is issued under the standard MIT license which is as follows:

```
Copyright 2020, The authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
