import turtle, time
from random import randint
wn = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed(0)
turtle.pencolor("black")
turtle.pensize(5)
 
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
listedColors = ['red', 'blue', 'purple', 'yellow', 'blue', 'green', 'orange', 'purple', 'blue'] 
counter = 0
 
#pick colors for the list
colors_used = []
 
for k in range(9):
    ourPick = listedColors[k]
    for pickIt in range(3):
        colors_used.append(ourPick)
 
    
def draw_whole_cube_face(addIt):
    counter = 0 + addIt
    for m in range(3):
        for k in range(3):
                rhombus_color = colors_used[counter]
                turtle.color("black", rhombus_color)
                turtle.begin_fill()
                for x in range(2):
                    turtle.forward(30)
                    turtle.right(120)
                    turtle.forward(30)
                    turtle.right(60)
                turtle.end_fill()
                turtle.forward(30)
                counter = counter + 1
                print(counter)
        turtle.back(30*3)
        turtle.right(120)
        turtle.forward(30)
        turtle.left(120)
   	 
    
def drawing_cube():
	draw_whole_cube_face(0)  #draw 'left' face
	turtle.left(60)     	#repositon turtle for right face
	turtle.forward(30*3)
	turtle.left(60)
	draw_whole_cube_face(9) #draw 'right' face
	turtle.left(60)    	#repositon turtle for top face
	turtle.forward(30*3)
	turtle.left(60)
	draw_whole_cube_face(18) #draw 'top' face
	print(colors_used)

def tilt_da_colors(start, end, increment, fake_conter):
    conter = fake_conter
    for m in range(start, end, increment):
        colors_used[m] = colors_used[conter]
        colors_used[conter] = COLORS[randint(0, 5)]
        conter = conter - 1

 
 
#drawing 2nd phase of cube
turtle.right(90)#untilt the cube
#ORIGNAL CUBE, perfectly striped faces
drawing_cube()


turtle.up()
turtle.goto(150, -150)
turtle.down()
turtle.left(120)

tilt_da_colors(17, 10, -3, 26)

drawing_cube()



turtle.up()
turtle.goto(-150, -150)
turtle.down()
turtle.left(120)

tilt_da_colors(2, 9, 3, 17)

drawing_cube()
 
turtle.up()
turtle.goto(0, -300)
turtle.down()
turtle.left(120)

tilt_da_colors(20, 27, 3, 8)

drawing_cube()
