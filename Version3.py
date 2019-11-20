# A simple calculator example
# Based on example found in programminginpython.com
# Modified for instructional purposes

import tkinter as tk

#Creates a window of a particular size
MyWindow = tk.Tk()
MyWindow.title("Slope Calculator")
MyWindow.geometry('600x400')
   # changing size of entry boxes
small_font = ('Verdana',10)








    # changing size of entry boxes


# This one currently adds two numbers together

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

    else: 

        result = "haha, no letters please nooblet"





 
# Create your variables  
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()

# Creating all of the labels with text information
labelTitle = tk.Label(MyWindow, text="Standard Form & Slope-Int Form")
labelNum1 = tk.Label(MyWindow, text="Enter the a value")
labelNum2 = tk.Label(MyWindow, text="Enter the b value")
labelNum3 = tk.Label(MyWindow, text="Enter the c value")
labelAns = tk.Label(MyWindow, text="The answer is")

# Arranging all of the labels in a "grid" where row "0", column "0" 
# represents the upper left hand corner
labelTitle.grid(row=0, column=2)
labelNum1.grid(row=1, column=0)
labelNum2.grid(row=2, column=0)
labelNum2.grid(row=2, column=0)
labelNum3.grid(row=3, column=0)
labelNum3.grid(row=3, column=0)
labelAns.grid(row=5, column=2)

# Here is where we go to input our numbers
entryNum1 = tk.Entry(MyWindow, textvariable=number1, font = small_font)
entryNum1. grid(row=1, column=2)
entryNum2 = tk.Entry(MyWindow, textvariable=number2, font = small_font)
entryNum2. grid(row=2, column=2)
entryNum3 = tk.Entry(MyWindow, textvariable=number3, font = small_font)
entryNum3. grid(row=3, column=2)


# Here is where we set up the button to perform "call" the calculation
# Calculation is performed when the "clicked" function is called
buttonCal = tk.Button(MyWindow, text="Calculate", command=clicked)
buttonCal.grid(row=5, column=0)

# Main Loop
MyWindow.mainloop()
