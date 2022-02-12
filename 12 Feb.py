# 1. Write a Python program to generate all permutations of a list in python.

# Sample Input : [1, 2, 3]
# Sample Output : [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

from itertools import permutations

nums = [1, 2, 3]
print(list(permutations(nums)))

# 2. Write a Python program to check whether a string contains all letters of the alphabet.

# Sample Input : "The quick brown fox jumps over the lazy dog"
# Sample Output : True

import string

str1 = "The quick brown fox jumps over the lazy dog"
str1 = str1.lower()
letter = string.ascii_lowercase
print(set(str1) >= set(letter))

# 3. Write a Python program to sort first half of the list in ascending order and second half in descending order.

# Sample Input : [5, 2, 4, 7, 9, 3, 1, 6, 8]
# Sample Output : [1, 2, 3, 4, 9, 8, 7, 6, 5]

nums = [5, 2, 4, 7, 9, 3, 1, 6, 8]
nums.sort()
print(nums[:(len(nums)//2)+1] + nums[:(len(nums)//2):-1])
