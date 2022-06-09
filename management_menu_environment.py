import pygame
from zombie_menu import ZombieMenu
from player_menu import PlayerMenu


class ManagementMenuEnvironment:
    def __init__(self, root, ROOT_WIDTH: int, ROOT_HEIGHT: int, best_score: int):
        self.root = root
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT
        self.best_score = best_score

        # create size of zombie
        self.ZOMBIE_WIDTH = 100
        self.ZOMBIE_HEIGHT = 100

        # writing style
        self.arial_font_bold = pygame.font.SysFont("Agency FB", 40, True)

        # create player and zombie
        self.player_menu = PlayerMenu(self.root, 50, 85, self.ZOMBIE_WIDTH, self.ZOMBIE_HEIGHT)
        self.zombie_1 = ZombieMenu(self.root, 50, 385, 0, 270, self.ZOMBIE_WIDTH, self.ZOMBIE_HEIGHT)
        self.zombie_2 = ZombieMenu(self.root, 630, 323, 630, 800, self.ZOMBIE_WIDTH, self.ZOMBIE_HEIGHT)

    def set_best_score(self, best_score: int):
        self.best_score = best_score

    def set_player_color(self, number: int):
        self.player_menu.set_new_color(number)

    def draw_zombie_and_player_menu(self):
        self.zombie_1.draw()
        self.zombie_2.draw()
        self.player_menu.draw()

    def draw_best_score(self):
        ammo_left = self.arial_font_bold.render(f"Best Score: {self.best_score}", True, (255, 0, 0))
        self.root.blit(ammo_left, [30, 530])

    def move_zombie(self):
        self.zombie_1.mouvement()
        self.zombie_2.mouvement()
