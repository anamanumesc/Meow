import pandas as pd

file_path = 'database/cat_personality.xlsx'
df = pd.read_excel(file_path)

df['Hair'] = 1

df.loc[df['Breed'] == 'SPH', 'Hair'] = 0

df.to_excel(file_path, index=False)

print("New 'Hair' attribute added successfully!")
