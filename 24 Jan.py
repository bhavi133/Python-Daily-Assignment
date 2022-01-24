# 1. Write a Python program to get the largest number from a list without using built-in function.

# Sample Input : [1, 5, -8, 0, -2]
# Expected Output : 5

def largest(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max

list1 = [1, 5, -8, 0, -2]
print(largest(list1))

# 2. Write a Python program to get the smallest number from a list without using built-in function.

# Sample Input : [1, 5, -8, 0, -2]
# Expected Output : -8

def smallest(list1):
    min = list1[0]
    for i in list1:
        if i <= min:
            min = i
    return min

list1 = [1, 5, -8, 0, -2]
print(smallest(list1))

# 3. Write a Python program to unzip a list of tuples into individual lists.

# Sample Input : [(1,2), (3,4), (8,9)]
# Expected Output : [(1, 3, 8), (2, 4, 9)]

l1 = [(1, 2), (3, 4), (8, 9)]
print(list(zip(*l1)))
