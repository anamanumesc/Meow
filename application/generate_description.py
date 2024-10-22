import pandas as pd
import math  # Import the math module for the ceil function
import random  # Import random to select verbs

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

attributes_mapping = {
    "calm": {
        1: "very anxious and restless",
        2: "slightly calm",
        3: "somewhat calm",
        4: "very calm",
        5: "always calm and relaxed"
    },
    "fearful": {
        1: "not fearful at all",
        2: "slightly fearful",
        3: "somewhat fearful",
        4: "very fearful",
        5: "extremely fearful"
    },
    "intelligent": {
        1: "not intelligent",
        2: "slightly intelligent",
        3: "moderately intelligent",
        4: "very intelligent",
        5: "extremely intelligent"
    },
    "vigilant": {
        1: "not vigilant",
        2: "slightly vigilant",
        3: "moderately vigilant",
        4: "very vigilant",
        5: "extremely vigilant"
    },
    "persevering": {
        1: "gives up easily",
        2: "slightly persevering",
        3: "moderately persevering",
        4: "very persevering",
        5: "extremely persevering"
    },
    "affectionate": {
        1: "not affectionate",
        2: "slightly affectionate",
        3: "moderately affectionate",
        4: "very affectionate",
        5: "extremely affectionate"
    },
    "friendly": {
        1: "not friendly",
        2: "slightly friendly",
        3: "moderately friendly",
        4: "very friendly",
        5: "extremely friendly"
    },
    "solitary": {
        1: "not solitary",
        2: "slightly solitary",
        3: "moderately solitary",
        4: "very solitary",
        5: "extremely solitary"
    },
    "brutal": {
        1: "completely gentle",
        2: "slightly brutal",
        3: "moderately brutal",
        4: "very brutal",
        5: "extremely brutal"
    },
    "dominant": {
        1: "very submissive",
        2: "slightly dominant",
        3: "moderately dominant",
        4: "very dominant",
        5: "extremely dominant"
    },
    "aggressive": {
        1: "not aggressive at all",
        2: "slightly aggressive",
        3: "moderately aggressive",
        4: "very aggressive",
        5: "extremely aggressive"
    },
    "impulsive": {
        1: "always cautious",
        2: "slightly impulsive",
        3: "moderately impulsive",
        4: "very impulsive",
        5: "extremely impulsive"
    },
    "predictable": {
        1: "completely unpredictable",
        2: "slightly predictable",
        3: "moderately predictable",
        4: "very predictable",
        5: "extremely predictable"
    },
    "distracted": {
        1: "never distracted",
        2: "slightly distracted",
        3: "moderately distracted",
        4: "very distracted",
        5: "extremely distracted"
    },
    "bird": {
        1: "never hunts birds",
        2: "rarely hunts birds",
        3: "sometimes hunts birds",
        4: "often hunts birds",
        5: "very often hunts birds"
    },
    "mammal": {
        1: "never hunts mammals",
        2: "rarely hunts mammals",
        3: "sometimes hunts mammals",
        4: "often hunts mammals",
        5: "very often hunts mammals"
    }
}
# List of sentence starters (verbs) to randomly choose from
sentence_starters = [
    "Your cat is", 
    "Other owners say that your cat is", 
    "It also seems to be", 
    "This cat is often seen as",
    "Many people describe this breed as",
    "You will find that this cat is",
    "The breed is known for being"
]

def get_attribute_description(attribute, level):
    """Fetches the description for a given attribute and level."""
    return attributes_mapping.get(attribute.lower(), {}).get(level, "No description available")

def run():
    print("Choose a breed:")
    for index, (code, name) in enumerate(breed_mapping.items(), start=1):
        print(f"{index}. {name}")
    
    try:
        choice = int(input("Enter the number corresponding to your breed choice: "))
        if choice < 1 or choice > len(breed_mapping):
            print("Invalid choice. Please try again.")
            return
        breed_code = list(breed_mapping.keys())[choice - 1]  
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    breed_name = breed_mapping[breed_code]
    breed_data = df[df['Breed'] == breed_code]
    
    if breed_data.empty:
        print(f"No data available for breed {breed_name}.")
        return
    
    print(f"\nBreed: {breed_name}\n")  # Display breed

    attributes = ['Calm', 'Fearful', 'Intelligent', 'Vigilant', 
                  'Persevering', 'Affectionate', 'Friendly', 
                  'Solitary', 'Brutal', 'Dominant', 
                  'Aggressive', 'Impulsive', 'Predictable', 'Distracted', 
                  'Bird', 'Mammal']

    results = []  # Store the results as pairs of attribute and level
    for attr in attributes:
        # Calculate the mean for the attribute
        most_likely_value = breed_data[attr].mean()
        
        # Round up to the nearest whole number
        level = math.ceil(most_likely_value)

        if most_likely_value == 0:
            level = 0  
        elif level > 5:
            level = 5  

        results.append((attr, level))
    
    print(f"\n{breed_name} Personality Description:\n")
    for attr, level in results:
        # Randomly pick a sentence starter
        verb = random.choice(sentence_starters)
        description = get_attribute_description(attr, level)
        print(f"{verb} {description} ({attr})")


