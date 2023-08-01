import pandas as pd

# Set display options
pd.set_option('display.max_colwidth', None)  # Show full content of each item in a column
# pd.set_option('display.max_rows', None)  # Show all rows

df = pd.read_parquet('/Users/mkane01/Downloads/contracts0.parquet')
print(df.head(5))  # Display the first few rows of the DataFrame