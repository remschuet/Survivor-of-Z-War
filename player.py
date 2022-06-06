from object import Object
from position_environment import PositionEnvironment


class Player(Object):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: int, position_environment: PositionEnvironment):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed)

        # for position in dict
        self.position_environment = position_environment
        self.position_environment.set_new_position(self.name_id, self.position_x, self.position_y, self.width, self.height)

        # for the bullet creation
        self.direction = None

        # inform position_player the x, y
        self.set_new_position()

    def move_left(self):
        self.position_x -= self.speed
        self.direction = "left"
        self.draw()
        self.set_new_position()

    def move_right(self):
        self.position_x += self.speed
        self.direction = "right"
        self.draw()
        self.set_new_position()

    def move_up(self):
        self.position_y -= self.speed
        self.direction = "up"
        self.draw()
        self.set_new_position()

    def move_down(self):
        self.position_y += self.speed
        self.direction = "down"
        self.draw()
        self.set_new_position()

    def set_new_position(self):
        # self.position_player.set_new_position(self.position_x, self.position_y)
        self.position_environment.set_new_position(self.name_id, self.position_x, self.position_y, self.width, self.height)
        # print the dict
        # self.position_environment.print_position_dict()

    def get_position(self):
        return self.position_x, self.position_y

    def get_direction(self):
        return str(self.direction)
