from application import (
    add_cat_instance, identify_cat_breed, generate_description, 
    compare_breeds, detect_errors, transform_attributes, find_correlations, propose_new_data
)
from database import attribute_distribution

def menu():
    print("\n--- Catology System ---")
    print("1. Add a new cat instance")
    #Propuneți soluții privind completarea setului de date cu instanțe și atribute noi.
    print("2. Identify a cat breed")
    print("3. Generate a breed description")
    print("4. Compare two breeds")
    print("5. Detect errors in dataset")
    #Implementați un program capabil să citească setul de date și să semnaleze eventuale erori (valori lipsă sau suplimentare, instanțe identice).
    print("6. Analyze attribute distribution")  # basicaly afiseaza multe date din exel 
    # afiseaza numărul de instanțe pentru fiecare clasă (rasă de pisici) 
    # extragă lista de valori distincte pentru fiecare atribut și să afișeze numărul total de valori și frecvența pentru fiecare valoare, la nivelul întregului fișier și la nivelul fiecărei clase.
    # + generates histograms and boxplots to visually represent these distributions.
    print("7. Transform non-numeric attributes")
    print("8. Find correlations between attributes")
    print("9. Propose new instances or attributes")
   # Identificați corelații între atribute și clase
    print("10. Exit")
    print("------------------------")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_cat_instance.run()
        elif choice == '2':
            identify_cat_breed.run()
        elif choice == '3':
            generate_description.run()
        elif choice == '4':
            compare_breeds.run()
        elif choice == '5':
            detect_errors.run()
        elif choice == '6':
            attribute_distribution.run()
        elif choice == '7':
            transform_attributes.run()
        elif choice == '8':
            find_correlations.run()
        elif choice == '9':
            propose_new_data.run()
        elif choice == '10':
            print("Exiting the Catology system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
