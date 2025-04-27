# Program 16: Calculate interest

def calculate_interest():
    # Get input from user
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter interest rate (%): "))
    time = float(input("Enter time period (in years): "))
    
    # Calculate interest using formula: I = PRN/100
    interest = (principal * rate * time) / 100
    
    # Display result
    print(f"Interest amount for Principal: ${principal}")
    print(f"At rate: {rate}% for {time} year(s)")
    print(f"Is: ${interest}")

if __name__ == "__main__":
    calculate_interest()