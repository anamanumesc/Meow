import pandas as pd

# Load the dataset
file_path = 'database/cat_personality.xlsx'
df = pd.read_excel(file_path)

# Breed mapping for user-friendly display
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

def run():
    print("Choose a breed:")
    for index, (code, name) in enumerate(breed_mapping.items(), start=1):
        print(f"{index}. {name}")
    
    try:
        choice = int(input("Enter the number corresponding to your breed choice: "))
        if choice < 1 or choice > len(breed_mapping):
            print("Invalid choice. Please try again.")
            return
        breed_code = list(breed_mapping.keys())[choice - 1]  # Get the corresponding breed code
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    breed_name = breed_mapping[breed_code]
    breed_data = df[df['Breed'] == breed_code]
    
    if breed_data.empty:
        print(f"No data available for breed {breed_name}.")
        return
    
    print(f"\nBreed: {breed_name}\n") #display breed

    attributes = ['Outdoors', 'Observation', 'Shy', 'Calm', 'Fearful', 'Intelligent', 'Vigilant', 'Persevering', 
                  'Affectionate', 'Friendly', 'Solitary', 'Brutal', 'Dominant', 'Aggressive', 'Impulsive', 
                  'Predictable', 'Distracted', 'Bird', 'Mammal']
    
    for attr in attributes:
        most_likely_value = breed_data[attr].mean()  #  mode = most frequent mode()[0]
                                                        # mean = media  mean() 
        print(f"{attr}: {most_likely_value}")

