# Program 14: Convert Celsius to Fahrenheit

def celsius_to_fahrenheit():
    # Get input from user
    celsius = float(input("Enter temperature in Celsius: "))
    
    # Convert Celsius to Fahrenheit using formula: F = (9/5 * C) + 32
    fahrenheit = (9/5 * celsius) + 32
    
    # Display result
    print(f"{celsius}°C is equal to {fahrenheit}°F")

if __name__ == "__main__":
    celsius_to_fahrenheit()