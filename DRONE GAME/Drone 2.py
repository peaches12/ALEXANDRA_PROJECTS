import pygame, sys
pygame.init()
screen=pygame.display.set_mode([900, 1500])
screen.fill([0, 255, 0])
#all our functions
def just_starting():
    angle = random.random(0, 360)
    
def next_step(x, y):
    if x < 1500 and y < 900: #prevents bullet from going offscreen
        x = x + 2
        y = y + 2
        
#all our lists
letters = [a, b, c, d, e]
positons_x = [100, 430, 1050, 800, 1231]
positons_y = [100, 467, 150, 677, 803]
rand_angle = []
firing = [y, y, y, y, y]
while True: #this loop runs forever
    for k in range(len[letters]):
        if firing[k] == 'y':
            next_step(positons_x[k], positons_y[k])
        elif firing[k] == 'n':
            will_you_go_next()
        elif firing[k] = 'j': #the bullet is just starting
            just_starting():
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
