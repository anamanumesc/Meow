import pandas as pd

file_path = 'database/form_information.xlsx'
data = pd.read_excel(file_path)

# i remove all the diacritics and capslocks
data['Sex'] = data['Sex'].str.strip()
data['Age'] = data['Age'].str.strip()
data['Breed'] = data['Breed'].str.strip()
data['Number'] = data['Number'].astype(str).str.strip()
data['Housing'] = data['Housing'].str.strip()
data['Area'] = data['Area'].str.strip()
data['Outdoors'] = data['Outdoors'].str.strip()
data['Observation'] = data['Observation'].str.strip()
data['Abundance'] = data['Abundance'].str.strip()
data['Bird'] = data['Bird'].str.strip()
data['Mammal'] = data['Mammal'].str.strip()

# copy the data
data_transformed = data.copy()

# map
data_transformed['Sex'] = data_transformed['Sex'].map({'Male': 0, 'Female': 1}).fillna(data_transformed['Sex'])

# map
age_mapping = {
    'Less than 1 year': 0,
    '1 to 2 years': 1,
    '2 to 10 years': 5,
    '10 + years': 7
}
data_transformed['Age'] = data_transformed['Age'].map(age_mapping).fillna(data_transformed['Age'])

# map
breed_mapping = {
    "BEN": "Bengal",
    "SBI": "Birman",
    "BRI": "British Shorthair",
    "CHA": "Chartreux",
    "EUR": "European",
    "MCO": "Maine Coon",
    "PER": "Persian",
    "RAG": "Ragdoll",
    "SPH": "Sphynx",
    "ORI": "Oriental",
    "TUV": "Turkish Angora"
}
data_transformed['Breed'] = data_transformed['Breed'].map(breed_mapping).fillna(data_transformed['Breed'])

# map
number_mapping = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '5+': 6
}
data_transformed['Number'] = data_transformed['Number'].map(number_mapping).fillna(data_transformed['Number'])

# map
housing_mapping = {
    'Apartment without balcony': 0, 
    'Apartment with balcony or terrace': 1,
    'House in a subdivision': 5, 
    'Individual house': 6
}
data_transformed['Housing'] = data_transformed['Housing'].map(housing_mapping).fillna(data_transformed['Housing'])

#map
area_mapping = {
    'Urban': 0, 
    'Periurban': 1, 
    'Rural': 2
}
data_transformed['Area'] = data_transformed['Area'].map(area_mapping).fillna(data_transformed['Area'])

# map
outdoors_mapping = {
    'None/Limited': 0, 
    'Moderate (1 to 5 hours)': 1, 
    'Long (more than 5 hours)': 2,
    'All the time (come back just to eat)': 3
}
data_transformed['Outdoors'] = data_transformed['Outdoors'].map(outdoors_mapping).fillna(data_transformed['Outdoors'])

# map
observation_mapping = {
    'None': 0, 
    'Limited (less than one hour)': 1, 
    'Moderate (1 to 5 hours)': 2,
    'Long (more than 5 hours)': 3
}
data_transformed['Observation'] = data_transformed['Observation'].map(observation_mapping).fillna(data_transformed['Observation'])

# map
abundance_mapping = {
    'Low': 1, 
    'Moderate': 2, 
    'High': 3, 
    "I don't know": 0
}
data_transformed['Abundance'] = data_transformed['Abundance'].map(abundance_mapping).fillna(data_transformed['Abundance'])

# map
bird_predation_mapping = {
    'Never': 0, 
    'Rarely (1 to 5 times a year)': 1, 
    'Sometimes (5 to 10 times a year)': 2,
    'Often (1 to 3 times a month)': 3, 
    'Very often (once a week or more)': 4
}
data_transformed['Bird'] = data_transformed['Bird'].map(bird_predation_mapping).fillna(data_transformed['Bird'])

# map
mammal_predation_mapping = {
    'Never': 0, 
    'Rarely (1 to 5 times a year)': 1, 
    'Sometimes (5 to 10 times a year)': 2,
    'Often (1 to 3 times a month)': 3, 
    'Very often (once a week or more)': 4
}
data_transformed['Mammal'] = data_transformed['Mammal'].map(mammal_predation_mapping).fillna(data_transformed['Mammal'])

# save the info
output_file_path = 'database/form_information.xlsx'
data_transformed.to_excel(output_file_path, index=False)

print(f"data successfully transformed and saved to {output_file_path}")
