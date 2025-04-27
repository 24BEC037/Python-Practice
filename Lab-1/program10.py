# Program 10: Convert dollars to pounds

def dollars_to_pounds():
    # Get input from user
    dollars = float(input("Enter amount in dollars: "))
    
    # Convert dollars to rupees first (1 USD = 48 INR)
    rupees = dollars * 48
    
    # Convert rupees to pounds (1 pound = 70 INR)
    pounds = rupees / 70
    
    # Display result
    print(f"${dollars} is equal to £{pounds}")

if __name__ == "__main__":
    dollars_to_pounds()