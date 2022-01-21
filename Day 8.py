# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

for i in range(1500, 2701):
    if (i % 7 == 0) and (i % 5 == 0):
        print(i, end=" ")

# 2. Write a Python program that accepts a string and calculate the number of digits and letters.

# Sample Data : Python 3.2
# Expected Output :
# Letters : 6
# Digits : 2

def count(str1):
    letter = 0
    digits = 0
    for i in str1:
        if i.isalpha():
            letter += 1
        elif i.isdigit():
            digits += 1
        else:
            pass

    print(letter)
    print(digits)

str1 = "Python 3.2"
count(str1)

# 3. Write a Python program to convert month name to a number of days.

# Expected Output:

# List of months: January, February, March, April, May, June, July, August, September, October, November, December
# Input the name of month: February
# Number of days: 28/29 days

print("List of months : January, February, March, April, May, June, July, August, September, October, November, December")
month = input("Input the name of month : ")
if month == "February":
    print("Number of days : 28/29 days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
    print("Number of days : 31 days")
elif month in ("April", "June", "September", "November"):
    print("Number of days : 30 days")
else:
    print("Wrong month name")
