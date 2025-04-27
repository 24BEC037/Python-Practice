import random

numbers = [random.randint(1, 30) for _ in range(50)]
print(f"Original list: {numbers}")

unique_numbers = list(set(numbers))
print(f"List after removing duplicates: {unique_numbers}")