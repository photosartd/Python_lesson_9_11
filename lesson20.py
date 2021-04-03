import pygame
from Circle import Circle
pygame.init()
#win - Surface
a = 500
win = pygame.display.set_mode((a,a))
background_color = (255,255,255)


circle_color = (255,255,0)
circle = Circle((250,250), radius=25, color=circle_color)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill(background_color)
    #code
    keys = pygame.key.get_pressed()
    circle.jump(keys)
    circle.move_by_keys(keys)
    circle.draw(win)
    pygame.display.update()
    pygame.time.delay(10)
