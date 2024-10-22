import pandas as pd

def run():
    file_path = 'database/cat_personality.xlsx'
    df = pd.read_excel(file_path)

    comparison_columns = [
        'Area', 'Outdoors', 'Observation', 'Shy', 'Calm', 'Fearful', 'Intelligent', 'Vigilant',
        'Persevering', 'Affectionate', 'Friendly', 'Solitary', 'Brutal', 'Dominant',
        'Aggressive', 'Impulsive', 'Predictable', 'Distracted', 'Abundance', 'Bird', 'Mammal'
    ]

    exact_duplicates = df[df.duplicated(keep=False)]

    duplicates_different_breed = df.groupby(comparison_columns).filter(lambda x: x['Breed'].nunique() > 1)

    print("Exact duplicates (all columns are the same):")
    print(exact_duplicates)

    print("\nCases where characteristics are the same but 'Breed' differs:")
    print(duplicates_different_breed)
