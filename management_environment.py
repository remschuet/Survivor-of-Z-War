import pygame
from player import Player
from enemy import Enemy
from position_environment import PositionEnvironment


class ManagementEnvironment:
    def __init__(self, root, HUMAN_WIDTH, HUMAN_HEIGHT, HUMAN_SPEED, ROOT_WIDTH, ROOT_HEIGHT):
        self.root = root
        self.HUMAN_WIDTH = HUMAN_WIDTH
        self.HUMAN_HEIGHT = HUMAN_HEIGHT
        self.HUMAN_SPEED = HUMAN_SPEED
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT

        # create writing style
        self.arial_font = pygame.font.SysFont("arial", 20)

        # create a list for the enemy
        self.enemy_list = []
        self.number_of_enemy = 0

        # Set up player
        self.position_environment = PositionEnvironment()
        self.player = Player(root, "player", "player", 400, 250,
                             self.HUMAN_WIDTH, self.HUMAN_HEIGHT, self.HUMAN_SPEED, self.position_environment)

    def call_every_2_sec(self):
        self.number_of_enemy += 1
        # create just 2 enemy
        if self.number_of_enemy <= 2:
            self.enemy_list.append(Enemy(self.root, "enemy", ("enemy" + str(self.number_of_enemy)), 50, 400, self.HUMAN_WIDTH,
                                         self.HUMAN_HEIGHT, self.HUMAN_SPEED, self.position_environment))

    def key_pressed(self, keys):
        if keys[pygame.K_LEFT] and self.player.position_x > 0:
            self.player.move_left()
        if keys[pygame.K_RIGHT] and self.player.position_x < self.ROOT_WIDTH - self.HUMAN_WIDTH:
            self.player.move_right()
        if keys[pygame.K_UP] and self.player.position_y > 0:
            self.player.move_up()
        if keys[pygame.K_DOWN] and self.player.position_y < self.ROOT_HEIGHT - self.HUMAN_HEIGHT:
            self.player.move_down()
        if keys[pygame.K_1]:
            self.destroy_enemy()

    def destroy_enemy(self):
        # to can destroy an enemy
        for enemy_item in self.enemy_list:
            if isinstance(enemy_item, Enemy):
                if enemy_item.name_id == "enemy1":
                    self.enemy_list.remove(enemy_item)
                    # destroy the position in position environment dict
                    self.position_environment.destroy_enemy_in_dict(enemy_item.name_id)

    def enemy_mouvement(self):
        for enemy_item in self.enemy_list:
            if isinstance(enemy_item, Enemy):
                enemy_item.movement()
            else:
                print("Nothing")

    def draw_human_and_fps(self, clock):
        # enemy
        for enemy_item in self.enemy_list:
            if isinstance(enemy_item, Enemy):
                enemy_item.draw()
        # player
        self.player.draw()
        # display the fsp in the screen
        fps_text = self.arial_font.render(f"{int(clock.get_fps())} fps", True, (0, 0, 0))
        self.root.blit(fps_text, [(self.ROOT_WIDTH - 70), 20])
