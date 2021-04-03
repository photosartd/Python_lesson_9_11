import pygame

pygame.init()
#win - Surface
win = pygame.display.set_mode((500,500))
background_color = (255,255,255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    rect_color = (0,255,255)
    circle_color = (255,255,0)
    pygame.draw.rect(win, rect_color, (250,0,250,250))
    pygame.draw.circle(win, circle_color, (125,125), 125)
    pygame.draw.line(win, (0,0,0), (250,250), (500,500), 5)
    pygame.display.update()