import pygame, sys, math, random

from random import randint
pygame.init()
screen = pygame.display.set_mode([2000, 2000])
screen.fill([50, 132, 255])

x_coord = 400
y_coord = 400

cardinalDirections = []
cardinalDistances = []

#open the directions file & put all lines in a list
with open("C:\Python36-32\Alexandra Projects/directions.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]  #content is a list of the lines
print(content)

#separating distances & directions

for splitIt in range(0, len(content), 2):
    cardinalDirections.append(content[splitIt])
    cardinalDistances.append(content[splitIt + 1])
print(cardinalDirections)
print(cardinalDistances)
    



for travelChunks in range(len(cardinalDirections)):
    Direction = cardinalDirections[travelChunks]
    Distance = cardinalDistances[travelChunks]
    #change x and/or y depending on direction
    if Direction == 'd':
        Yincrement = 2
        Xincrement = 0
    if Direction == 'r':
        Yincrement = 0
        Xincrement = 2
    if Direction == 'u':
        Yincrement = -2
        Xincrement = 0
    if Direction == 'l':
        Yincrement = 0
        Xincrement = -2
    SmallDistance = 2
    if Direction == 'nw':
        Yincrement = -1
        Xincrement = -1
        SmallDistance = math.sqrt(1**2 + 1**2) 
    if Direction == 'ne':
        Yincrement = -1
        Xincrement = 1
        SmallDistance = math.sqrt(1**2 + 1**2) 
    if Direction == 'sw':
        Yincrement = 1
        Xincrement = -1
        SmallDistance = math.sqrt(1**2 + 1**2) 
    if Direction == 'se':
        Yincrement = 1
        Xincrement = 1
        SmallDistance = math.sqrt(1**2 + 1**2) 

    #how many times do we move the ball?
    moveBallTimes = int(Distance)/(SmallDistance)
    for moveIt in range(int(moveBallTimes)):
        #change x & y before 'moving' ball
        x_coord = x_coord + Xincrement
        y_coord = y_coord + Yincrement
        pygame.draw.rect(screen, [50, 132, 255], [x_coord-25, y_coord-25, 50, 50], 0)                       #draw a rectangle to cover up the ball                                                                          #aka if the ball hasn't hit the screen yet
        pygame.draw.circle(screen, [255, 0, 0], [int(x_coord), int(y_coord)], 25, 0)
        pygame.display.flip()
        pygame.time.delay(20)
    

