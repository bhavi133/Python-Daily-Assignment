# 1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : 'w'
# Expected Result : ''

def func(str1):
    if len(str1) >= 2:
        return str1[0:2] + str1[-2:]
    else:
        return ""

print(func('w3resource'))
print(func('w3'))
print(func('w'))

# 2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def func(str1):
    if len(str1) > 2:
        if str1[-3:] != 'ing':
            return str1 + 'ing'
        else:
            return str1 + 'ly'
    else:
        return str1

print(func('ab'))
print(func('abc'))
print(func('string'))

# 3. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def char_mix_up(str1, str2):
    return str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]

print(char_mix_up('abc', 'xyz'))
