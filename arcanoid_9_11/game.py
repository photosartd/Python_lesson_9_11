import pygame
from Circle import Circle
from platform import Brick, Platform, Wall
import random

pygame.init()
#win - Surface
win_size = 500
win = pygame.display.set_mode((win_size, win_size))
background_color = (0,0,0)

FPS = 60
clock = pygame.time.Clock()

#функция генерации рандомного цвета
def generate_random_color():
    return random.choices(range(256), k=3)

brick_color = generate_random_color()
platform_color = generate_random_color()

brick = Brick(win, win_size, brick_color, win_size/2, win_size/2, win_size/10)
platform = Platform(win, win_size, platform_color, win_size/2, win_size/2, win_size/8)

#параметры мяча
center = (win_size/2, win_size/2)
radius = 10
color_ball = (255,255,0)
#мяч
ball = Circle(color_ball, radius, center)
#стена
RED = (255,0,0)
wall = Wall(win_size, win, RED)
wall.fill(3, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    #code
    #получение кнопок
    #brick.draw()
    wall.draw()
    ball.random_movement(win_size, platform, wall)
    ball.draw(win)

    platform.move_by_keys()
    platform.draw()

    pygame.display.update()
    clock.tick(FPS)