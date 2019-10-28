# Here is a program to show how to use "if - elif - else"
# when they are "nested" of "one inside of the other"
#
#   > means "greater than..."
#   >= means "greater than or equal to..."
#   < means "less than..."
#   <= means "less than or equal to..."
#
# You can use "and" to join conditions together
# Author: Mr. Jugoon
# Upper Canada College
#
# Put down some options for the user to choose from...

print("1. x")
print(" ")
print("Choose one of the options above")

mood = int(input("Which value would you like to enter first? \n"))



if mood == 1:
      print("Keep having a good day!")
else:
      print ("That's not a valid option!")


# This is a way to gracefully exit the program
input("Press ENTER to quit the program")
