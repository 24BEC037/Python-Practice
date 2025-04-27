import random

fahrenheit = [random.randint(32, 212) for _ in range(10)]
print(f"Fahrenheit temps: {fahrenheit}")

celsius = [round((f-32)*5/9, 1) for f in fahrenheit]
print(f"Celsius equivalents: {celsius}")