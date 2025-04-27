def count_alphabets_digits(s):
    alphabets = sum(c.isalpha() for c in s)
    digits = sum(c.isdigit() for c in s)
    print(f"Alphabets: {alphabets}, Digits: {digits}")

count_alphabets_digits("Hello123")