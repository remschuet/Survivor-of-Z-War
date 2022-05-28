import pygame


class ObjectScene:
    def __init__(self, root, position_x: int, position_y: int, height: int, width: int, speed: int):
        self.root = root
        self.position_x = position_x
        self.position_y = position_y
        self.height = height
        self.width = width
        self.speed = speed

        self.draw()

    def move_left(self):
        self.position_x -= self.speed
        self.draw()

    def move_right(self):
        self.position_x += self.speed
        self.draw()

    def move_up(self):
        self.position_y -= self.speed
        self.draw()

    def move_down(self):
        self.position_y += self.speed
        self.draw()

    def draw(self):
        pygame.draw.rect(self.root, (0, 0, 0), (self.position_x, self.position_y, self.width, self.height))
