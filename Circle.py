import pygame
class Circle:
    def __init__(self, center, radius, color):
        self.center = center
        self.x, self.y = center[0], center[1]
        self.radius = radius
        self.color = color
        self.is_jumping = False
        self.jump_count = 10
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    def move_by_keys(self, keys):
        if not self.is_jumping:
            if keys[pygame.K_LEFT]:
                self.x -= 3
            elif keys[pygame.K_RIGHT]:
                self.x += 3
            elif keys[pygame.K_UP]:
                self.y -= 3
            elif keys[pygame.K_DOWN]:
                self.y += 3
    def jump(self, keys):
        if keys[pygame.K_SPACE]:
            if not self.is_jumping:
                self.is_jumping = True
        if self.is_jumping:
            if self.jump_count >= -10:
                self.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jumping = False