# 1. WAP to check whether the each word in a string begins with upper letter on not. If all the word begins with Upper letter print True otherwise print false.

# Sample input :- "I Like Python"
# Output:- True
# Sample Input : "I Like python "
# Output :- False

def is_upper(str1):
    return str1.istitle()

print(is_upper("I Like Python"))
print(is_upper("I Like python"))

# 2. Write a Python Program to print all the duplicates from a given list.(without using set function).

# Sample input: [1,2,2,3,3,4,4,4]
# Sample output:- [2,3,4]

num1 = [1, 2, 2, 3, 3, 4, 4, 4]
num2 = []
for i in num1:
    if i not in num2 and num1.count(i) > 1:
        num2.append(i)
print(num2)

# 3. Write a Python Program to print the symmetric difference between two list.

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
res1 = [i for i in l1 if i not in l2]
res2 = [i for i in l2 if i not in l1]
print(res1+res2)
