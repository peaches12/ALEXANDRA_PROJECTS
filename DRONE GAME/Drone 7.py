import pygame, sys, math, random
from decimal import *
from random import randint
pygame.init()
screen = pygame.display.set_mode([2000, 2000])
screen.fill([50, 132, 255])


#lists
positons_x = []  
positons_y = []
angles = []
addit = [] 
#constant

def pick_spot_function(our_range, list_append, minimum, maximum):
    for pick_spot in range(our_range):
        list_append.append(randint(minimum, maximum))
pick_spot_function(13, positons_x, 0, 1000) #x-coordinates
pick_spot_function(13, positons_y, 0, 1000) #y-coordinates
pick_spot_function(13, angles, -89, 270)      #angle the 'ball' is going at
for y in range(len(angles)):
    if angles[y] > 90:
        angles[y] = angles[y] - 180
        addit.append(-2)
    else:
        addit.append(2) 

#determining the location of the bullets
while True:
    for loop in range(13):
        x_now = positons_x[loop]
        y_now = positons_y[loop]
        for bouncer in range(13):                                                                          #checking if ball is hitting another ball
            x_comparer = positons_x[bouncer]
            y_comparer = positons_y[bouncer]
            if x_comparer != x_now and y_comparer != y_now:                                                #don't compare against the current ball
                if math.sqrt(x_comparer**2 + x_now**2) > 50 and math.sqrt(y_comparer**2 + y_now**2) > 50:  #if the ball isn't hitting another one
                    pass
                else:
                    angles[loop] = -angles[loop]                                                            #make the ball go in the opposite direction
            else:
                pass
            
        if  0 < x_now < 1000 and 0 < y_now < 1000:
            pygame.draw.rect(screen, [50, 132, 255], [x_now-25, y_now-25, 50, 50], 0)                       #draw a rectangle to cover up the ball
            pygame.display.flip()                                                                           #aka if the ball hasn't hit the screen yet
            pygame.draw.circle(screen, [255, 0, 0], [int(x_now), int(y_now)], 25, 0)
            pygame.display.flip()

        else:
            positons_x[loop] = randint(100, 800)                  
            positons_y[loop] = randint(100, 800)
            angles[loop] = randint(-89, 89)
            pygame.draw.rect(screen, [50, 132, 255], [x_now-25, y_now-25, 50, 50], 0)

        pygame.time.delay(1)
        x_now = positons_x[loop] + int(addit[loop])
        positons_x[loop]=x_now                                                                             #change the x position
        sin_calculator = math.sin(angles[loop]) * int(addit[loop])                                                       #calculate the y change
        y_now = positons_y[loop] + sin_calculator                                                          #change the y positons
        positons_y[loop]=y_now
running = True
while running:                                                                                       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
