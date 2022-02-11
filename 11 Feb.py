# 1. Write a Python program to split a given multiline string into a list of lines. 

# Original String : 'This
# is a
# multiline
# string'.

# Split the said multiline string into a list of lines : ['This', 'is a', 'multiline', 'string.', '']

str1 = '''This
is a
multiline
string'''
print("Original String : ", str1)
print("Split the said multiline string into a list of lines : ", str1.split('\n'))

# 2. Write a Python program find the common values that appear in two given strings. 

# Original Strings:
# Python3
# Python2.7

# Intersection of two said String : Python

def string_intersection(str1, str2):
    str3 = ""
    for i in str1:
        if i in str2:
            str3 = str3 + i
    return str3

str1 = "Python3"
str2 = "Python2.7"
print("Original Strings:")
print(str1)
print(str2)
print("Intersection of two said String : ", string_intersection(str1, str2))

# 3. Write a Python program to select an item randomly from a list. 

# Sample Input : ['Red', 'Blue', 'Green', 'White', 'Black']
# Sample Output : Black

import random
colors = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(colors))
