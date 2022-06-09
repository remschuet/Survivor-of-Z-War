import pygame
from zombie_menu import ZombieMenu
from player_menu import PlayerMenu


class ManagementMenuEnvironment:
    def __init__(self, root, ROOT_WIDTH, ROOT_HEIGHT):
        self.root = root
        self.ZOMBIE_WIDTH = 100
        self.ZOMBIE_HEIGHT = 100
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT

        self.player_menu = PlayerMenu(self.root, 50, 85, self.ZOMBIE_WIDTH, self.ZOMBIE_HEIGHT)
        self.zombie_1 = ZombieMenu(self.root, 50, 385, 0, 270, self.ZOMBIE_WIDTH, self.ZOMBIE_HEIGHT)
        self.zombie_2 = ZombieMenu(self.root, 630, 323, 630, 800, self.ZOMBIE_WIDTH, self.ZOMBIE_HEIGHT)

    def set_player_color(self, number: int):
        self.player_menu.set_new_color(number)

    def draw_zombie_menu(self):
        self.zombie_1.draw()
        self.zombie_2.draw()
        self.player_menu.draw()

    def move_zombie(self):
        self.zombie_1.mouvement()
        self.zombie_2.mouvement()