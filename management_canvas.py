import pygame
from management_environment import ManagementEnvironment


class ManagementCanvas:
    def __init__(self, root, clock, launched):

        self.ROOT_WIDTH = 900
        self.ROOT_HEIGHT = 600
        self.HUMAN_WIDTH = 80
        self.HUMAN_HEIGHT = 80
        self.HUMAN_SPEED = 2

        self.root = root
        self.clock = clock
        self.launched = launched

        self.root_background_image = pygame.image.load("background_game.png")
        self.root_background_image = pygame.transform.scale(self.root_background_image, (self.ROOT_WIDTH, self.ROOT_HEIGHT))

        self.management_environment = ManagementEnvironment(root, self.HUMAN_WIDTH, self.HUMAN_HEIGHT,
                                                            self.HUMAN_SPEED, self.ROOT_WIDTH, self.ROOT_HEIGHT)

    def get_if_quit(self):
        return self.launched

    def check_event_key(self):
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                self.launched = False
            # for event every 2 sec
            elif event.type == pygame.USEREVENT:
                self.management_environment.create_enemy_every_2_sec()
            # to can shoot
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_3:
                    self.management_environment.shoot_bullet()

        # player mouvement
        keys_pressed = pygame.key.get_pressed()

        # keys_up = pygame.key.K_UP()
        if keys_pressed:
            self.management_environment.key_pressed(keys_pressed)

        # mouvement enemy
        self.management_environment.enemy_mouvement()
        self.management_environment.bullet_mouvement()

        # check if player died
        self.management_environment.check_if_end_game()

        # display the background image to the root
        self.root.blit(self.root_background_image, [0, 0])

        # draw enemy
        self.management_environment.draw_human_and_fps(self.clock)
