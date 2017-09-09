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

def pick_spot_function(our_range, x_stuff, y_stuff):
    for pick_spot in range(our_range):
        x_stuff.append(randint(25, 1000))
        y_stuff.append(randint(25, 1000))
pick_spot_function(13, positons_x, positons_y)
pick_spot_function(13, angles, angles) 
#angle of firing

#determining the location of the bullets
while True:
    for loop in range(13):
        pygame.time.delay(2)
        x_now = positons_x[loop] + 2
        positons_x[loop]=x_now
        sin_calculator = math.sin(angles[loop]) * 2
        y_now = positons_y[loop] + sin_calculator
        positons_y[loop]=y_now
        pygame.draw.rect(screen, [50, 132, 255], [x_now, y_now, 100, 100], 0)
        if  0 < x_now < 2000 and 0 < y_now < 1000:
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
