

# Python Class 1548
# Lesson 9 Problem 6
# Author: peaches1210 (202437)

import turtle

turtle.setup(800,600) # Change the width of the drawing to 800px and the height to 600px.
wn = turtle.Screen()
sammy = turtle.Turtle()

inFile = open('directions_turtle.txt', 'r')
lista = inFile.readlines()
for UPG in lista:
    UPG = UPG.strip()
    if UPG == 'UP':
        sammy.up()
    elif UPG == 'DOWN':
        sammy.down()
    else:
        UPG_list = UPG.split()
        print(UPG_list)
        sammy.goto(float(UPG_list[0]), float(UPG_list[1]))
inFile.close()

                              
        
        
