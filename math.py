# Here is a program that shows basic math operations
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Olamide Dinah
# Upper Canada College

# Tell the user what the program will do...




print ("This program will perform mathematical calculations")

# 'num1' and 'num2' will hold numbers typed in from the keyboard
# and they will be stored as something called a 'float' which
# is another way to say 'decimal'

x1 = float(input("What is the x value? \n"))
y1 = float(input("What is the y value? \n"))
x2 = float(input("What is the second x value? \n"))
y2 = float(input("What is the second y value? \n"))


a = (y2 - y1) / (x2 - x1)
b = y1 - a * x1

print('slope: ', a)
print('intercept: ', b)