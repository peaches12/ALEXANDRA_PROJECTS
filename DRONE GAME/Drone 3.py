import pygame, sys, math, random
from decimal import *
from random import randint
pygame.init()
screen = pygame.display.set_mode([2000, 2000])
screen.fill([50, 132, 255])
#our 'sprites'
bullet = pygame.image.load("ball.png")
bullet = pygame.transform.scale(bullet, (50, 50)) #resize bullet

cannon = pygame.image.load("cannontwo.png")
cannon = pygame.transform.scale(cannon, (50, 50))

#changeable
positons_x = []
positons_y = []
#constant

def pick_spot_function(our_range):
    for pick_spot in range(our_range):
        positons_x.append(randint(100, 800))
        positons_y.append(randint(100, 800))
pick_spot_function(13) 
for x in range(13):
    x_coord = positons_x[x]
    y_coord = positons_y[x]
    screen.blit(cannon, [x_coord, y_coord])
angles = [45, -60, 84, -78, 35, -10, 73, 65, -32, 89, 46, -55, 25]
#determining the location of the bullets
while True:
    for loop in range(13):
        pygame.time.delay(2)
        x_now = positons_x[loop] + 2
        positons_x[loop]=x_now
        sin_calculator = math.sin(angles[loop]) * 2
        y_now = positons_y[loop] + sin_calculator
        positons_y[loop]=y_now
        pygame.draw.rect(screen, [50, 132, 255], [x_now, y_now, 50, 50], 0)
        if  0 < x_now < 2000 and 0 < y_now < 2000:
            screen.blit(bullet, [x_now, y_now])
            pygame.display.flip()
        else:
            positons_x[loop] = randint(100, 800)
            positons_y[loop] = randint(100, 800) 
            print("BALL DISAPPEARS")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
