import pygame
from Circle import Circle
import random

pygame.init()
#win - Surface
win_size = 500
win = pygame.display.set_mode((win_size, win_size))
background_color = (255,255,255)
center = (win_size/2, win_size/2)
radius = 25
circle_color = (255,255,0)

def generate_random_circles(number, radius, width):
    #нужно создать список наших кругов
    circles = []
    for i in range(number):
        center = random.choices(range(radius, width-radius), k=2)
        color = random.choices(range(256), k=3)
        circle = Circle(color, radius, center)
        circles.append(circle)
    return circles

FPS = 60
clock = pygame.time.Clock()

circle = Circle(center=center, radius=radius, color=circle_color)

#создание списка из 10 окружностей
circles_number = 20
circles = generate_random_circles(circles_number, radius, win_size)

current_circles_number = 0
timer = 0
TIME_TO_ADD = 3000

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    #code
    #получение кнопок
    #keys = pygame.key.get_pressed()
    #circle.jump(keys)
    #circle.move_by_keys(keys)
    if timer > TIME_TO_ADD:
        current_circles_number += 1
        if current_circles_number > circles_number:
            current_circles_number = 0
        timer = 0
    for i in range(current_circles_number):
        circles[i].random_movement(win_size)
        circles[i].draw(win)

    pygame.display.update()
    timer += clock.tick(FPS)