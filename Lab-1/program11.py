# Program 11: Convert grams into kg

def grams_to_kg():
    # Get input from user
    grams = float(input("Enter weight in grams: "))
    
    # Convert grams to kilograms (1 kg = 1000 grams)
    kg = grams / 1000
    
    # Display result
    print(f"{grams} gram(s) is equal to {kg} kilogram(s)")

if __name__ == "__main__":
    grams_to_kg()