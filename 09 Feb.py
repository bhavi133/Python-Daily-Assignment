# 1. Write a Python program to find the sum of all items in a dictionary.

# Sample Input : {'a': 100, 'b':200, 'c':300}
# Sample Output : 600

dic = {'a': 100, 'b':200, 'c':300}
print(sum(dic.values()))

# 2. Write a Python program to merge two dictionaries.

dic1 = {'a': 1, 'b':2, 'c':3}
dic2 = {'d': 4, 'e': 5}
dic1.update(dic2)
print(dic1)

# 3. Write a Python program to check if a substring is present in a given string.,

# Sample Input : str1 ='Hello, World' str2 ='World'
# Sample Output : Yes

str1 = "Hello, World"
str2 = "World"
if str2 in str1:
    print("Yes")
else:
    print("No")
