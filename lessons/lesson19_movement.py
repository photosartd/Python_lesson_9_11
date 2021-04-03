import pygame
import math

a = int(input("Enter window size a: "))

pygame.init()
#win - Surface
win = pygame.display.set_mode((a,a))
background_color = (255,255,255)
yellow = (255,255,0)
red = (255,0,0)
circle_color = yellow

center = a/2
x = a/2
y = a/2
diff = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    radius = 25
    #code
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if (x - radius <=0):
            pass
        else:
            x -= 3
    elif keys[pygame.K_RIGHT]:
        if (x + radius >= a):
            pass
        else:
            x += 3
    elif keys[pygame.K_UP]:
        y -= 3
    elif keys[pygame.K_DOWN]:
        y += 3
    else:
        #Для того, чтобы отслеживать, когда кнопки не нажаты
        if x > a/2:
            x -= diff
        elif x < a/2:
            x += diff
        
        if y > a/2:
            y -= diff
        elif y < a/2:
            y += diff

    
    pygame.draw.circle(win, circle_color, (x,y), radius)

    pygame.display.update()
    pygame.time.delay(10)