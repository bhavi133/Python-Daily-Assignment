# 1. Write a Python program to access multiple elements of specified index from a given list.

# Sample Input:
# Original List : [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Index List : [0, 3, 5, 7, 10]

# Sample Output:
# Items with specified index of the said list : [2, 4, 9, 2, 1]

nums_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
print("Original List : ", nums_list)
index_list = [0, 3, 5, 7, 10]
print("Index List : ", index_list)
print("Items with specified index of the said list : ", [nums_list[i] for i in index_list])

# 2. Write a Python program to remove all elements from a given list present in another list.

# Original Lists:
# list1 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 : [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2' : [1, 3, 5, 7, 9, 10]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
print("Original Lists:")
print(list1)
print(list2)
print("Remove all elements from 'list1' present in 'list2:")
print([i for i in list1 if i not in list2])
print(list(filter(lambda x : x not in list2, list1)))

# 3. Write a Python program to convert a given list of strings into list of lists. 

# Original list of strings : ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists : [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

colors = ['Red', 'Maroon', 'Yellow', 'Olive']
print("Original list of strings : ", colors)
print("Convert the said list of strings into list of lists : ", [list(i) for i in colors])
