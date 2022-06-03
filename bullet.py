import pygame
from position_environment import PositionEnvironment


class Bullet:
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, width: int, height: int, position_environment: PositionEnvironment):
        self.root = root
        self.name_image = name_image
        self.name_id = name_id
        self.position_x = position_x
        self.position_y = position_y
        self.height = height
        self.width = width
        self.position_environment = position_environment

        self.speed = 5

    def set_new_positon(self):
        self.position_environment.set_new_position(self.name_id, self.position_x, self.position_y, self.width,
                                                   self.height)
    def draw(self):
        # draw the rect using the position x, y, width, height
        pygame.draw.rect(self.root, (0, 0, 0), (self.position_x, self.position_y, self.width, self.height), 1)
        # draw the image using the position x, y
        self.root.blit(self.player_image, (self.position_x, self.position_y))
