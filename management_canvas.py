import pygame
from management_gameplay_environment import ManagementEnvironment


class ManagementCanvas:
    def __init__(self, root, clock, launched: bool, ROOT_WIDTH: int, ROOT_HEIGHT: int):
        self.ROOT_WIDTH = ROOT_WIDTH
        self.ROOT_HEIGHT = ROOT_HEIGHT
        self.OBJECT_WIDTH = 80
        self.OBJECT_HEIGHT = 80
        self.OBJECT_SPEED = 2

        self.management_environment = None

        # call every x milliseconds
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        # canvas, init to menu
        self.root_menu = True
        self.root_gameplay = False

        self.root = root
        self.clock = clock
        self.launched = launched

        self.root_background_image_gameplay = pygame.image.load("background_game.png")
        self.root_background_image_gameplay = pygame.transform.scale(self.root_background_image_gameplay,
                                                                     (self.ROOT_WIDTH, self.ROOT_HEIGHT))

        self.root_background_image_menu = pygame.image.load("background_menu.png")
        self.root_background_image_menu = pygame.transform.scale(self.root_background_image_menu,
                                                                 (self.ROOT_WIDTH, self.ROOT_HEIGHT))

    def create_management_environment(self):
        # create all the enemy, player, bullet
        self.management_environment = ManagementEnvironment(self.root, self.OBJECT_WIDTH, self.OBJECT_HEIGHT,
                                                            self.OBJECT_SPEED, self.ROOT_WIDTH, self.ROOT_HEIGHT)

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
            self.check_event_key_in_menu()
        # draw everything
        self.management_draw()

    def check_event_key_in_menu(self):
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                self.launched = False
            # to start game
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    print("start")
                    self.root_gameplay = True
                    self.root_menu = False
                    self.create_management_environment()

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
                    self.management_environment.shoot_bullet()

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
        elif self.root_menu:
            self.root.blit(self.root_background_image_menu, [0, 0])
