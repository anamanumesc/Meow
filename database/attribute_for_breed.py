import pandas as pd

file_path = 'database/cat_personality.xlsx'
df = pd.read_excel(file_path)

# function to check if a column is numeric
def is_numeric(column):
    return pd.api.types.is_numeric_dtype(column)

# display distinct values for each numeric attribute per breed, excluding 'Row.names'
print("\nDistinct Values for Numeric Attributes Per Breed:")
breeds = df['Breed'].unique()  #get the list of unique breeds
for breed in breeds:
    print(f"\nBreed: {breed}")
    breed_data = df[df['Breed'] == breed]
    
    for column in df.columns:
        if column != 'Breed' and column != 'Row.names' and is_numeric(df[column]):  # Exclude 'Row.names' and 'Breed'
            distinct_values_per_breed = breed_data[column].value_counts()  # Get distinct values and their frequency for this breed
            print(f"\nAttribute: {column}")
            print(distinct_values_per_breed)