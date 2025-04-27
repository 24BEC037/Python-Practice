# Program 5: Add, multiply, subtract and divide two numbers

def perform_operations():
    # Get input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Calculate results
    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    
    # Handle division
    if num2 == 0:
        quotient = "undefined (division by zero)"
    else:
        quotient = num1 / num2
    
    # Display results
    print(f"\nResults for {num1} and {num2}:")
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Quotient: {quotient}")

if __name__ == "__main__":
    perform_operations()