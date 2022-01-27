# 1. Write a Python program to replace the last element in a list with another list.

# Sample Data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

lst1 = [1, 3, 5, 7, 9, 10]
lst2 = [2, 4, 6, 8]
lst1[-1:] = lst2
print(lst1)

# 2. Write a Python program to insert a given string at the beginning of all items in a list.

# Sample List : [1, 2, 3, 4] , string : 'emp'
# Expected Output : ['emp1', 'emp2', 'emp3', 'emp4']

lst = [1, 2, 3, 4]
string = input("Input a string : ")
print([f"{string}{i}" for i in lst])

# 3. Write a Python program to split a given list into two parts where the length of the first part of the list is given.

# Original List:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list : 3
# Splited the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1])

def split_two_list(lst, l):
    return lst[0:l], lst[l:]

lst = [1, 1, 2, 3, 4, 4, 5, 1]
print("Original List:")
print(lst)
l = 3
print("Length of the first part of the list : ", l)
print("Splited the said list into two parts:") 
print(split_two_list(lst, l))
