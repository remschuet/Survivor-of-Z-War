import pygame


class Human:
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int, speed: int):
        self.root = root
        self.name_image = name_image
        self.name_id = name_id
        self.position_x = position_x
        self.position_y = position_y
        self.height = height
        self.width = width
        self.speed = speed

        prefix = str.lower(self.name_image)

        self.player_image = pygame.image.load(prefix+"_yellow_idle.png")
        self.player_image = pygame.transform.scale(self.player_image, (self.width, self.height))

        self.draw()

    def draw(self):
        pygame.draw.rect(self.root, (0, 0, 0), (self.position_x, self.position_y, self.width, self.height), 1)
        self.root.blit(self.player_image, (self.position_x, self.position_y))
