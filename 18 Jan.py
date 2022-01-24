# 1. Write a Python program to calculate the length of a string without using built-in function.

def length(str1):
    len = 0
    for i in str1:
        len += 1
    return len

print(length('w3resource'))
print(length('python'))

# 2. Write a Python function to reverses a string if it's length is a multiple of 4 without using built-in function.

def reverse_string(str1):
    if len(str1) % 4 == 0:
        return str1[::-1]
    else:
        return str1

print(reverse_string('exercise'))
print(reverse_string('python'))

# 3. Write a Python program to print the index of the character in a string.

# Sample string : w3resource
# Expected output :
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - 
# Current character c position at 8
# Current character e position at 9

str1 = 'w3resource'
for i, j in enumerate(str1):
    print(f"Current character {j} position at {i}")
