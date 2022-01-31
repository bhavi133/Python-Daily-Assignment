# 1. Write a Python program to check if two given sets have no elements in common.

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
set3 = {8}
print("Original set elements:")
print(set1)
print(set2)
print(set3)
print("\nCompare two given sets have no element(s) in common:")
print("\nCompare set1 and set2:")
print(set1.isdisjoint(set2))
print("\nCompare set2 and set3:")
print(set2.isdisjoint(set3))
print("\nCompare set3 and set1:")
print(set3.isdisjoint(set1))

# 2. Write a Python program to swap two variables.

def swap(a, b):
    print(f"The value of a before swapping : {a}")
    print(f"The value of b before swapping : {b}")
    a, b = b, a
    print(f"\nThe value of a after swapping : {a}")
    print(f"The value of b after swapping : {b}")

swap(2, 3)

# 3. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2

print(difference(12))
print(difference(17))
print(difference(19))
