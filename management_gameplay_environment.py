import random

import pygame
from player import Player
from enemy import Enemy
from position_environment import PositionEnvironment
from bullet import Bullet
from box_ammo import BoxAmmo


class ManagementEnvironment:
    def __init__(self, root, HUMAN_WIDTH, HUMAN_HEIGHT, HUMAN_SPEED, ROOT_WIDTH, ROOT_HEIGHT):
        self.root = root
        self.HUMAN_WIDTH = HUMAN_WIDTH
        self.HUMAN_HEIGHT = HUMAN_HEIGHT
        self.HUMAN_SPEED = HUMAN_SPEED
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT

        # create writing style
        self.arial_font = pygame.font.SysFont("arial", 25)
        self.arial_font_bold = pygame.font.SysFont("arial", 25, True)

        # create a list for the enemy
        self.enemy_list = []
        self.number_of_enemy = 0

        # create a list for the bullet
        self.bullet_list = []
        self.name_of_bullet = 0

        # to manage ammo
        self.box_ammo_list = []
        self.number_of_ammo = 20

        # Set up player
        self.position_environment = PositionEnvironment()
        self.player = Player(root, "player", "player", 400, 250,
                             self.HUMAN_WIDTH, self.HUMAN_HEIGHT, self.HUMAN_SPEED, self.position_environment)

        # set up first ammo_box
        self.box_ammo_list.append(BoxAmmo(root, "ammo", "box_ammo", 500, 300, self.HUMAN_WIDTH, self.HUMAN_HEIGHT,
                                          self.HUMAN_SPEED, self.position_environment))

    def random_position_of_enemy(self):
        list = [(0, 300), (450, 0), (900, 300), (450, 600)]
        x, y = random.choice(list)
        return x, y

    def create_enemy_every_2_sec(self):
        self.number_of_enemy += 1
        # random position
        position_x, position_y = self.random_position_of_enemy()
        # create enemy
        if self.number_of_enemy <= 20:
            self.enemy_list.append(Enemy(self.root, "enemy", ("enemy" + str(self.number_of_enemy)),
                                         position_x, position_y, self.HUMAN_WIDTH, self.HUMAN_HEIGHT,
                                         self.HUMAN_SPEED, self.position_environment))

    def key_pressed(self, keys):
        if keys[pygame.K_LEFT] and self.player.position_x > 0:
            self.player.move_left()
        if keys[pygame.K_RIGHT] and self.player.position_x < self.ROOT_WIDTH - self.HUMAN_WIDTH:
            self.player.move_right()
        if keys[pygame.K_UP] and self.player.position_y > 0:
            self.player.move_up()
        if keys[pygame.K_DOWN] and self.player.position_y < self.ROOT_HEIGHT - self.HUMAN_HEIGHT:
            self.player.move_down()

    def check_if_end_game(self):
        if not self.position_environment.get_player_alive_or_not():
            return False
        else:
            return True

    def shoot_bullet(self):
        self.create_bullet()

    def destroy_enemy_and_bullet(self):
        # take the list with the name of enemy we need to destroy
        list_to_destroy = self.position_environment.get_list_of_enemy_to_destroy()
        # take all the name in enemy list
        for enemy_item in self.enemy_list:
            if isinstance(enemy_item, Enemy):
                # take name in list to destroy
                for item_name_to_destroy in list_to_destroy:
                    if enemy_item.name_id == item_name_to_destroy:
                        # remove item fro the enemy_list
                        self.enemy_list.remove(enemy_item)
                        # destroy the position in position environment dict
                        self.position_environment.destroy_object_in_dict(enemy_item.name_id)

        list_bullet = self.position_environment.get_list_of_bullet_to_destroy()
        for bullet_item in self.bullet_list:
            if isinstance(bullet_item, Bullet):
                for item_name_to_destroy in list_bullet:
                    if bullet_item.name_id == item_name_to_destroy:
                        self.bullet_list.remove(bullet_item)
                        self.position_environment.destroy_object_in_dict(bullet_item.name_id)

        list_box_ammo = self.position_environment.get_box_ammo_to_destroy()
        for box_ammo_item in self.box_ammo_list:
            if isinstance(box_ammo_item, BoxAmmo):
                for item_name_to_destroy in list_box_ammo:
                    if box_ammo_item.name_id == item_name_to_destroy:
                        self.number_of_ammo += 10
                        self.box_ammo_list.remove(box_ammo_item)
                        self.position_environment.destroy_object_in_dict(box_ammo_item.name_id)

    def enemy_mouvement(self):
        for enemy_item in self.enemy_list:
            if isinstance(enemy_item, Enemy):
                enemy_item.movement()

    def bullet_mouvement(self):
        for bullet_item in self.bullet_list:
            if isinstance(bullet_item, Bullet):
                bullet_item.movement()

    def draw_object_and_fps(self, clock):
        # bullet
        for bullet_item in self.bullet_list:
            if isinstance(bullet_item, Bullet):
                bullet_item.draw()
        # enemy
        for enemy_item in self.enemy_list:
            if isinstance(enemy_item, Enemy):
                enemy_item.draw()

        for box_ammo_item in self.box_ammo_list:
            if isinstance(box_ammo_item, BoxAmmo):
                box_ammo_item.draw()

        # check if we need to destroy an enemy
        self.destroy_enemy_and_bullet()

        # # draw ammo
        # self.box_ammo.draw()

        # player
        self.player.draw()
        # display the fsp in the screen
        fps_text = self.arial_font.render(f"{int(clock.get_fps())} fps", True, (0, 0, 0))
        self.root.blit(fps_text, [(self.ROOT_WIDTH - 70), 20])

    def draw_ammo(self):
        # draw ammo left in the screen
        ammo_left = self.arial_font_bold.render(f"{self.number_of_ammo} ammo", True, (255, 0, 0), (182, 182, 182))
        self.root.blit(ammo_left, [20, 20])

    def create_bullet(self):
        self.name_of_bullet += 1
        if self.number_of_ammo >= 1:
            self.number_of_ammo -= 1
            # search position player
            position_x, position_y = self.player.get_position()
            # get direction of the players
            direction = self.player.get_direction()
            # create bullet
            self.bullet_list.append(
                Bullet(self.root, "bullet", ("bullet" + str(self.name_of_bullet)), position_x, position_y,
                       20, 20, self.HUMAN_SPEED, self.position_environment, direction))
            print("create bullet")
        else:
            print("No ammo")

    def check_ammo_collision_player(self):
        for box_ammo_item in self.box_ammo_list:
            if isinstance(box_ammo_item, BoxAmmo):
                box_ammo_item.check_if_player_collision()
