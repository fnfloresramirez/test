import polars as pl

file_path = "data/sample_data.csv"

try:
    df = pl.read_csv(file_path)
    print(df.head())
    print(df.describe())
    print(df.shape)
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
except Exception as e:
    print(f"An error occurred while processing the file: {e}")
