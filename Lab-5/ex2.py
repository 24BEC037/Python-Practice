import random

numbers = [random.randint(1, 100) for _ in range(20)]
print(f"Generated list: {numbers}")

try:
    search_num = int(input("Enter number to find: "))
    positions = [i for i, num in enumerate(numbers) if num == search_num]
    
    if positions:
        print(f"Number found at positions: {positions}")
    else:
        print("Number not found in list")
except ValueError:
    print("Invalid input. Please enter an integer.")