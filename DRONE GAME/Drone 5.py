import pygame, sys, math, random
from decimal import *
from random import randint
pygame.init()
screen = pygame.display.set_mode([2000, 2000])
screen.fill([50, 132, 255])
#our 'sprites'
bullet = pygame.image.load("ball.png")
bullet = pygame.transform.scale(bullet, (100, 100)) #resize bullet


#changeable
positons_x = []
positons_y = []
angles = []
#constant

def pick_spot_function(our_range, list_append, minimum, maximum):
    for pick_spot in range(our_range):
        list_append.append(randint(minimum, maximum))
pick_spot_function(13, positons_x, 25, 1000) #x-coordinates
pick_spot_function(13, positons_y, 25, 1000) #y-coordinates
pick_spot_function(13, angles, -89, 89)      #angle the ball is going at


#determining the location of the bullets
while True:
    for loop in range(13):
        pygame.time.delay(2)
        x_now = positons_x[loop] + 2
        positons_x[loop]=x_now
        sin_calculator = math.sin(angles[loop]) * 2
        y_now = positons_y[loop] + sin_calculator
        positons_y[loop]=y_now
        for bouncer in range(13):                                                   #checking if ball is hitting another ball
            x_comparer = positons_x[bouncer]
            y_comparer = positons_y[bouncer]
            if x_comparer != x_now and y_comparer != y_now:                         #don't compare against the current ball
                if abs(x_comparer - x_now) > 100 and abs(y_comparer - y_now) > 100: #if the ball isn't hitting another one
                    pass
                else:
                    angles[loop] = -angles[loop]                                    #make the ball go in the opposite direction
            else:
                pass
        pygame.draw.rect(screen, [50, 132, 255], [x_now, y_now, 100, 100], 0)
        if  0 < x_now < 2000 and 0 < y_now < 1000: #aka if the ball hasn't hit the screen yet
            screen.blit(bullet, [x_now, y_now])
            pygame.display.flip()
        else:
            positons_x[loop] = randint(100, 800)
            positons_y[loop] = randint(100, 800)
            angles[loop] = randint(-89, 89)
            print(str(positons_x[loop]) + ' ' + str(positons_y[loop]))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
