# 1. Write a Python program to create string consisting of the non-negative integers up to n inclusive.

# Input : 4
# Output : 0 1 2 3 4

# Input : 15
# Output : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 

n = int(input("Input a number : "))
for i in range(n+1):
    print(str(i), end=" ")

# 2. Write a Python program to generate a list, containing the fibonacci sequence, up until the nth term.

# Sample Output:
# First 5 fibonacci numbers : [0, 1, 1, 2, 3]

def fibonacci(n):
    lst = []
    a = 0
    b = 1
    if n == 1:
        lst.append(a)
    elif n == 2:
        lst.append(a)
        lst.append(b)
    else:
        lst.append(a)
        lst.append(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            lst.append(c)
    return lst

n = int(input("Input a number : "))
print(f"First {n} fibonacci numbers : ", fibonacci(n))

# 3. Write a Python program to check if all the elements of a list are included in another given list. 

# Sample Input : 
# test_includes_all([10, 20, 30, 40, 50, 60], [20, 40]))
# test_includes_all([10, 20, 30, 40, 50, 60], [20, 80]))

# Sample Output:
# True
# False 

def test_includes_all(lst1, lst2):
    for i in lst2:
        if i not in lst1:
            return False
    return True

print(test_includes_all([10, 20, 30, 40, 50, 60], [20, 40]))
print(test_includes_all([10, 20, 30, 40, 50, 60], [20, 80]))
