class PositionEnvironment:
    def __init__(self):
        # create the dictionary for the name: x, y
        self.human_position_dic = {}
        self.human_name = None

    def set_new_position(self, name, position_x, position_y, width, height):
        # set up position for every human
        self.human_position_dic[name] = (position_x, position_y, width, height)

    def print_position_dict(self):
        print(self.human_position_dic)

    def get_position_player(self):
        if "player" in self.human_position_dic:
            return self.human_position_dic["player"]

    def destroy_enemy_in_dict(self, name):
        self.human_position_dic.pop(name)

    def check_if_collision(self, name, position_x, position_y, width, height):
        for self.human_name, (x, y, w, h) in self.human_position_dic.items():
            if name != self.human_name:
                if position_x + width >= x and \
                        position_x <= x + w and \
                        position_y + height >= y and \
                        position_y <= y + h:
                    # Return name of the object in collision not the player
                    print("collision")
                    return True
        return False
