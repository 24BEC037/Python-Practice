# Program 12: Convert kgs into grams

def kg_to_grams():
    # Get input from user
    kg = float(input("Enter weight in kilograms: "))
    
    # Convert kilograms to grams (1 kg = 1000 grams)
    grams = kg * 1000
    
    # Display result
    print(f"{kg} kilogram(s) is equal to {grams} gram(s)")

if __name__ == "__main__":
    kg_to_grams()