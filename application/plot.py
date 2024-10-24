import os
import pandas as pd
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

file_path = r'/home/sphinx/AI/project/Meow/database/cat_numericals.xlsx'
data = pd.read_excel(file_path)

missing_values_count = data.isnull().sum().sum()
print(f"Missing values count: {missing_values_count}")

duplicates_found = data.duplicated().sum()
print(f"Duplicates: {duplicates_found}")

if 'Breed' in data.columns:
    breed_counts = data['Breed'].value_counts()
    print("\nBreed counts:")
    for breed, count in breed_counts.items():
        print(f"{breed}: {count}")

data = data.drop(['Row.names', 'Timestamp', 'More', 'Breed'], axis=1, errors='ignore')

for column in data.columns:
    data[column] = pd.to_numeric(data[column], errors='coerce')

data = data.fillna(data.mean())

duplicates_found_after = data.duplicated().sum()
if duplicates_found_after > 0:
    data = data.drop_duplicates()

X = data.copy()
y = pd.Series([1] * len(X))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

dtc = DecisionTreeClassifier(random_state=42)
dtc.fit(X_train, y_train)

y_pred = dtc.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy}")

plots_dir = '/home/sphinx/AI/project/Meow/plots/'
os.makedirs(plots_dir, exist_ok=True)

for column in X.columns:
    plot.figure(figsize=(8, 6))
    value_counts = data[column].value_counts().sort_index()

    if not value_counts.empty:
        value_counts.plot(kind='bar')
        plot.title(f'Distribution of {column}')
        plot.xlabel(column)
        plot.ylabel('Count')
        plot.xticks(rotation=0)
        plot.tight_layout()
        plot.savefig(f'{plots_dir}{column}_distribution.png')
        print(f'Bar plot {column} saved')

    plot.close()
