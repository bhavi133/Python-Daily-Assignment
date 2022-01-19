# 1. Write a Python program to filter a list of integers using lambda.

# Original list of integers :
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list :
# [2, 4, 6, 8, 10]
# Odd numbers from the said list :
# [1, 3, 5, 7, 9]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers from the said list:")
print(list(filter(lambda x : x % 2 == 0, list1)))
print("Odd numbers from the said list:")
print(list(filter(lambda x : x % 2 != 0, list1)))

# 2. Write a Python program to add two given lists using map and lambda.

# Original list :
# [1, 2, 3]
# [4, 5, 6]
# Result : after adding two list
# [5, 7, 9]

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print("After adding two lists:")
print(list(map(lambda x, y : x + y, l1, l2)))

# 3. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# Expected Output : 0 1 2 4 5

for i in range(0, 7):
    if (i == 3 or i == 6):
        continue
    print(i, end=" ")
