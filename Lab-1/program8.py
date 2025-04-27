# Program 8: Convert dollars to Indian Rupees

def dollars_to_rupees():
    # Get input from user
    dollars = float(input("Enter amount in dollars: "))
    
    # Convert dollars to rupees (1 USD = 48 INR)
    rupees = dollars * 48
    
    # Display result
    print(f"${dollars} is equal to ₹{rupees}")

if __name__ == "__main__":
    dollars_to_rupees()