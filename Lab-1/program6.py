# Program 6: Convert hours into minutes

def hours_to_minutes():
    # Get input from user
    hours = float(input("Enter number of hours: "))
    
    # Convert hours to minutes (1 hour = 60 minutes)
    minutes = hours * 60
    
    # Display result
    print(f"{hours} hour(s) is equal to {minutes} minute(s)")

if __name__ == "__main__":
    hours_to_minutes()