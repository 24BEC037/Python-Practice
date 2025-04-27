import random

list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(8)]
print(f"First list: {list1}")
print(f"Second list: {list2}")

list3 = [num for num in list1 if num not in list2]
print(f"Elements in first list not present in second: {list3}")