import pandas as pd

# Load your Excel file
file_path = 'database/cat_personality.xlsx'
df = pd.read_excel(file_path)

# Drop the 'Row.names' column if present
if 'Row.names' in df.columns:
    df = df.drop(columns=['Row.names'])

# Convert the 'Breed' column to numerical values using Label Encoding
df['Breed_Num'] = df['Breed'].astype('category').cat.codes

# Select numeric columns (excluding 'Breed_Num')
numeric_columns = df.select_dtypes(include=['number']).columns

# Calculate the correlation matrix
correlation_matrix = df[numeric_columns].corr()

# Display the correlation of each numeric attribute with the class (Breed_Num)
correlations_with_breed = correlation_matrix['Breed_Num'].sort_values(ascending=False)

# Print correlations
print("Correlation between attributes and cat breeds (class):\n")
print(correlations_with_breed)
