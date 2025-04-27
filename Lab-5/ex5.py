import random
import string

words = [''.join(random.choice(string.ascii_lowercase) for _ in range(5)) for _ in range(5)]
print(f"Original strings: {words}")

uppercase = [word.upper() for word in words]
print(f"Uppercase list: {uppercase}")