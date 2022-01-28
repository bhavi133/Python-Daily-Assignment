# 1. Write a Python program to drop empty Items from a given Dictionary.

# Original Dictionary : {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items : {'c1': 'Red', 'c2': 'Green'}

dic1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
print("Original Dictionary : ", dic1)
dic2 = {key: val for key, val in dic1.items() if val is not None}
print("New Dictionary after dropping empty items : ", dic2)

# 2. Write a Python program to filter the height and width of students, which are stored in a dictionary.

# Original Dictionary : {'Cierra Vega' : (6.2, 70), 'Alden Cantrell' : (5.9, 65), 'Kierra Gentry' : (6.0, 68), 'Pierre Cox' : (5.8, 66)}
# Height > 6ft and Weight> 70kg : {'Cierra Vega': (6.2, 70)}

dic1 = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print("Original Dictionary : ", dic1)
dic2 = {key: val for key, val in dic1.items() if val[0] > 6 and val[1] >= 70}
print("Height > 6ft and Weight > 70kg : ", dic2)

# 3. Write a Python program to sort a tuple by its float element.

# Sample Data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print("Original List:")
print(lst)
print("Sorting a tuple by its float element:")
print(sorted(lst, key=lambda x: float(x[1]), reverse=True))
