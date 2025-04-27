def remove_substring(s, to_remove):
    len_remove = len(to_remove)
    result = ''
    i = 0
    while i < len(s):
        if s[i:i+len_remove] == to_remove:
            i += len_remove
        else:
            result += s[i]
            i += 1
    return result

s = input('Enter main string: ')
to_remove = input('Enter string to remove: ')
print('Result:', remove_substring(s, to_remove))