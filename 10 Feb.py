# 1. Write a Python program to calculate the product of the unique numbers of a given list. 

# Original List : [10, 20, 30, 40, 20, 50, 60, 40]
# Product of the unique numbers of the said list : 720000000

def product(nums):
    ctr = 1
    for i in list(set(nums)):
        ctr = ctr * i
    return ctr

nums = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ", nums)
print("Product of the unique numbers of the said list : ", product(nums))

# 2. Write a Python program to get the items from a given list with specific condition. 

# Original List : [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Number of Items of the said list which are even and greater than 45 : 5

def func(nums):
    return len([i for i in nums if i % 2 == 0 and i > 45])

nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
print("Original List : ", nums)
print("Number of Items of the said list which are even and greater than 45 : ", func(nums))

# 3. Write a Python program to extract numbers from a given string. 

# Original String : 'red 12 black 45 green'
# Extract numbers from the said string : [12, 45]

def extract_numbers(str1):
    return [int(i) for i in str1.split() if i.isdigit()]

str1 = 'red 12 black 45 green'
print("Original String : ", str1)
print("Extract numbers from the said string : ", extract_numbers(str1))
