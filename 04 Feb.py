# 1. Write a Python program to sort each sublist of strings in a given list of lists.

# Original List : [['orange', 'blue'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists : [['blue', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

colors1 = [['orange', 'blue'], ['black', 'white'], ['white', 'black', 'orange']]
print("Original List : ", colors1)
colors2 = [sorted(i) for i in colors1]
print("After sorting each sublist of the said list of lists : ",colors2)

# 2. Write a Python program to sort a given list of lists by length and value.

# Original List : [[2], [0], [1, 3], [0, 7], [9, 11], [17, 13, 15]]
# Sort the list of lists by length and value : [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

nums1 = [[2], [0], [1, 3], [0, 7], [9, 11], [17, 13, 15]]
print("Original List : ", nums1)
nums2 = sorted(nums1)
nums3 = sorted(nums2, key=len)
print("Sort the list of lists by length and value : ", nums3)

# 3. Write a Python program to find the maximum and minimum values in a given heterogeneous list. 

# Original List : ['Python', 3, 2, 4, 5, 'Java']
# Maximum and Minimum values in the said list : (5, 2)

lst = ['Python', 3, 2, 4, 5, 'Java']
print("Original List : ", lst)
max_value = max(i for i in lst if type(i) == int)
min_value = min(i for i in lst if type(i) == int)
print("Maximum and Minimum values in the said list : ", (max_value, min_value))
