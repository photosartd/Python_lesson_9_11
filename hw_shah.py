import pygame

def shah(a, n, win, rect_color):
    #Координаты
    x = 0
    y = 0
    #Вычисление размера клетки
    size = a/n
    for i in range(n):
        while (x + size) <= a:
            pygame.draw.rect(win, rect_color, (x,y,size,size))
            x += 2*size
        if i % 2 == 0:
            x = size
        else:
            x = 0
        y += size

while True:
    a = int(input("Enter window size a: "))
    n = int(input("Enter rows number n: "))
    
    if a % n != 0:
        print('a should be divided by n without the rest!')
        continue
    else:
        break

pygame.init()
#win - Surface
win = pygame.display.set_mode((a,a))
background_color = (255,255,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    rect_color = (0,0,0)
    #code
    shah(a, n, win, rect_color)
    pygame.display.update()

