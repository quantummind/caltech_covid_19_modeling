# Caltech COVID-19 Prediction Challenge

## Overview
This repository contains all of the code generated during our efforts to
understand and model the COVID-19 outbreak.

### Sample Submission

sample_submission.csv shows the expected format of predictions. Predictions should have 10 columns titled ['id', '10', '20', '30', '40', '50', '60', '70', '80', '90']. Each entry of the 'id' column should be in yyyy-mm-dd-FIPS format, where yyyy is the year of the prediction (2020 in this case), mm is the 2-digit month, dd is the 2-digit day, and FIPS indicates the entire FIPS code of predicted the county. The other columns should hold a numeric prediction for the corresponding quantile. For example '10' corresponds to the 0.1 quantile, or the bottom 10% of expected outcomes. A prediction should be made for every quantile for every county for every day from April 1st to June 30th inclusive. 

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
