from math import factorial

def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def npr(n, r):
    return factorial(n) // factorial(n - r)

print(ncr(5, 2))
print(npr(5, 2))