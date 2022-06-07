import pygame
from management_gameplay_environment import ManagementEnvironment


class ManagementCanvas:
    def __init__(self, root, clock, launched: bool, ROOT_WIDTH: int, ROOT_HEIGHT: int):
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT
        self.HUMAN_WIDTH = 80
        self.HUMAN_HEIGHT = 80
        self.HUMAN_SPEED = 2

        self.management_environment = None
        self.spawn_speed = False
        self.USEREVENT_timer = 0
        self.timer_create_enemy = 1000

        # call every in milliseconds
        pygame.time.set_timer(pygame.USEREVENT, self.timer_create_enemy)

        self.root_gameplay = False
        self.root_menu = True

        self.root = root
        self.clock = clock
        self.launched = launched

        self.root_background_image_gameplay = pygame.image.load("background_game.png")
        self.root_background_image_gameplay = pygame.transform.scale(self.root_background_image_gameplay, (self.ROOT_WIDTH, self.ROOT_HEIGHT))

        self.root_background_image_menu = pygame.image.load("background_menu.png")
        self.root_background_image_menu = pygame.transform.scale(self.root_background_image_menu, (self.ROOT_WIDTH, self.ROOT_HEIGHT))

    def init_the_management_gameplay_environment(self):
        # create all the enemy, player, bullet
        self.management_environment = ManagementEnvironment(self.root, self.HUMAN_WIDTH, self.HUMAN_HEIGHT,
                                                            self.HUMAN_SPEED, self.ROOT_WIDTH, self.ROOT_HEIGHT)

    def call_every_frame(self):
        if self.root_gameplay:
            self.check_event_key_in_gameplay()
            self.management_mouvement()
            # check if player died
            self.management_player_alive_or_not()
            self.draw_background_and_fps()
        elif self.root_menu:
            self.check_event_key_in_menu()
            self.draw_background_and_fps()

    def check_event_key_in_menu(self):
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                self.launched = False
            # for event every 2 sec
            elif event.type == pygame.USEREVENT:
                print("every 2 secondes")
            # to start game
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    print("start")
                    self.root_gameplay = True
                    self.root_menu = False
                    self.init_the_management_gameplay_environment()

    def check_event_key_in_gameplay(self):
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                self.launched = False

            # create enemy with clock timer
            elif event.type == pygame.USEREVENT:
                self.call_every_2_seconds()

            # to can shoot
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_3:
                    self.management_environment.shoot_bullet()

        # player mouvement
        keys_pressed = pygame.key.get_pressed()
        # keys_up = pygame.key.K_UP()
        if keys_pressed:
            self.management_environment.key_pressed(keys_pressed)

    def call_every_2_seconds(self):
        self.USEREVENT_timer += 1
        self.spawn_speed = False
        # if timer is multiply of 5 update new timer
        # if self.USEREVENT_timer % 5 == 0:
        # self.timer_create_enemy -= 300
        # re create timer with an other variable
        # pygame.time.set_timer(pygame.USEREVENT, self.timer_create_enemy)

        self.management_environment.create_enemy_every_2_sec()


    def management_mouvement(self):
        # mouvement enemy
        self.management_environment.enemy_mouvement()
        self.management_environment.bullet_mouvement()

    def management_player_alive_or_not(self):
        if not self.management_environment.check_if_end_game():
            print("player died")
            self.root_gameplay = False
            self.root_menu = True

    def draw_background_and_fps(self):
        if self.root_gameplay:
            # display the background image to the root
            self.root.blit(self.root_background_image_gameplay, [0, 0])

            # draw enemy
            self.management_environment.draw_human_and_fps(self.clock)
        elif self.root_menu:
            self.root.blit(self.root_background_image_menu, [0, 0])
