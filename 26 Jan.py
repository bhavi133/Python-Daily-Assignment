# 1. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

# Sample Input : green-red-yellow-black-white
# Expected Output : black-green-red-white-yellow

string = 'green-red-yellow-black-white'
print(string)
string = string.split('-')
string.sort()
print('-'.join(string))

# 2. Write a Python program to find the values of length six in a given list using lambda.

# Sample List : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Sample Output : [Monday, Friday, Sunday]

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(week_days)
days = list(filter(lambda x : len(x) == 6, week_days))
print(days)

# 3. Write a Python program to find palindromes in a given list of strings using lambda.

# Orginal List : ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes  : ['php', 'aaa']

texts = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
print("Original List : ", texts)
result = list(filter(lambda x : x == x[::-1], texts))
print("List of palindromes : ", result)
