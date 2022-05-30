from human import Human
from position_player import PositionPlayer
from position_environment import PositionEnvironment


class Enemy(Human):
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int, speed: int,
                 position_player: PositionPlayer, position_environment: PositionEnvironment):
        super().__init__(root, name_image, name_id, position_x, position_y, height, width, speed)

        # to can reach position of the player
        self.position_player = position_player
        self.player_position_x = None
        self.player_position_y = None

        # set up position in dict
        self.position_environment = position_environment
        self.position_environment.set_new_position(self.name_id, self.position_x, self.position_y)

    def move_left(self):
        self.position_x -= self.speed//2
        self.draw()

    def move_right(self):
        self.position_x += self.speed//2
        self.draw()

    def move_up(self):
        self.position_y -= self.speed//2
        self.draw()

    def move_down(self):
        self.position_y += self.speed//2
        self.draw()

    def get_new_position(self):
        # get position from position_player
        self.player_position_x, self.player_position_y = self.position_player.get_position()

    def movement(self):
        # get the position
        self.get_new_position()
        # move to the player position x, y
        if self.player_position_x >= self.position_x:
            self.move_right()
        if self.player_position_x < self.position_x:
            self.move_left()
        if self.player_position_y >= self.position_y:
            self.move_down()
        if self.player_position_y < self.position_y:
            self.move_up()
        # inform the dict the new position
        self.set_new_positon()

    def set_new_positon(self):
        self.position_environment.set_new_position(self.name_id, self.position_x, self.position_y)
