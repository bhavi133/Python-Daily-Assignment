# 1. Write a Python program to compute average of two given lists. 

# Original Lists:
# [1, 1, 3, 4, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 4, 5, 7, 8]
# Average of two lists:
# 3.823529411764706

def average(l1, l2):
    return sum(l1 + l2) / len(l1 + l2)

l1 = [1, 1, 3, 4, 4, 5, 6, 7]
l2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
print("Original Lists:")
print(l1)
print(l2)
print("Average of two lists:")
print(average(l1, l2))

# 2. Write a Python program to count integer in a given mixed list. 

# Original List : [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of integers in the said mixed list : 6

lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print("Original List : ", lst)
print("Number of integers in the said mixed list : ", len([i for i in lst if type(i) == int]))

# 3. Write a Python program to extract a specified column from a given nested list. 

# Original Nested List : [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Extract 1st column : [1, 2, 1]

# Original Nested list : [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Extract 3rd column : [3, -5, 1]

def remove_column(lst, n):
    return [i.pop(n) for i in lst]

lst =  [[1, 2, 3], [2, 4, 5], [1, 1, 1]] 
n = 0
print("Original Nested list : ", lst)
print("Extract 1st column : ", remove_column(lst, n))

lst = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
n = 2
print("Original Nested list : ", lst)
print("Extract 3rd column : ", remove_column(lst, n))
