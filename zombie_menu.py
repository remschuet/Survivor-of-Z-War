import pygame


class ZombieMenu:
    def __init__(self, root, position_x, position_y, min_x, max_x, width, height):
        self.position_x = position_x
        self.position_y = position_y
        self.min_x = min_x
        self.max_x = max_x
        self.speed = 1
        self.width = width
        self.height = height
        self.root = root

        self.direction = "right"

        self.object_image = pygame.image.load("enemy_zombie_idle.png")
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
