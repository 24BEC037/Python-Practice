# Program 7: Convert minutes into hours

def minutes_to_hours():
    # Get input from user
    minutes = float(input("Enter number of minutes: "))
    
    # Convert minutes to hours (1 hour = 60 minutes)
    hours = minutes / 60
    
    # Display result
    print(f"{minutes} minute(s) is equal to {hours} hour(s)")

if __name__ == "__main__":
    minutes_to_hours()