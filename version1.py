# A simple calculator example
# Based on example found in programminginpython.com
# Modified for instructional purposes

import tkinter as tk

#Creates a window of a particular size
MyWindow = tk.Tk()
MyWindow.title("Slope Calculator")
MyWindow.geometry('600x400')


# Helper functions to support button action

# This one is not currently being used
def clicked2():

    radius = float(txt.get())
    area = 3.14 * (radius ** 2)
    info = "The area of the circle is:"
    lbl.configure(text= info)

# This one currently adds two numbers together
def clicked():
    num1 = (number1.get())
    num2 = (number2.get())
    num3 = (number3.get())
    num4 = (number4.get())
    result = (int(num4)-int(num2))/(int(num3)-int(num1))
    labelAns.config(text="Result is %d" % result)
 
# Create your variables  
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()

# Creating all of the labels with text information
labelTitle = tk.Label(MyWindow, text="Solve for Slope!")
labelNum1 = tk.Label(MyWindow, text="Enter first x value")
labelNum2 = tk.Label(MyWindow, text="Enter first y value")
labelNum3 = tk.Label(MyWindow, text="Enter second x value")
labelNum4 = tk.Label(MyWindow, text="Enter second y value")
labelAns = tk.Label(MyWindow, text="The answer is")

# Arranging all of the labels in a "grid" where row "0", column "0" 
# represents the upper left hand corner
labelTitle.grid(row=0, column=2)
labelNum1.grid(row=1, column=0)
labelNum2.grid(row=2, column=0)
labelNum2.grid(row=2, column=0)
labelNum3.grid(row=3, column=0)
labelNum3.grid(row=3, column=0)
labelNum4.grid(row=4, column=0)
labelNum4.grid(row=4, column=0)
labelAns.grid(row=5, column=2)

# Here is where we go to input our numbers
entryNum1 = tk.Entry(MyWindow, textvariable=number1)
entryNum1. grid(row=1, column=2)
entryNum2 = tk.Entry(MyWindow, textvariable=number2)
entryNum2. grid(row=2, column=2)
entryNum3 = tk.Entry(MyWindow, textvariable=number3)
entryNum3. grid(row=3, column=2)
entryNum4 = tk.Entry(MyWindow, textvariable=number4)
entryNum4. grid(row=4, column=2)

# Here is where we set up the button to perform "call" the calculation
# Calculation is performed when the "clicked" function is called
buttonCal = tk.Button(MyWindow, text="Calculate", command=clicked)
buttonCal.grid(row=5, column=0)

# Main Loop
MyWindow.mainloop()
