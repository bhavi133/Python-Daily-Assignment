# 1. Write a Python program to check if there are duplicate values in a given flat list. 

# Sample Output:
# Original List : [1, 2, 3, 4, 5, 6, 7]
# Check if there are duplicate values in the said given flat list : False

# Original List : [1, 2, 3, 3, 4, 5, 5, 6, 7]
# Check if there are duplicate values in the said given flat list : True

def duplicates(nums):
    if len(nums) != len(set(nums)):
        return True
    else:
        return False

nums = [1, 2, 3, 4, 5, 6, 7]
print("Original List : ", nums)
print("Check if there are duplicate values in the said given flat list : ", duplicates(nums))

nums = [1, 2, 3, 3, 4, 5, 5, 6, 7]
print("Original List : ", nums)
print("Check if there are duplicate values in the said given flat list : ", duplicates(nums))

# 2. Write a Python program to convert a given number (integer) to a list of digits.

# Sample Input : 123
# Sample Output : [1, 2, 3]

num = int(input("Input a number : "))
print(list(map(int, str(num))))

# 3. Write a Python program to remove all the values except integer values from a given array of mixed values. 

# Original List: [34.67, 12, -94.89, 'Python', 0, 'C#']
# After removing all the values except integer values from the said array of mixed values: [12, 0]

lst1 = [34.67, 12, -94.89, 'Python', 0, 'C#']
print("Original List : ", lst1)
lst2 = []
for i in lst1:
    if type(i) == int:
        lst2.append(i)
    else:
        pass

print("After removing all the values except integer values from the said array of mixed values : ", lst2)
