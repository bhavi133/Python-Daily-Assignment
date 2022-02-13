# 1. Write a Python program to construct the following pattern, using a nested loop number. 

# Expected Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for i in range(1, 10):
    print(str(i) * i)

# 2. Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class. Create a function to display the entire attribute and their values in Student class.

# Sample Output :

# Student ID : 101
# Student Name : Jacqueline Barnett
# Student Class : VII

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None
    
    def set_class(self, student_class):
        self.student_class = student_class
    
    def display(self):
        print(f"Student ID : {self.student_id}, \nStudent Name : {self.student_name}, \nStudent Class : {self.student_class}")

student1 = Student(101, "Jacqueline Barnett")
student1.set_class('VII')
student1.display()

# 3. Write a Python program to insert an element at a specified position into a given list. 

# Original List : [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at nth position in the said list : [1, 1, 9, 2, 3, 4, 4, 5, 1]

def insert_element(num_list, position, element):
    num_list.insert(position, element)
    return num_list

num_list = [1, 1, 2, 3, 4, 4, 5, 1]
position = int(input("Input a position : "))
element = int(input("Input a element : "))
print("After inserting an element at nth position in the said list : ", insert_element(num_list, position, element))
