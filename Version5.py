# Version 5.0 (1.5) of my tkinter/python project
# Author: Olamide Dinah
# Student of Upper Canada College (grade9)
# Modified for instructional purposes



# Simplified sersion as tkinter
import tkinter as tk
# Importing all exposed tkinter objects into the namespace
from tkinter import *


# Setting
large_font =('Comic Sans MS',20,)
small_font = ('Comic Sans MS',12,)
medium_font = ('Comic Sans MS',15,)




######################
#Slope-Int Form Calculator
#######################

# setting up the window (size,color,title)
MyWindow = tk.Tk()
MyWindow.title("Welcome")
MyWindow.geometry('750x450')
MyWindow.configure(bg='orange')

#declaring a function that executes 
def clicked():
    a = float(number1.get())
    b = float(number2.get())
    c = float(number3.get())

    m = (int(a)) / (int(b))
    y = (int(b)) / (int(b))
    z = (int(c)) / (int(b))





# this code is just statement outputs for all differnet possible outcomes.
    if z > 0 and m > 0 and b > 0:

        result = "y =" + "-" + str(m) + "x -" + str(z)
        labelAns.config(text="Result is %s" % result)
    
    if z > 0 and m < 0 and b > 0:

        result = "y =" + " " + str(int(m) / int(-1)) + "x -" + str(z)
        labelAns.config(text="Result is %s" % result)

    if z < 0 and m < 0 and b > 0:

        result = "y =" + " " + str(int(m) / int(-1)) + "x +" + str(int(z) / int(-1))
        labelAns.config(text="Result is %s" % result)


# accounting for when the y value is negative.

# this code is just statement outputs for all differnet possible outcomes.
    if z > 0 and m > 0 and b < 0:
       # steps.config(text = str(int(a) "+" + - str(int(a) + str(int(b) + str(int(m) + "=" +  str(int(a) + "\n" + str(int(b) + str(int(m) - str(int(m) + "=" + "-" + str(int(a) + str(int(m) + "\n" + str(int(b) / str(int(b) + "=" + str(int(a) / str(int(b) + str(int(m) / str(int(b))  
        labelsteps.config(text=str(a) + "x" + str(b) + "y" + str(c) + "=" + str(0) + "\n" + str(b) + "y" + str(c) + "=" + str(a/-1) + "x" + "\n" + str(b) + "y" + "=" + str(a/-1) + "x" + "+" + str(c/-1) + "\n" + "y" + "=" + str(-a/b) + "x" + str(-c/b) ) 
        result = "y" + "=" + str(-a/b) + "x" + str(-c/b)
        labelAns.config(text="Result is %s" % result)
        explanation.config(text="In this scenario, you must isolate for the \n variable Y. This is done by shifting over the\n variables to the other side. One thing you may have \nnoticed is that the values  ended up being negative.This \nis as it is considered poor practice to leave the \n negative,  which means  the negative  had to be \ndivided out.")

    
    if z > 0 and m < 0 and b < 0:

        result = "y =" + " " + str(int(m) / int(-1)) + "x -" + str(z)
        labelAns.config(text="Result is %s" % result)

    if z < 0 and m < 0 and b < 0:

        result = "y =" + " " + str(int(m) / int(-1)) + "x +" + str(int(z) / int(-1))
        labelAns.config(text="Result is %s" % result)


# Creating a easily changeable  Var value that allows or easy value collection
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
# Labels of space
labelNum5 = tk.Label(bg='orange')
labelNum6 = tk.Label(bg='orange')
labelNum7 = tk.Label(bg='orange')
labelNum8 = tk.Label(bg='orange')
labelNum9 = tk.Label(bg='orange')
labelNum10 = tk.Label(bg='orange')
labelNum11 = tk.Label(bg='orange')


# Creating all of the labels with text information
labelTitle = tk.Label(MyWindow, font=small_font, text="Standard Form & Slope-Int Form", bg = 'orange')
labelNum1 = tk.Label(MyWindow, font =small_font, text="Enter the a value", bg = 'orange')
labelNum2 = tk.Label(MyWindow, font =small_font, text="Enter the b value", bg = 'orange')
labelNum3 = tk.Label(MyWindow, font =small_font, text="Enter the c value", bg = 'orange')
labelsteps = tk.Label(MyWindow, font =medium_font, text = "Click this button to show steps!", bg = 'lightblue')
labelAns = tk.Label(MyWindow, font=small_font, text="", bg = 'orange')
explanation = tk.Label(MyWindow, font=medium_font, text="How?", bg = 'lightblue')
# Arranging all of the labels in a "grid" where row "0", column "0" 
# represents the upper left hand corner
# Also positioning the labels I created earlier
labelTitle.grid(row=0, column=1)
labelNum1.grid(row=1, column=0)

labelNum2.grid(row=2, column=0)

labelNum3.grid(row=3, column=0)

labelsteps.grid(row=5, column=0)

labelNum5.grid(row=4, column=0)

labelNum6.grid(row=6, column=0)

labelNum7.grid(row=7, column=0)

labelNum8.grid(row=8, column=0)

labelAns.grid(row=7, column=1)

labelNum9.grid(row=9, column=2)

labelNum10.grid(row=9, column=3)

labelNum11.grid(row=9, column=4)

explanation.grid(row=7, column=5)



