#this program draws a colorful 3-d brick wall
import turtle, time
wn = turtle.Screen()

pen = turtle.Turtle()

pen.speed(0)


def draw_rhombus(side, color):
    '''draws a rhombus with 60-120-60-120 angles
    draws the acute angle first, moves counterclockwise
    side: side length
    color: fill color'''
    
    #start filling
    pen.pensize(5)
    pen.pencolor("black")
    pen.fillcolor(color)        #this color is for the fill
    pen.begin_fill()
    for x in range(2):
        pen.forward(side)
        pen.right(120)
        pen.forward(side)
        pen.right(60)
    pen.end_fill()
    #end filling


side_lengh = int(100)
x_coord = 300
y_coord = -250
increment = 90

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
def making_cube_thing(le_couleur): 
    '''draws a cube consisting of 3 rhombuses'''
    pen.left(30)                        #pen starts facing right 
    draw_rhombus(side_lengh, le_couleur)    #right rhombus face
    pen.left(120)
    draw_rhombus(side_lengh, "grey")    #top rhombus face
    pen.left(120)
    draw_rhombus(side_lengh, le_couleur)    #left rhombus face



#we draw 3 stacked cubes

for towers in range(len(color_list)):
    pen.up()
    pen.goto(x_coord, y_coord)
    pen.down()
    our_color = color_list[towers]
    for k in range(6):
        making_cube_thing(our_color)
        pen.right(180)
        pen.up()
        pen.forward(side_lengh)
        pen.right(90)
        pen.down()
    x_coord = x_coord - increment
    y_coord = y_coord - 50
wn.mainloop()

#copyright the real peaches1210 *wink wink*    
