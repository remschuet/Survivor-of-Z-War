import pygame


class PlayerMenu:
    def __init__(self, root, position_x, position_y, width, height):
        self.root = root
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.object_image = None

        self.player_color = "asset/image/player_yellow_idle.png"
        self.resize_image()

    def set_new_color(self, number: int):
        if number == 1:
            self.player_color = "asset/image/player_yellow_idle.png"
        elif number == 2:
            self.player_color = "asset/image/player_green_idle.png"
        elif number == 3:
            self.player_color = "asset/image/player_purple_idle.png"
        self.resize_image()

    def resize_image(self):
        self.object_image = pygame.image.load(self.player_color)
        self.object_image = pygame.transform.scale(self.object_image, (self.width, self.height))

    def draw(self):
        # draw the rect using the position x, y, width, height
        pygame.draw.rect(self.root, (0, 0, 0), (self.position_x, self.position_y, self.width, self.height), 1)
        # draw the image using the position x, y
        self.root.blit(self.object_image, (self.position_x, self.position_y))
