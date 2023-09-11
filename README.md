# IDS706_MiniProj2_YangXu

This repository is a continuation of the IDS706 course assignments, focusing on Mini Project 2. Building upon the foundational [ids706-python-template](https://github.com/xuy50/ids706-python-template), it modifies and introduces Pandas-based descriptive statistics.

## Overview

Utilizing the Pandas library, this project demonstrates essential techniques for statistical analysis on datasets. 

## Key Modifications from Original Template

- Transformed `mean.py` to exhibit a sample Pandas descriptive statistics script.
- Adjusted `test_main.py` to reflect changes introduced in `mean.py`.
- Integrated `pandas 2.1.0` within `requirements.txt` to facilitate data manipulation and statistical functions.

### Requirements

Ensure the presence of:
- Python (Version 3.6 or newer)
- Pandas (Version 2.1.0)

`python main.py`

## Functionality

- `load_data()`: Reads the `dataset_sample.csv` file and returns it as a pandas DataFrame.
- `get_descriptive_statistics(data)`: Takes a DataFrame and returns its descriptive statistics.
- `plot_data_distribution(data, column_name)`: Plots and saves a histogram of the given column.

## Sample Output

- Output:
```bash
          Price   Quantity
count  9.000000   9.000000
mean   1.433333  38.111111
std    0.845577  14.084073
min    0.500000  19.000000
25%    0.700000  22.000000
50%    1.200000  42.000000
75%    2.400000  50.000000
max    2.600000  55.000000
```
  
- Descriptive Statistics:


- Data Visualization:
![Price Distribution](Price_distribution.png)


[![example workflow](https://github.com/nogibjj/IDS706_MiniProj2_YangXu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_MiniProj2_YangXu/actions/workflows/cicd.yml)
