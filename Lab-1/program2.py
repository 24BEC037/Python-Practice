# Program 2: Subtract two numbers

def subtract_numbers():
    # Get input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Calculate difference
    result = num1 - num2
    
    # Display result
    print(f"The difference between {num1} and {num2} is: {result}")

if __name__ == "__main__":
    subtract_numbers()