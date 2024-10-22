import pandas as pd

#how many instances for each breed?

file_path = 'database/cat_personality.xlsx'
df = pd.read_excel(file_path)
# group by breed and count
breed_counts = df.groupby('Breed').size().reset_index(name='Attribute Count')
# sort the result from small to high
breed_counts_sorted = breed_counts.sort_values(by='Attribute Count', ascending=True)
# print the result
print(breed_counts_sorted)

