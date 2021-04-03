import pygame

a = int(input())
b = int(input())

pygame.init()
win = pygame.display.set_mode((a,b))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    
    win.fill((255,255,255))

    pygame.draw.line(win, (0,0,0), (0,0), (a,b), 5)
    pygame.draw.line(win, (0,0,0), (0,b), (a,0), 5)
    pygame.display.update()
    pygame.time.delay(10)
