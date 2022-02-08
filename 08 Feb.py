# 1. Write a Python program to check leap year.

def leap_year(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

year = int(input("Input a year : "))
print(leap_year(year)) 

# 2. Write a Python program to check if a number is positive, negative or zero.

num = int(input("Input a number : "))
if num < 0:
    print("It is a negative number")
elif num == 0:
    print("It is a zero")
else:
    print("It is a positive number")

# 3. Write a Python program to find the largest among three numbers.

def largest(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n1:
        return n2
    else:
        return n3

n1 = int(input("Input the first number : "))
n2 = int(input("Input the second number : "))
n3 = int(input("Input the third number : "))
print(largest(n1, n2, n3))
