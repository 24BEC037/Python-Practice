# Program 1: Add two numbers

def add_numbers():
    # Get input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Calculate sum
    result = num1 + num2
    
    # Display result
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    add_numbers()