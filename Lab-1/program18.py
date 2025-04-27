# Program 18: Calculate area & perimeter of a rectangle

def calculate_rectangle_measurements():
    # Get input from user
    length = float(input("Enter length of the rectangle: "))
    breadth = float(input("Enter breadth of the rectangle: "))
    
    # Calculate area (A = L*B)
    area = length * breadth
    
    # Calculate perimeter (P = 2(L+B))
    perimeter = 2 * (length + breadth)
    
    # Display results
    print(f"For a rectangle with length {length} and breadth {breadth}:")
    print(f"Area: {area} square units")
    print(f"Perimeter: {perimeter} units")

if __name__ == "__main__":
    calculate_rectangle_measurements()