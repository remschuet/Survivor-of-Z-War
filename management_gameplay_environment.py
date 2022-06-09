import random

import pygame
from player import Player
from enemy import Enemy
from position_environment import PositionEnvironment
from bullet import Bullet
from box_ammo import BoxAmmo

from sounds import Sounds


class ManagementEnvironment:
    def __init__(self, root, OBJECT_WIDTH, OBJECT_HEIGHT, OBJECT_SPEED, ROOT_WIDTH, ROOT_HEIGHT, player_color, score_total):
        self.root = root
        self.OBJECT_WIDTH = OBJECT_WIDTH
        self.OBJECT_HEIGHT = OBJECT_HEIGHT
        self.OBJECT_SPEED = OBJECT_SPEED
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT
        self.player_color = str(player_color)

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
        self.number_of_ammo = 15

        # number of box ammo
        self.number_of_box_ammo = 0
        self.number_chance_box_ammo = 7

        # init the score to 0
        self.score_total = score_total

        # player pv
        player_pv = 3
        self.player_image_pv_3 = pygame.image.load("asset/image/player_pv_3.png")
        self.player_image_pv_2 = pygame.image.load("asset/image/player_pv_2.png")
        self.player_image_pv_1 = pygame.image.load("asset/image/player_pv_1.png")

        # set up sound
        self.sound = Sounds()

        # set up environment
        self.position_environment = PositionEnvironment(player_pv)
        # set up player
        self.player = Player(self.root, "player_" + self.player_color, "player", 400, 250,
                             self.OBJECT_WIDTH, self.OBJECT_HEIGHT, self.OBJECT_SPEED, self.position_environment)

    def get_score_total(self):
        return self.score_total

    def random_position_of_enemy(self):
        list = [(0, 300), (450, 0), (900, 300), (450, 600)]
        x, y = random.choice(list)
        return x, y

    def enemy_select_type(self):
        choice = random.randint(1, 3)
        if choice == 1:
            return "zombie"
        elif choice == 2:
            return "squeletton"
        elif choice == 3:
            return "momie"

    def call_every_2_secondes(self):
        self.check_to_create_enemy()
        self.check_to_create_box_ammo()

    def random_position_box_ammo(self):
        x = random.randint(100, (800 - self.OBJECT_WIDTH))
        y = random.randint(100, (500 - self.OBJECT_HEIGHT))
        return x, y

    def check_to_create_box_ammo(self):
        # if not box ammo in screen and if less then 15 box ammo total
        if not self.box_ammo_list and self.number_of_box_ammo <= 20:
            # if less then 3 box ammo
            if self.number_of_ammo <= 3:
                self.create_box_ammo()
            # if less then 15 bullet
            elif self.number_of_ammo <= 15:
                create_box_ammo = random.randint(1, self.number_chance_box_ammo)
                if create_box_ammo == 1:
                    self.create_box_ammo()

    def create_box_ammo(self):
        self.number_of_box_ammo += 1
        x, y = self.random_position_box_ammo()
        self.box_ammo_list.append(
            BoxAmmo(self.root, "ammo", "box_ammo" + str(self.number_of_box_ammo), x, y, self.OBJECT_WIDTH,
                    self.OBJECT_HEIGHT, self.OBJECT_SPEED, self.position_environment))

    def check_to_create_enemy(self):
        # create enemy
        if self.number_of_enemy <= 100:
            if self.number_of_enemy <= 10:
                self.create_enemy()
            elif self.number_of_enemy > 10:
                self.create_enemy()
                self.create_enemy()

    def create_enemy(self):
        self.number_of_enemy += 1
        # random position
        position_x, position_y = self.random_position_of_enemy()
        choice = self.enemy_select_type()
        self.enemy_list.append(Enemy(self.root, "enemy_" + str(choice), ("enemy" + str(self.number_of_enemy)),
                                     position_x, position_y, self.OBJECT_WIDTH, self.OBJECT_HEIGHT,
                                     self.OBJECT_SPEED, self.position_environment))

    def key_pressed(self, keys):
        if keys[pygame.K_LEFT] and self.player.position_x > 0:
            self.player.move_left()
        if keys[pygame.K_RIGHT] and self.player.position_x < self.ROOT_WIDTH - self.OBJECT_WIDTH:
            self.player.move_right()
        if keys[pygame.K_UP] and self.player.position_y > 0:
            self.player.move_up()
        if keys[pygame.K_DOWN] and self.player.position_y < self.ROOT_HEIGHT - self.OBJECT_HEIGHT:
            self.player.move_down()

    def check_if_end_game(self):
        if not self.position_environment.get_bool_player_alive_or_not():
            self.sound.play_game_over_sound()
            return False
        else:
            return True

    def shoot_bullet(self):
        self.create_bullet()

    def check_destroy_object(self):
        # take the list with the name of enemy we need to destroy
        list_to_destroy = self.position_environment.get_list_of_enemy_to_destroy()
        # enemy
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
                        self.sound.play_enemy_died_sound()
                        # update score total
                        self.score_total += 1

        # bullet
        list_bullet = self.position_environment.get_list_of_bullet_to_destroy()
        for bullet_item in self.bullet_list:
            if isinstance(bullet_item, Bullet):
                for item_name_to_destroy in list_bullet:
                    if bullet_item.name_id == item_name_to_destroy:
                        self.bullet_list.remove(bullet_item)
                        self.position_environment.destroy_object_in_dict(bullet_item.name_id)

        # box ammo
        list_box_ammo = self.position_environment.get_box_ammo_to_destroy()
        for box_ammo_item in self.box_ammo_list:
            if isinstance(box_ammo_item, BoxAmmo):
                for item_name_to_destroy in list_box_ammo:
                    if box_ammo_item.name_id == item_name_to_destroy:
                        self.number_of_ammo += 10
                        self.box_ammo_list.clear()
                        self.position_environment.destroy_object_in_dict(box_ammo_item.name_id)
                        self.sound.play_box_ammo_sound()

    def enemy_mouvement(self):
        for enemy_item in self.enemy_list:
            if isinstance(enemy_item, Enemy):
                enemy_item.movement()

    def bullet_mouvement(self):
        for bullet_item in self.bullet_list:
            if isinstance(bullet_item, Bullet):
                bullet_item.movement()

    def draw_object(self):
        # player
        self.player.draw()
        # enemy
        for enemy_item in self.enemy_list:
            if isinstance(enemy_item, Enemy):
                enemy_item.draw()
        # bullet
        for bullet_item in self.bullet_list:
            if isinstance(bullet_item, Bullet):
                bullet_item.draw()
        # box ammo
        for box_ammo_item in self.box_ammo_list:
            if isinstance(box_ammo_item, BoxAmmo):
                box_ammo_item.draw()

    def draw_informations(self, clock):
        # display the fsp in the screen
        fps_text = self.arial_font.render(f"{int(clock.get_fps())} fps", True, (0, 0, 0))
        self.root.blit(fps_text, [(self.ROOT_WIDTH - 70), 20])

        # draw ammo left in the screen
        ammo_left = self.arial_font_bold.render(f"{self.number_of_ammo} bullets", True, (0, 0, 0), (99, 198, 69))
        self.root.blit(ammo_left, [20, 20])

    def draw_score(self):
        self.get_score_total()
        score_total = self.arial_font_bold.render(f"{self.score_total} points", True, (0, 0, 0), (99, 198, 69))
        self.root.blit(score_total, [20, 50])

    def draw_player_pv(self):
        # draw player pv in the screen
        number_of_pv = self.position_environment.get_player_pv()
        if number_of_pv == 3:
            self.player_image_pv_3 = pygame.transform.scale(self.player_image_pv_3, (150, 50))
            self.root.blit(self.player_image_pv_3, (370, 0))
        elif number_of_pv == 2:
            self.player_image_pv_2 = pygame.transform.scale(self.player_image_pv_2, (150, 50))
            self.root.blit(self.player_image_pv_2, (370, 0))
        elif number_of_pv == 1:
            self.player_image_pv_1 = pygame.transform.scale(self.player_image_pv_1, (150, 50))
            self.root.blit(self.player_image_pv_1, (370, 0))

    def create_bullet(self):
        if self.number_of_ammo >= 1:
            self.name_of_bullet += 1
            self.number_of_ammo -= 1
            # search position player
            position_x, position_y = self.player.get_position()
            # get direction of the players
            direction = self.player.get_direction()
            # create bullet
            self.bullet_list.append(Bullet(self.root, "bullet", ("bullet" + str(self.name_of_bullet)), position_x,
                                           position_y, 20, 20, self.OBJECT_SPEED, self.position_environment, direction))
            self.sound.play_bullet_shoot_sound()
        else:
            # sound tell empty gun
            self.sound.play_bullet_empty_sound()

    def check_ammo_collision_player(self):
        for box_ammo_item in self.box_ammo_list:
            if isinstance(box_ammo_item, BoxAmmo):
                box_ammo_item.check_if_player_collision()
