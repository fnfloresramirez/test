# This script demonstrates the generation of a synthetic time series dataset (Temperature, pH, COD)
# and performs various Exploratory Data Analysis (EDA) tasks.
# These tasks include data inspection, missing value checks,
# univariate analysis (histograms, box plots), bivariate analysis (scatter plots, correlation heatmap),
# and plotting the initial time series data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # For heatmap visualization

def generate_and_save_data(filename='time_series_dataset.csv'):
    """
    Generates a time series dataset with Date, Temperature, pH, and COD.
    Saves the dataset to a CSV file.

    Args:
        filename (str): The name of the CSV file to save the data to.

    Returns:
        pd.DataFrame: The generated time series data.
    """
    # Generate date range from January 2013 to December 2020 with monthly frequency
    date_range = pd.date_range(start='2013-01-01', end='2020-12-31', freq='M')

    # Generate random temperatures between -5 and +35 degrees Celsius
    temperatures = np.random.uniform(low=-5, high=35, size=len(date_range))

    # Generate random pH values between 4 and 7
    ph_values = np.random.uniform(low=4, high=7, size=len(date_range))
    cod = np.random.uniform(low=0, high=4, size=len(date_range))

    # Create a DataFrame
    time_series_data = pd.DataFrame({
        'Date': date_range,
        'Temperature': temperatures,
        'pH': ph_values,
        'cod': cod,
    })

    # Save the dataset to a CSV file
    time_series_data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
    return time_series_data

def plot_initial_data(dataframe):
    """
    Plots Temperature, pH, and COD time series data from the given DataFrame.
    Each variable is plotted on a separate subplot in a 3x1 layout.

    Args:
        dataframe (pd.DataFrame): DataFrame containing 'Date', 'Temperature', 'pH', and 'cod' columns.
                                  'Date' column should be datetime objects.
    
    Side Effects:
        Displays a matplotlib plot with three subplots.
    """
    plt.figure(figsize=(14, 10)) # Adjusted figure size for 3 plots

    # Plot Temperature
    plt.subplot(3, 1, 1)
    plt.plot(dataframe['Date'], dataframe['Temperature'], label='Temperature', color='r')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature vs Time')
    plt.legend()
    plt.grid(True) # Added grid

    # Plot pH
    plt.subplot(3, 1, 2)
    plt.plot(dataframe['Date'], dataframe['pH'], label='pH', color='b')
    plt.xlabel('Date')
    plt.ylabel('pH')
    plt.title('pH vs Time')
    plt.legend()
    plt.grid(True) # Added grid

    # Plot cod
    plt.subplot(3, 1, 3)
    plt.plot(dataframe['Date'], dataframe['cod'], label='COD', color='g')
    plt.xlabel('Date')
    plt.ylabel('COD')
    plt.title('COD vs Time')
    plt.legend()
    plt.grid(True) # Added grid

    # Adjust layout and show plot
    plt.tight_layout()
    plt.show() # Added plt.show()

