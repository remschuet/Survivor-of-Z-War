import random
import pygame.mixer


class Sounds:
    """
    https://mixkit.co/free-sound-effects/monster/
    """
    def __init__(self):
        self.sound_bullet_shoot = pygame.mixer.Sound("asset/sounds/gun_sounds.wav")
        self.sound_bullet_empty = pygame.mixer.Sound("asset/sounds/gun_empty.wav")
        self.sound_get_box_ammo = pygame.mixer.Sound("asset/sounds/ammo_sounds.wav")
        self.sound_game_over = pygame.mixer.Sound("asset/sounds/game_over_sounds.wav")
        self.sound_enemy_died_01 = pygame.mixer.Sound("asset/sounds/monster_died_1.wav")
        self.sound_enemy_died_03 = pygame.mixer.Sound("asset/sounds/monster_died_3.wav")
        self.sound_player_hit = pygame.mixer.Sound("asset/sounds/player_hit.wav")
        self.sound_win_game = pygame.mixer.Sound("asset/sounds/win_game.wav")

    def play_win_game(self):
        # stop all sound
        self.sound_game_over.stop()
        self.sound_enemy_died_01.stop()
        self.sound_enemy_died_03.stop()
        # set volume
        self.sound_win_game.set_volume(0.5)
        # play final sound
        self.sound_win_game.play()

    def play_bullet_shoot_sound(self):
        self.sound_bullet_shoot.play()

    def play_bullet_empty_sound(self):
        self.sound_bullet_empty.play()

    def play_box_ammo_sound(self):
        self.sound_get_box_ammo.play()

    def play_game_over_sound(self):
        # stop all sound
        self.sound_enemy_died_01.stop()
        self.sound_enemy_died_03.stop()
        # play sound game over
        self.sound_game_over.play()

    def play_player_hit_sound(self):
        self.sound_player_hit.play()

    def play_enemy_died_sound(self):
        # random between 2 sound
        i = random.randint(1, 2)
        if i == 1:
            self.sound_enemy_died_01.play()
        elif i == 2:
            self.sound_enemy_died_03.play()
