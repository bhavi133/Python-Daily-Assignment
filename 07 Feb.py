# 1. Write a Python program to calculate the circumference of a circle.

from math import pi

def circumference_of_circle(radius):
    return 2 * pi * radius

radius = float(input("Input a radius : "))
print("The circumference of a circle is : %.2f" %circumference_of_circle(radius), 'cm')

# 2. Write a Python program to calculate the area of a rectangle.

def area_of_rectangle(length, breadth):
    return length * breadth

length = float(input("Input the length of a rectangle : "))
breadth = float(input("Input the breadth of a rectangle : "))
print("The area of a rectangle is : %.2f" %area_of_rectangle(length, breadth), 'sq.cm')

# 3. Write a Python program to calculate the area of a square.

def area_of_square(side):
    return side * side

side= float(input("Input the side of a square : "))
print("The area of a rectangle is : %.2f" %area_of_square(side), 'sq.cm')
