from position_environment import PositionEnvironment
from object import Object


class Bullet(Object):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: int, position_environment: PositionEnvironment):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed)

        self.position_environment = position_environment

        self.speed = 3

    def movement(self):
        # check if collision
        # if self.position_environment.check_if_collision(self.name_id, self.position_x, self.position_y, self.width,
        #                                                 self.height):
        #    print("collision")
        # move to the player position x, y
        self.position_x = self.position_x + 10

    def set_new_positon(self):
        self.position_environment.set_new_position(self.name_id, self.position_x, self.position_y,
                                                   self.width, self.height)
