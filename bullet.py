from position_environment import PositionEnvironment
from object import Object


class Bullet(Object):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: int, position_environment: PositionEnvironment, direction):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed)

        self.position_environment = position_environment

        self.speed = 3
        self.direction = direction

    def movement(self):
        # move from the player position x, y
        if self.direction == "left":
            self.position_x = self.position_x - 10

        if self.direction == "right":
            self.position_x = self.position_x + 10

        if self.direction == "up":
            self.position_y = self.position_y - 10

        if self.direction == "down":
            self.position_y = self.position_y + 10

        # set the new position
        self.set_new_positon()

    def set_new_positon(self):
        self.position_environment.set_new_position_in_dict(self.name_id, self.position_x, self.position_y,
                                                           self.width, self.height)
