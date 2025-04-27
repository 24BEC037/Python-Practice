# Program 17: Calculate area & perimeter of a square

def calculate_square_measurements():
    # Get input from user
    length = float(input("Enter length of the square: "))
    
    # Calculate area (A = L^2)
    area = length ** 2
    
    # Calculate perimeter (P = 4L)
    perimeter = 4 * length
    
    # Display results
    print(f"For a square with length {length}:")
    print(f"Area: {area} square units")
    print(f"Perimeter: {perimeter} units")

if __name__ == "__main__":
    calculate_square_measurements()