# Program 3: Multiply two numbers

def multiply_numbers():
    # Get input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Calculate product
    result = num1 * num2
    
    # Display result
    print(f"The product of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    multiply_numbers()