import pandas as pd

file_path = 'database/cat_personality.xlsx'
df = pd.read_excel(file_path)

# function to check if a column is numeric
def is_numeric(column):
    return pd.api.types.is_numeric_dtype(column)

# display distinct values for each numeric attribute globally, excluding 'Row.names'
print("\nDistinct Values for Numeric Attributes Globally:")
for column in df.columns:
    if column != 'Row.names' and is_numeric(df[column]):
        distinct_values = df[column].value_counts()  # Get distinct values and their frequency
        print(f"\nAttribute: {column}")
        print(distinct_values)