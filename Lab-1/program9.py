# Program 9: Convert Indian Rupees to dollars

def rupees_to_dollars():
    # Get input from user
    rupees = float(input("Enter amount in rupees: "))
    
    # Convert rupees to dollars (1 USD = 48 INR)
    dollars = rupees / 48
    
    # Display result
    print(f"₹{rupees} is equal to ${dollars}")

if __name__ == "__main__":
    rupees_to_dollars()