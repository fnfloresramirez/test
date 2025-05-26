# Python EDA Project: Time Series Analysis

## Overview

This project demonstrates a basic Exploratory Data Analysis (EDA) workflow in Python. It involves:
1.  Generating a synthetic time series dataset with columns for Date, Temperature, pH, and Chemical Oxygen Demand (COD).
2.  Saving this dataset to a CSV file (`time_series_dataset.csv`).
3.  Loading the data from the CSV.
4.  Performing a series of EDA tasks to understand the data's characteristics, distributions, and relationships.

The primary script for this project is `test_1812024.py`.

## Features

*   **Data Generation:** Creates a sample time series dataset.
*   **Data Inspection:** Basic checks like `head()`, `tail()`, `info()`, `describe()`.
*   **Missing Value Handling:** Includes a check for missing values and a placeholder for imputation strategies.
*   **Univariate Analysis:**
    *   Histograms for 'Temperature', 'pH', and 'cod'.
    *   Box plots for 'Temperature', 'pH', and 'cod'.
*   **Bivariate Analysis:**
    *   Scatter plots for pairs of numerical variables.
    *   Correlation matrix and heatmap.
*   **Time Series Visualization:** Plots 'Temperature', 'pH', and 'cod' over time.

## Requirements

*   Python 3.x
*   pandas
*   numpy
*   matplotlib
*   seaborn

You can install these dependencies using pip:
```
pip install pandas numpy matplotlib seaborn
```

## How to Run

1.  Ensure you have Python and the required libraries installed (see Requirements).
2.  Clone this repository or download the `test_1812024.py` script.
3.  Navigate to the directory containing the script.
4.  Run the script from your terminal:
    ```
    python test_1812024.py
    ```
5.  The script will:
    *   Generate `time_series_dataset.csv`.
    *   Print various data summaries and the correlation matrix to the console.
    *   Display a series of plots (histograms, box plots, scatter plots, heatmap, and time series plots). Each plot or set of plots will appear in a separate window; close each window to proceed to the next.

## EDA Steps Performed

The script `test_1812024.py` executes the following EDA steps:

1.  **Data Generation & Saving:** Creates and saves the synthetic dataset.
2.  **Data Loading & Initial Inspection:** Loads the data and prints `head`, `tail`, `info`, and `describe` outputs.
3.  **Missing Value Check:** Reports if any missing values are found.
4.  **Univariate EDA:** Generates histograms and box plots for each key numerical feature to understand their individual distributions and identify outliers.
5.  **Bivariate EDA:** Creates scatter plots to visualize relationships between pairs of features and computes/displays a correlation matrix (with a heatmap) to quantify these relationships.
6.  **Time Series Plotting:** Visualizes each key numerical feature over time to observe trends or patterns.
```