def perform_univariate_eda(dataframe):
    """
    Performs univariate EDA by plotting histograms and box plots for Temperature, pH, and COD.

    Args:
        dataframe (pd.DataFrame): DataFrame containing 'Temperature', 'pH', and 'cod' columns.

    Side Effects:
        Displays histograms and box plots for each specified column.
    """
    numerical_cols = ['Temperature', 'pH', 'cod']
    for col in numerical_cols:
        # Plot Histogram
        plt.figure(figsize=(8, 6))
        plt.hist(dataframe[col], bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

        # Plot Box Plot
        plt.figure(figsize=(8, 6))
        plt.boxplot(dataframe[col], vert=False, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
        plt.title(f'Box Plot of {col}')
        plt.xlabel(col) # For horizontal boxplot, this is the value axis
        plt.yticks([]) # Hide Y-axis ticks for horizontal boxplot if only one variable
        plt.tight_layout()
        plt.show()

def perform_bivariate_eda(dataframe):
    """
    Performs bivariate EDA: generates scatter plots for pairs of variables,
    prints a correlation matrix, and attempts to display a heatmap of the matrix.

    Args:
        dataframe (pd.DataFrame): DataFrame containing 'Temperature', 'pH', and 'cod' columns.

    Side Effects:
        Displays scatter plots and potentially a heatmap. Prints the correlation matrix.
    """
    numerical_cols = ['Temperature', 'pH', 'cod']
    pairs = [('Temperature', 'pH'), ('Temperature', 'cod'), ('pH', 'cod')]

    # Scatter Plots
    for col1, col2 in pairs:
        plt.figure(figsize=(8, 6))
        plt.scatter(dataframe[col1], dataframe[col2], alpha=0.5)
        plt.title(f'{col1} vs. {col2}')
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # Correlation Matrix
    print("\nCorrelation Matrix:")
    correlation_matrix = dataframe[numerical_cols].corr()
    print(correlation_matrix)

    # Heatmap (Optional - attempting with seaborn)
    try:
        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"\nCould not generate heatmap, possibly due to missing seaborn or other error: {e}")
        print("Seaborn is an optional dependency for heatmap visualization.")

if __name__ == '__main__':
    # --- Data Generation ---
    # Generate synthetic data and save it to a CSV file.
    # The returned DataFrame is assigned to '_' as its direct use is not immediately needed
    # because the script proceeds to load data from the CSV for subsequent steps.
    print("--- Data Generation ---")
    _ = generate_and_save_data('time_series_dataset.csv')
    print("--- End of Data Generation ---\n")

    # --- Data Loading ---
    print("--- Data Loading ---")
    # Load the data from the CSV file.
    # 'parse_dates=['Date']' ensures the 'Date' column is read as datetime objects.
    loaded_data = pd.read_csv('time_series_dataset.csv', parse_dates=['Date'])
    print("Data loaded successfully from time_series_dataset.csv")
    print("--- End of Data Loading ---\n")

    # Display the first few rows of the loaded dataset (original optional verification)
    # print("Loaded data from CSV head:") # This was the original head print (now part of Data Inspection)
    # print(loaded_data.head()) # This was the original head print (now part of Data Inspection)

    # --- Data Inspection ---
    # Basic inspection of the loaded DataFrame.
    print("--- Data Inspection ---")

    print("\nFirst 5 rows (loaded_data.head()):")
    print(loaded_data.head())

    print("\nLast 5 rows (loaded_data.tail()):")
    print(loaded_data.tail())

    print("\nDataFrame Info (loaded_data.info()):")
    # .info() prints summary directly to stdout, including dtype and non-null counts.
    loaded_data.info()

    print("\nDescriptive Statistics (loaded_data.describe()):")
    print(loaded_data.describe())

    print("--- End of Data Inspection ---\n")

    # --- Missing Value Check ---
    # Checking for any missing values in the dataset.
    print("--- Missing Value Check ---")
    print("\nMissing Values per Column:")
    print(loaded_data.isnull().sum())

    # Placeholder for Imputation Strategy.
    # If missing values were present and significant, appropriate imputation
    # (e.g., mean, median, mode imputation, or more advanced techniques)
    # would be considered here based on the nature of the data and missingness.
    # Example:
    # for column in ['Temperature', 'pH', 'cod']:
    #     if loaded_data[column].isnull().any():
    #         loaded_data[column].fillna(loaded_data[column].median(), inplace=True) # Using median as an example
    print("--- End of Missing Value Check ---\n")

    # --- Univariate EDA ---
    # Performing univariate analysis on key numerical columns.
    print("--- Univariate EDA ---")
    perform_univariate_eda(loaded_data)
    print("--- End of Univariate EDA ---\n")

    # --- Bivariate EDA ---
    # Performing bivariate analysis to understand relationships between variables.
    print("--- Bivariate EDA ---")
    perform_bivariate_eda(loaded_data)
    print("--- End of Bivariate EDA ---\n")

    # --- Initial Time Series Plotting ---
    # Plotting the original time series data for Temperature, pH, and COD.
    print("--- Initial Time Series Plotting ---")
    plot_initial_data(loaded_data)
    print("--- End of Initial Time Series Plotting ---")
    
    # Note: plt.show() is called within each plotting function 
    # (plot_initial_data, perform_univariate_eda, perform_bivariate_eda)
    # to display plots immediately after they are generated for that specific EDA step.
