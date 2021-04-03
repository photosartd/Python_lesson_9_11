import pygame

#Считать с клавиатуры 2 цифры через пробел
dimensions = input().split(" ")
width = int(dimensions[0])
height = int(dimensions[1])

def draw_lines(width, height, surface):
    pygame.draw.line(surface, (0,0,0), (0,0), (width, height), 5)
    pygame.draw.line(surface, (0,0,0), (0,height), (width, 0), 5)

pygame.init()
win = pygame.display.set_mode((width,height))
background_color = (255,255,255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill(background_color)
    draw_lines(width, height, win)
    pygame.display.update()
