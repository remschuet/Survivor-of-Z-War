import pygame


class ZombieMenu:
    def __init__(self, root, position_x: int, position_y: int, min_x: int, max_x: int, width: int, height: int):
        self.root = root
        self.position_x = position_x
        self.position_y = position_y
        self.min_x = min_x
        self.max_x = max_x
        self.width = width
        self.height = height

        # speed mouvement
        self.speed = 1

        # first direction to right
        self.direction = "right"

        # image
        self.object_image = pygame.image.load("asset/image/enemy_zombie_idle.png")
        self.object_image = pygame.transform.scale(self.object_image, (self.width, self.height))

    def mouvement(self):
        if self.direction == "right":
            if self.position_x <= self.max_x:
                self.move_right()
            else:
                self.direction = "left"
        elif self.direction == "left":
            if self.position_x >= self.min_x:
                self.move_left()
            else:
                self.direction = "right"

    def move_right(self):
        self.position_x += self.speed

    def move_left(self):
        self.position_x -= self.speed

    def draw(self):
        # draw the rect using the position x, y, width, height
        pygame.draw.rect(self.root, (0, 0, 0), (self.position_x, self.position_y, self.width, self.height), 1)
        # draw the image using the position x, y
        self.root.blit(self.object_image, (self.position_x, self.position_y))
