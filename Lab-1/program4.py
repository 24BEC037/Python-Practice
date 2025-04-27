# Program 4: Divide two numbers

def divide_numbers():
    # Get input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Check for division by zero
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        return
    
    # Calculate quotient
    result = num1 / num2
    
    # Display result
    print(f"The quotient of {num1} divided by {num2} is: {result}")

if __name__ == "__main__":
    divide_numbers()