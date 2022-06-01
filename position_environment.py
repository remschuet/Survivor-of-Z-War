class PositionEnvironment:
    def __init__(self):
        # create the dictionary for the name: x, y
        self.position_dic = {}

    def set_new_position(self, name, position_x, position_y):
        # set up position for every human
        self.position_dic[name] = (position_x, position_y)

    def print_position_dict(self):
        print(self.position_dic)

    def get_position_player(self):
        if "player" in self.position_dic:
            return self.position_dic["player"]

    def check_if_collision(self):
        print("here we check the collision human")