class PositionPlayer:
    def __init__(self):

        self.position_x = 20
        self.position_y = 20

        self.position_list = []

    def set_new_position(self, position_x, position_y):
        self.change_value_position(position_x, position_y)
        self.position_list = (self.position_x, self.position_y)
        # print(self.position_list)

    def change_value_position(self, new_position_x, new_position_y):
        self.position_x = new_position_x
        self.position_y = new_position_y

    def get_position(self):
        return self.position_list
