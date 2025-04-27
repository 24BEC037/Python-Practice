# Program 19: Calculate area of a circle

def calculate_circle_area():
    # Get input from user
    radius = float(input("Enter radius of the circle: "))
    
    # Calculate area (A = 22/7 * R * R)
    area = (22/7) * radius * radius
    
    # Display result
    print(f"Area of circle with radius {radius} is: {area} square units")

if __name__ == "__main__":
    calculate_circle_area()