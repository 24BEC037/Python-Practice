def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    return sum(int(d)**len(str(n)) for d in str(n)) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    return str(n**2).endswith(str(n))

num = 121
print(f"Prime: {is_prime(num)}")
print(f"Perfect: {is_perfect(num)}")
print(f"Armstrong: {is_armstrong(num)}")
print(f"Palindrome: {is_palindrome(num)}")
print(f"Automorphic: {is_automorphic(num)}")