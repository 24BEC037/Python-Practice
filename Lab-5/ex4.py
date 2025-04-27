import random

numbers = [random.randint(-50, 50) for _ in range(30)]
print(f"Original list: {numbers}")

positive = [num for num in numbers if num > 0]
negative = [num for num in numbers if num < 0]
print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")