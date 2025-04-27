# Program 15: Convert Fahrenheit to Celsius

def fahrenheit_to_celsius():
    # Get input from user
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius using formula: C = 5/9 * (F - 32)
    celsius = 5/9 * (fahrenheit - 32)
    
    # Display result
    print(f"{fahrenheit}°F is equal to {celsius}°C")

if __name__ == "__main__":
    fahrenheit_to_celsius()