# A simple calculator example
# Based on example found in programminginpython.com
# Modified for instructional purposes

import tkinter as tk
from tkinter import *


large_font =('Comic Sans MS',20,)
small_font = ('Comic Sans MS',12,)
medium_font = ('Comic Sans MS',15,)


intro = tk.Tk()
intro.title("Welcome User!")
intro.geometry('500x225')
intro.configure(bg='lightblue')


def clicked():
    name1 = (firstname.get())
    name2 = (lastname.get())
    result = name1[:3] + name2[:1]
    labelAns.config(text="Your Username is %s" % result + " Welcome! \n please exit this window")
    storedname = [result]
 
 
firstname = tk.StringVar()
lastname = tk.StringVar()


labelTitle = tk.Label(intro, text="Solve for Slope!", font=medium_font, bg = 'lightblue')
labelName1 = tk.Label(intro, text="Enter First-Name", font=medium_font, bg = 'lightblue')
labelName2 = tk.Label(intro, text="Enter Last-Name", font=medium_font, bg = 'lightblue')
labelAns = tk.Label(intro, text="The answer is", font=medium_font, bg = 'lightblue')


labelTitle.grid(row=0, column=2)
labelName1.grid(row=1, column=0)
labelName2.grid(row=2, column=0)
labelAns.grid(row=5, column=2)


entryname1 = tk.Entry(intro, textvariable=firstname, font=medium_font, fg = 'orange',highlightbackground='lightblue')
entryname1. grid(row=1, column=2)
entryname2 = tk.Entry(intro, textvariable=lastname, font=medium_font, fg = 'orange',highlightbackground='lightblue')
entryname2. grid(row=2, column=2)



buttondo = tk.Button(intro, text="Create Name!", command=clicked, font=medium_font)
buttondo.grid(row=5, column=0)

intro.mainloop()


######################
#Slope-Int Form Calculator
#######################

MyWindow = tk.Tk()
MyWindow.title("Welcome")
MyWindow.geometry('750x450')
MyWindow.configure(bg='orange')



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
        labelsteps.config(text=str(a) + "x" + str(b) + "y" + str(c) + "=" + str(0) + "\n" + str(b) + "y" + str(c) + "=" + str(a/-1) + "\n" + str(b) + "y" + "=" + str(a/-1) + "+" + str(c/-1) + "\n" + "y" + "=" + str(-a/b) + "x" + str(-c/b) ) 
        result = "y =" + "-" + str(m) + "x -" + str(z)
        labelAns.config(text="Result is %s" % result)
        explanation.config(text="In this scenario, you must isolate for the \n variable Y. This is done by shifting over the\n variables to the other side. One thing you may have \nnoticed is that the values  ended up being negative.This \nis as it is considered poor practice to leave the \n negative,  which means  the negative  had to be \ndivided out.")

    
    if z > 0 and m < 0 and b < 0:

        result = "y =" + " " + str(int(m) / int(-1)) + "x -" + str(z)
        labelAns.config(text="Result is %s" % result)

    if z < 0 and m < 0 and b < 0:

        result = "y =" + " " + str(int(m) / int(-1)) + "x +" + str(int(z) / int(-1))
        labelAns.config(text="Result is %s" % result)


# Create your variables  
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
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
labelTitle.grid(row=0, column=1)
labelNum1.grid(row=1, column=0)

labelNum2.grid(row=2, column=0)

labelNum3.grid(row=3, column=0)

labelsteps.grid(row=5, column=0)

labelNum5.grid(row=4, column=0)

labelNum6.grid(row=6, column=0)

labelNum7.grid(row=7, column=0)

labelNum8.grid(row=8, column=0)


labelAns.grid(row=9, column=1)

labelNum9.grid(row=9, column=2)

labelNum10.grid(row=9, column=3)

labelNum11.grid(row=9, column=4)

explanation.grid(row=7, column=5)



# Here is where we go to input our numbers
entryNum1 = tk.Entry(MyWindow, textvariable=number1, font = medium_font, borderwidth=5, relief ="raised", bg = 'white', highlightbackground='lightblue', fg = 'orange')
entryNum1. grid(row=1, column=1)
entryNum2 = tk.Entry(MyWindow, textvariable=number2, font = medium_font, borderwidth=5, relief ="raised", bg = 'white', highlightbackground='lightblue', fg = 'orange')
entryNum2. grid(row=2, column=1)
entryNum3 = tk.Entry(MyWindow, textvariable=number3, font = medium_font, borderwidth=5, relief ="raised", bg = 'white', highlightbackground='lightblue', fg = 'orange')
entryNum3. grid(row=3, column=1)


# Here is where we set up the button to perform "call" the calculation
# Calculation is performed when the "clicked" function is called

buttonCal = tk.Button(MyWindow, text="Calculate", font=medium_font,command=clicked, fg = 'orange', highlightbackground = 'lightblue')
buttonCal.grid(row=7, column=0)

def hide():
    labelsteps.config(text="")
    small_font = ('Comic Sans MS',3,)

buttonstep = tk.Button(MyWindow, text="Steps", font=medium_font, command=hide, fg = 'orange', highlightbackground = 'lightblue')
buttonstep.grid(row=5, column=1)


## restart function work in progress
##root=Tk()
##def restart():
## root.mainloop() 

def exit():
    MyWindow.destroy() 


def hide():
    labelsteps.config(text="")

            

restart = tk.Button(MyWindow, text="Quit", command =exit,font=medium_font, fg = 'orange', highlightbackground = 'lightblue')
restart.config(height = 1, width = 10,)
restart.grid(row=1, column=5)


###########################
#Slope Calculator Code
##################



root = Toplevel(MyWindow)
root.title("Welcome")
root.geometry('450x225')
root.configure(bg='black')

#

def clicked():
    num1 = float(x1.get())
    num2 = float(y1.get())
    num3 = float(x2.get())
    num4 = float(y2.get())
    result = (int(num4)-int(num2))/(int(num3)-int(num1))
    labelAns.config(text="Result is %d" % result)
 
 
x1 = tk.StringVar()
y1 = tk.StringVar()
x2 = tk.StringVar()
y2 = tk.StringVar()


labelTitle = tk.Label(root, text="Solve for Slope!")
labelNum1 = tk.Label(root, text="Enter first x value")
labelNum2 = tk.Label(root, text="Enter first y value")
labelNum3 = tk.Label(root, text="Enter second x value")
labelNum4 = tk.Label(root, text="Enter second y value")
labelAns = tk.Label(root, text="The answer is")


labelTitle.grid(row=0, column=2)
labelNum1.grid(row=1, column=0)
labelNum2.grid(row=2, column=0)
labelNum2.grid(row=2, column=0)
labelNum3.grid(row=3, column=0)
labelNum3.grid(row=3, column=0)
labelNum4.grid(row=4, column=0)
labelNum4.grid(row=4, column=0)
labelAns.grid(row=5, column=2)


entrynum1 = tk.Entry(root, textvariable=x1)
entrynum1. grid(row=1, column=2)
entrynum2 = tk.Entry(root, textvariable=y1)
entrynum2. grid(row=2, column=2)
entrynum3 = tk.Entry(root, textvariable=x2)
entrynum3. grid(row=3, column=2)
entrynum4 = tk.Entry(root, textvariable=y2)
entrynum4. grid(row=4, column=2)


buttondo = tk.Button(root, text="Calculate", command=clicked)
buttondo.grid(row=5, column=0)



root.mainloop()



MyWindow.mainloop()

