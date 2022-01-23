# 1. Write a Python program to remove an empty tuple(s) from a list of tuples.

# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

list1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(list1)
list2 = [i for i in list1 if i]
print(list2)

list1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(list1)
list2 = [i for i in list1 if len(i) >= 1]
print(list2)

# 2. Write a Python program to calculate the sum of the digits in an integer.

# Sample Data : 12345
# Expected Output : 15

str1 = '12345'
sum = 0
for i in str1:
    sum += int(i)
print(sum)

# 3. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

list1 = ['abc', 'xyz', 'aba', '1221']
print(list1)
list2 = [i for i in list1 if len(i) > 2 and i[0] == i[-1]]
print(list2)
