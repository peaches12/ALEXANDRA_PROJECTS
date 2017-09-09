#moving circle across a screen
import pygame, sys
from random import randint
pygame.init()
screen=pygame.display.set_mode([1500, 1000])
screen.fill([30, 100, 50])
#ALL THE LISTS
x_coordinates = []
y_coordinates = []
size_list = []
color = []
random_color = ['255, 0, 0', '0, 255, 0', '0, 0, 255'] 
for setup in range(20):
    choose_y = randint(0, 500)
    choose_x = 20
    x_coordinates.append(choose_x)
    y_coordinates.append(choose_y)
    size_list.append(randint(5, 50))
    redgreenblue = random_color[randint(0, 2)]
    color.append(redgreenblue)
while True:
    for loop in range(len(x_coordinates)):
        x_now = x_coordinates[loop]
        y_now = y_coordinates[loop]
        size = size_list[loop]
        current_color = color[loop]
        if x_now < 1000:
            pygame.draw.rect(screen, [30, 100, 50], [x_now-size/2, y_now-size/2, size, size], 0)
            x_now = x_now + 1
            print(current_color)
            if current_color == '255, 0, 0': 
                pygame.draw.circle(screen, [255, 0, 0], [x_now, y_now], int(size/2), 0)
            if current_color == '0, 255, 0':
                pygame.draw.circle(screen, [0, 255, 0], [x_now, y_now], int(size/2), 0)
            if current_color == '0, 0, 255':
                pygame.draw.circle(screen, [0, 0, 255], [x_now, y_now], int(size/2), 0)
        else:
            pygame.draw.rect(screen, [30, 100, 50], [x_now-size/2, y_now-size/2, size, size], 0)
            x_coordinates[loop] = 20
            y_coordinates[loop] = randint(3, 25)
            redgreenblue = randint(0, 2)
            color[loop] = random_color(randint(0,2))
            size_list[loop] = randint(5, 50)
        pygame.display.flip()
        pygame.time.delay(1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
            
