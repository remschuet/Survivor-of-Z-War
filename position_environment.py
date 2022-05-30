class PositionEnvironment:
    def __init__(self):
        self.position_dic = {}

    def set_new_position(self, name, position_x, position_y):
        self.position_dic[name] = (position_x, position_y)

    def print_position_dict(self):
        print(self.position_dic)

        # print(f" Player {name} now at x={position_x} y={position_y} )")
