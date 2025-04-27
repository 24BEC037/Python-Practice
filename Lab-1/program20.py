# Program 20: Calculate area of a triangle

def calculate_triangle_area():
    # Get input from user
    height = float(input("Enter height of the triangle: "))
    length = float(input("Enter length of the triangle: "))
    
    # Calculate area (A = H*L/2)
    area = height * length / 2
    
    # Display result
    print(f"Area of triangle with height {height} and length {length} is: {area} square units")

if __name__ == "__main__":
    calculate_triangle_area()