# Setting up and positioning entry boxes, linking them two the stringvars and subsequently math above - setting up colour schemes aswell
entryNum1 = tk.Entry(MyWindow, textvariable=number1, font = medium_font, borderwidth=5, relief ="raised", bg = 'white', highlightbackground='lightblue', fg = 'orange')
entryNum1. grid(row=1, column=1)
entryNum2 = tk.Entry(MyWindow, textvariable=number2, font = medium_font, borderwidth=5, relief ="raised", bg = 'white', highlightbackground='lightblue', fg = 'orange')
entryNum2. grid(row=2, column=1)
entryNum3 = tk.Entry(MyWindow, textvariable=number3, font = medium_font, borderwidth=5, relief ="raised", bg = 'white', highlightbackground='lightblue', fg = 'orange')
entryNum3. grid(row=3, column=1)


# Calling the function I defined earlier
# Calculation is performed when the "clicked" function is called
buttonCal = tk.Button(MyWindow, text="Calculate", font=medium_font,command=clicked, fg = 'orange', highlightbackground = 'lightblue')
buttonCal.grid(row=7, column=0)


# defining another function
def hide():
    labelsteps.config(text="")
    small_font = ('Comic Sans MS',3,)

# calling that function when the Hide Steps button is pressed
buttonstep = tk.Button(MyWindow, text="Hide Steps", font=medium_font, command=hide, fg = 'orange', highlightbackground = 'lightblue')
buttonstep.grid(row=5, column=1)


'''restart function work in progress
MyWindow=Tk()
def restart():
root.mainloop() 
'''


# defining another function
def exit():
    MyWindow.destroy() 

           
# calling it
restart = tk.Button(MyWindow, text="Quit", command =exit,font=medium_font, fg = 'orange', highlightbackground = 'lightblue')
restart.config(height = 1, width = 10,)
restart.grid(row=1, column=5)



##################
#Title Page
##################


# Creating another window as a child of the MyWindow
intro = Toplevel(MyWindow)
intro.attributes("-topmost", True)
intro.title("Welcome User!")
intro.geometry('500x225')
intro.configure(bg='lightblue')

# creating a function
def clicked():
    name1 = (firstname.get())
    name2 = (lastname.get())
    #'Slicing' values from the result in order to create a username
    result = name1[:3] + name2[:1]
    labelAnswer.config(text="Your Username is %s" % result + " Welcome! \n please exit this window")
  
 
# easily changeable value holder
firstname = tk.StringVar()
lastname = tk.StringVar()


# again indetifying labels for entry buttons
labelTitle = tk.Label(intro, text="Create a Name!", font=medium_font, bg = 'lightblue')
labelName1 = tk.Label(intro, text="Enter First-Name", font=medium_font, bg = 'lightblue')
labelName2 = tk.Label(intro, text="Enter Last-Name", font=medium_font, bg = 'lightblue')
labelAnswer = tk.Label(intro, text="The answer is", font=medium_font, bg = 'lightblue')

# positioning these labels
labelTitle.grid(row=0, column=2)
labelName1.grid(row=1, column=0)
labelName2.grid(row=2, column=0)
labelAnswer.grid(row=5, column=2)

# creating/positioning the entry buttons
entryname1 = tk.Entry(intro, textvariable=firstname, font=medium_font, fg = 'orange',highlightbackground='lightblue')
entryname1. grid(row=1, column=2)
entryname2 = tk.Entry(intro, textvariable=lastname, font=medium_font, fg = 'orange',highlightbackground='lightblue')
entryname2. grid(row=2, column=2)


# calling on the function created earlier - creating the name 
buttondo = tk.Button(intro, text="Create Name!", command=clicked, font=medium_font)
buttondo.grid(row=5, column=0)


###########################
#Slope Calculator Code
##################


# creating the final window again as a child
root = Toplevel(MyWindow)
root.title()
root.geometry('450x225')
root.configure(bg='lightblue')


def clicked2():
    a = float(x1.get())
    b = float(y1.get())
    c = float(x2.get())
    d = float(y2.get())

    z = (int(d)) - (int(b))
    y = (int(c)) - (int(a))

    result = str(z/y)

    labelAnswer2.config(text="Result is %s" % result)
 
 
x1 = tk.StringVar()
y1 = tk.StringVar()
x2 = tk.StringVar()
y2 = tk.StringVar()


labelTitle = tk.Label(root, text="Solve for Slope! (A Value)", bg = 'lightblue')
labelNum1 = tk.Label(root, text="Enter first x value", bg = 'lightblue')
labelNum2 = tk.Label(root, text="Enter first y value", bg = 'lightblue')
labelNum3 = tk.Label(root, text="Enter second x value", bg = 'lightblue')
labelNum4 = tk.Label(root, text="Enter second y value", bg = 'lightblue')
labelAnswer2 = tk.Label(root, text="The answer is", bg = 'lightblue')


labelTitle.grid(row=0, column=2)
labelNum1.grid(row=1, column=0)
labelNum2.grid(row=2, column=0)
labelNum2.grid(row=2, column=0)
labelNum3.grid(row=3, column=0)
labelNum3.grid(row=3, column=0)
labelNum4.grid(row=4, column=0)
labelNum4.grid(row=4, column=0)
labelAnswer2.grid(row=5, column=2)


entrynum1 = tk.Entry(root, textvariable=x1)
entrynum1. grid(row=1, column=2)
entrynum2 = tk.Entry(root, textvariable=y1)
entrynum2. grid(row=2, column=2)
entrynum3 = tk.Entry(root, textvariable=x2)
entrynum3. grid(row=3, column=2)
entrynum4 = tk.Entry(root, textvariable=y2)
entrynum4. grid(row=4, column=2)


buttondo = tk.Button(root, text="Calculate", command=clicked2)
buttondo.grid(row=5, column=0)



root.mainloop()

intro.mainloop()

MyWindow.mainloop()

