import pygame
from management_gameplay_environment import ManagementEnvironment
from management_menu_environment import ManagementMenuEnvironment


class ManagementCanvas:
    def __init__(self, root, clock, launched: bool, ROOT_WIDTH: int, ROOT_HEIGHT: int):
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT
        self.OBJECT_WIDTH = 80
        self.OBJECT_HEIGHT = 80
        self.OBJECT_SPEED = 2

        self.score_total = 0
        self.best_score = 0

        # for the player color
        self.player_color = "yellow"

        self.management_menu_environment = None
        self.management_environment = None

        # call every x milliseconds
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        # canvas, init to menu
        self.root_menu = True
        self.root_gameplay = False

        self.root = root
        self.clock = clock
        self.launched = launched

        self.root_background_image_gameplay = pygame.image.load("asset/image/background_game.png")
        self.root_background_image_gameplay = pygame.transform.scale(self.root_background_image_gameplay,
                                                                     (self.ROOT_WIDTH, self.ROOT_HEIGHT))

        self.root_background_image_menu = pygame.image.load("asset/image/background_menu.png")
        self.root_background_image_menu = pygame.transform.scale(self.root_background_image_menu,
                                                                 (self.ROOT_WIDTH, self.ROOT_HEIGHT))

    def create_management_menu_environment(self):
        # create zombie in main menu
        self.management_menu_environment = ManagementMenuEnvironment(self.root, self.ROOT_WIDTH, self.ROOT_HEIGHT, self.best_score)

    def create_management_environment(self):
        # score total to 0
        self.score_total = 0
        # create all the enemy, player, bullet
        self.management_environment = ManagementEnvironment(self.root, self.OBJECT_WIDTH, self.OBJECT_HEIGHT,
                                                            self.OBJECT_SPEED, self.ROOT_WIDTH, self.ROOT_HEIGHT,
                                                            self.player_color, self.score_total)

    def call_every_frame(self):
        if self.root_gameplay:
            # check key event
            self.check_event_key_in_gameplay()
            # enemy mouvement
            self.management_environment.enemy_mouvement()
            # bullet mouvement
            self.management_environment.bullet_mouvement()
            # check if player collision with box ammo
            self.management_environment.check_ammo_collision_player()
            # check if need to destroy object
            self.management_environment.check_destroy_object()
            # check if player died
            self.management_player_alive_or_not()
        elif self.root_menu:
            # set up best score
            self.set_new_best_score()
            # move zombie
            self.management_menu_environment.move_zombie()
            # check key event
            self.check_event_key_in_menu()
        # draw everything
        self.management_draw()

    def set_new_best_score(self):
        if self.management_environment is not None:
            self.score_total = self.management_environment.get_score_total()
        if self.score_total >= self.best_score:
            self.best_score = self.score_total
        self.management_menu_environment.set_best_score(self.best_score)

    def check_event_key_in_menu(self):
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                self.launched = False

            elif event.type == pygame.KEYUP:
                # to start game
                if event.key == pygame.K_SPACE:
                    self.root_gameplay = True
                    self.root_menu = False
                    self.create_management_environment()
                # to change color of player
                elif event.key == pygame.K_1:
                    self.management_menu_environment.set_player_color(1)
                    self.player_color = "yellow"
                elif event.key == pygame.K_2:
                    self.management_menu_environment.set_player_color(2)
                    self.player_color = "green"
                elif event.key == pygame.K_3:
                    self.management_menu_environment.set_player_color(3)
                    self.player_color = "purple"
                elif event.key == pygame.K_4:
                    self.management_menu_environment.set_player_color(4)
                    self.player_color = "blue"

    def check_event_key_in_gameplay(self):
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                self.launched = False
            # create enemy with clock timer
            elif event.type == pygame.USEREVENT:
                self.management_environment.call_every_2_secondes()
                # self.management_environment.create_enemy_every_2_sec()
            # to can shoot
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_3:
                    self.management_environment.call_create_bullet()

        # player mouvement
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed:
            self.management_environment.key_pressed(keys_pressed)

    def management_player_alive_or_not(self):
        if not self.management_environment.check_if_end_game():
            print("player died")
            self.root_gameplay = False
            self.root_menu = True

    def management_draw(self):
        if self.root_gameplay:
            # draw background
            self.root.blit(self.root_background_image_gameplay, [0, 0])
            # draw abject (player enemy bullet)
            self.management_environment.draw_object()
            # draw information (fps ammo)
            self.management_environment.draw_informations(self.clock)
            # draw player pv
            self.management_environment.draw_player_pv()
            # draw score
            self.management_environment.draw_score()
        elif self.root_menu:
            self.root.blit(self.root_background_image_menu, [0, 0])
            self.management_menu_environment.draw_zombie_and_player_menu()
            self.management_menu_environment.draw_best_score()
