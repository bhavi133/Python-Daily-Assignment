# 1. Write a Python function to insert a string in the middle of a string.

# Sample Input :
# insert_sting_middle('[[]]', 'Python')
# insert_sting_middle('{{}}', 'PHP')

# Sample Output :
# [[Python]]
# {{PHP}}

def insert_sting_middle(str1, word):
    return str1[:2] + word + str1[2:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))

# 2. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

def insert_end(string):
    if len(string) >= 2:
        return string[-2:] * 4
    else:
        return string

print(insert_end('Python'))
print(insert_end('Exercises'))

# 3. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
