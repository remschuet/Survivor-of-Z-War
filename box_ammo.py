from object import Object
from position_environment import PositionEnvironment


class BoxAmmo(Object):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: int, position_environment: PositionEnvironment):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed)

        self.position_environment = position_environment

        print(self.name_id)

        self.set_new_position()

    def set_new_position(self):
        self.position_environment.set_new_position_in_dict(self.name_id, self.position_x, self.position_y, self.width, self.height)

    def check_if_player_collision(self):
        self.position_environment.check_if_box_ammo_collision(self.name_id, self.position_x, self.position_y, self.width,
                                                              self.height)
