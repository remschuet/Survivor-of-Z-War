import pygame
from human import Human
from position_player import PositionPlayer


class Player(Human):
    def __init__(self,  root, name, position_x: int, position_y: int, height: int, width: int, speed: int,
                 position_player: PositionPlayer):
        super().__init__(root, name, position_x, position_y, height, width, speed)

        self.position_player = position_player
        self.set_new_position()

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
        self.set_new_position()

    def set_new_position(self):
        self.position_player.set_new_position(self.position_x, self.position_y)

