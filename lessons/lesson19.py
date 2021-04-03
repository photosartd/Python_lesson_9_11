import pygame

def ellipses(n, a, win, color):
    difference = a/n
    width = a/n
    height = a
    x = (a - width)/2
    y = 0
    for i in range(n):
        pygame.draw.ellipse(win, color, (x,y, width, height), 1)
        width += difference
        x -= difference/2


a = int(input("Enter window size a: "))
n = int(input("Enter ellipses number n: "))
    
pygame.init()
#win - Surface
win = pygame.display.set_mode((a,a))
background_color = (0,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    ellipse_color = (255,255,255)
    #code
    ellipses(n, a, win, ellipse_color)
    pygame.display.update()