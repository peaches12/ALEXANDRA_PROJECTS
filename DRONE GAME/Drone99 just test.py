import pygame, sys
pygame.init()
screen=pygame.display.set_mode([1500, 1000])
screen.fill([0, 255, 0]) 
#setup the 'bullet'
center_x = 400
center_y = 700
Center_location = [center_x, center_y]
bullet = pygame.image.load("bullet.png")
bullet = pygame.transform.scale(bullet, (50, 50)) #resize bullet
ANGLE = -135 #rotate bullet
y_increment = 2
RANGE = 200
#here comes the loop
for x in range (3):
    bullet = pygame.transform.rotate(bullet, ANGLE)
    for move_bullet in range(RANGE):
        pygame.time.delay(20)
        center_x = center_x + 2
        center_y = center_y - y_increment
        screen.blit(bullet, [center_x, center_y])
        pygame.display.flip()
        pygame.draw.rect(screen, [0, 255, 0], [center_x, center_y, 90, 90], 0)
    center_x = 400
    center_y = 700
    ANGLE = ANGLE - 5 # change 'bullet-angle'
    y_increment = y_increment + 5 # change 'angle'
    RANGE = RANGE - 50 # decrease range
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
