def is_substring(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    for i in range(len1 - len2 + 1):
        if s1[i:i+len2] == s2:
            return True
    return False

s1 = input('Enter first string: ')
s2 = input('Enter second string: ')
print('Is second string in first string:', is_substring(s1, s2))