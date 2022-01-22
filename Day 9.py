# 1. Write a Python program to reverse a string without using any built-in function and slicing.

# Sample String: "1234abcd"
# Expected Output: "dcba4321"

def reverse(string):
    str1 = ""
    for i in string:
        str1 = i + str1
    return str1

string = "1234abcd"
print(reverse(string))

# 2. Write a Python program to convert a list of characters into a string.

# Sample List : ['a', 'b', 'c', 'd']
# Expected Output : abcd

list1 = ['a', 'b', 'c', 'd']
string = ""
for i in list1:
    string += i
print(string)

# 3. Write a Python program calculate the product, multiplying all the numbers of a given tuple.

# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648

def multiply(tup1):
    ctr = 1
    for i in tup1:
        ctr *= i
    return ctr

tup1 = (4, 3, 2, 2, -1, 18)
print("Original Tuple:")
print(tup1)
print("Product - multiplying all the numbers of the said tuple : ", multiply(tup1))

tup2 = (2, 4, 8, 8, 3, 2, 9)
print("Original Tuple:")
print(tup1)
print("Product - multiplying all the numbers of the said tuple : ", multiply(tup2))

