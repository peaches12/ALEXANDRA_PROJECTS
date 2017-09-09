import turtle
from random import randint
wn = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed(0)
turtle.pencolor("black")
turtle.pensize(5)

COLORS = ['red', 'purple', 'blue', 'green', 'yellow', 'darkblue']

def draw_tiny_rhombus(side_lengh):
    rhombus_color = COLORS[randint(0, 5)]
    turtle.color("black", rhombus_color) 
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(side_lengh)
        turtle.right(120)
        turtle.forward(side_lengh)
        turtle.right(60)
    turtle.end_fill()
def draw_whole_cube_face():
    for m in range(3):
        for k in range(3):
            draw_tiny_rhombus(30)
            turtle.forward(30)
        turtle.back(30*3)
        turtle.right(120)
        turtle.forward(30)
        turtle.left(120)
    

turtle.left(60)         #turtle the turtle
draw_whole_cube_face()  #draw 'right' face
turtle.left(60)         #repositon turtle for top face
turtle.forward(30*3)
turtle.left(60)
draw_whole_cube_face() #draw 'top' face
turtle.left(60)        #repositon turtle for left face
turtle.forward(30*3)
turtle.left(60)
draw_whole_cube_face() #draw 'left' face
