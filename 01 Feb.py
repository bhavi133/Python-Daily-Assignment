# 1. Write a Python program to count the elements in a list until an element is a tuple.

# Sample Input : [10, 20, 30, (10,20), 40]
# Expected Output : 3

lst = [10, 20, 30, (10, 20), 40]
count = 0
for i in lst:
    if isinstance(i, tuple):
        break
    else:
        count += 1
print(count)

# 2. Write a Python program to compute element-wise sum of given tuples.

# Original Tuples:
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Element-wise sum of the said tuples:
# (6, 9, 8, 6)

t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)
print("Original Tuples:")
print(t1)
print(t2)
print(t3)
print("Element-wise sum of the said tuples:")
print(tuple(map(lambda x, y, z: x + y + z, t1, t2, t3)))

# 3. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.

# Original List: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the positive numbers : 48
# Sum of the negative numbers : -32

numbers = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print(numbers)
negative = list(filter(lambda x: x < 0, numbers))
positive = list(filter(lambda x: x > 0, numbers))
print("Sum of the positive numbers : ", sum(positive))
print("Sum of the negative numbers : ", sum(negative))
