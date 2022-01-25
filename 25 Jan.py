# 1. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# Sample Input : 5
# Expected Output : 120

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# 2. Write a Python function that takes a list and returns a new list with unique elements of the first list without using set().

# Sample List : [1, 2, 3, 3, 3, 3, 4, 5]
# Unique List : [1, 2, 3, 4, 5]

def remove_duplicates(list1):
    unique = []
    for i in list1:
        if i not in unique:
            unique.append(i)
    return unique

list1 = [1, 2, 3, 3, 3, 3, 4, 5]
print(remove_duplicates(list1))

# 3. Write a Python function that checks whether a passed string is palindrome or not.
# The function should return true if it is a palindrome it should return false.

# Sample Input : 'Wow'
# Expected Output : True

def is_palindrome(str1):
    str1 = str1.lower()
    return str1 == str1[::-1]

print(is_palindrome('Wow'))
print(is_palindrome('MAN'))
