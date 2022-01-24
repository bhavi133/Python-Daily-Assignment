# 1. Python program to interchange first and last elements in a list

list1 = [1, 2, 3, 4, 5]
print(list1)
list1[0], list1[-1] = list1[-1], list1[0]
print(list1)

# 2. Find sum and average of List in Python

list1 = [1, 2, 3, 4, 5]
print(sum(list1))
print(sum(list1)//len(list1))

# 3. Python program to find second largest number in a list

def second_largest(list1):
    result = sorted(list1)
    return result[-2]

print(second_largest([32, 4, 2, 1, 5, 6, 5, 6, 64]))
