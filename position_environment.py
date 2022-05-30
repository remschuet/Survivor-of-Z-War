class PositionEnvironment:
    def __init__(self):
        # create the dictionary for the name: x, y
        self.position_dic = {}

    def set_new_position(self, name, position_x, position_y):
        # set up position for every human
        self.position_dic[name] = (position_x, position_y)

    def print_position_dict(self):
        print(self.position_dic)
