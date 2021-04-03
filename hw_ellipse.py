import pygame

def draw_ellipses(win, win_size, color, number):
    center = win_size / 2
    width = win_size/n
    height = win_size
    diff = win_size/n
    x = win_size/2 - diff/2
    y = 0
    while width <= win_size:
        pygame.draw.ellipse(win, color, (x, y, width, height), 1)
        width += diff
        x -= diff/2

a = int(input("Enter win square size: "))
n = int(input("Enter ellipse number n: "))

pygame.init()
#win - Surface
win = pygame.display.set_mode((a,a))
background_color = (0,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    rect_color = (255,255,255)
    #code
    draw_ellipses(win, a, rect_color, n)
    pygame.display.update()

