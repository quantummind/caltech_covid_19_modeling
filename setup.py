import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covid19",
    version="0.0.1",
    author="COVID-19 PBoP consortium",
    author_email="mrazomej {at} caltech {dot} edu",
    description="This repository contains all active research materials for the COVID-19 outbreak modeling project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/COVIDmodeling/covid_19_modeling",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
