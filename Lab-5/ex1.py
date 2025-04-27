import random

odd = [random.randrange(1, 10, 2) for _ in range(5)]
even = [random.randrange(2, 10, 2) for _ in range(4)]
print(f"Odd list: {odd}")
print(f"Even list: {even}")

odd[2] = even
print(f"After replacement: {odd}")

flattened = []
for num in odd:
    if isinstance(num, list):
        flattened.extend(num)
    else:
        flattened.append(num)
print(f"Flattened list: {flattened}")

flattened.sort()
print(f"Sorted list: {flattened}")