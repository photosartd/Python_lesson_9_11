import pygame
import random

class Circle:
    #инициализация (первоначальное создание объекта круга)
    def __init__(self, color, radius, center):
        self.color = color
        self.radius = radius
        self.x, self.y = center[0], center[1]
        self.is_jumping = False
        self.jump_count = 10
        self.diff_x = 0
        self.diff_y = 0
        while self.diff_x == 0 or self.diff_y == 0:
            self.diff_x = random.randint(-5,5)
            self.diff_y = random.randint(-5,5)
    #метод отрисовки: принимает в себя объект "окна (surface)"
    def draw(self, surface1):
        pygame.draw.circle(surface=surface1, color=self.color, center=(self.x, self.y), radius=self.radius)
    
    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        #Если не в состоянии прыжка, то последующий код должен выполняться
        #Если в состоянии прыжка, то следующик код просто не выполняется
        if self.is_jumping:
            return
        if keys[pygame.K_LEFT]:
            self.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.x += 3
        elif keys[pygame.K_UP]:
            self.y -= 3
        elif keys[pygame.K_DOWN]:
            self.y += 3

    def jump(self, keys):
        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
        #Если в состоянии прыжка, то меняй координату y
        if self.is_jumping:
            #Пока между 10 и 0 - симулируем прыжок вверх
            if self.jump_count > 0:
                self.y -= 10
                self.jump_count -= 1
            #симулирем приземление
            # self.jump_count in range(-10, 1)
            elif self.jump_count > -10 and self.jump_count <= 0:
                self.y += 10
                self.jump_count -= 1
            #при приземлении должны сказать, что уже не прыгаем и снова можем прыгать
            else:
                self.is_jumping = False
                self.jump_count = 10

    def __collision(self, brick):
        top_border =  (self.y + self.radius >= brick.top) \
            and (self.y + self.radius <= brick.bottom)
        bottom_border = (self.y - self.radius <= brick.bottom) \
            and (self.y - self.radius >= brick.top)
        left_right_border = brick.left <= self.x <= brick.right

        if (top_border or bottom_border) and left_right_border:
            self.diff_y = -self.diff_y
            if isinstance(brick, Brick):
                return True
        
        return False

    def random_movement(self, width, brick, wall):
        for brick1 in wall.bricks:
            destroy = self.__collision(brick1)
            if destroy:
                #вызов метода разрушения кирпича из стены
                wall.destroy(brick)
        self.__collision(brick)
        #изменяются координаты на diff_x diff_y
        self.x += self.diff_x
        self.y += self.diff_y
        #реализовать логику соударения с окном
        if self.x + self.radius >= width or self.x - self.radius <= 0:
            self.diff_x = -self.diff_x
            #хотим менять цвет
            self.color = random.choices(range(256), k=3)
        if self.y + self.radius >= width or self.y - self.radius <=0:
            self.diff_y = -self.diff_y
            #хотим менять цвет
            self.color = random.choices(range(256), k=3)

    
        