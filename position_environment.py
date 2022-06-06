class PositionEnvironment:
    def __init__(self):
        # create the dictionary for the name: x, y
        self.human_bullet_position_dic = {}
        # create a list who tell management environment to destroy enemy
        self.enemy_need_to_destroy = []
        self.human_bullet_name = None

    def get_list_of_enemy_to_destroy(self):
        return self.enemy_need_to_destroy

    def set_new_position(self, name, position_x, position_y, width, height):
        # set up position for every human
        self.human_bullet_position_dic[name] = (position_x, position_y, width, height)

    def print_position_dict(self):
        print(self.human_bullet_position_dic)

    def get_position_player(self):
        if "player" in self.human_bullet_position_dic:
            return self.human_bullet_position_dic["player"]

    def destroy_enemy_in_dict(self, name):
        self.human_bullet_position_dic.pop(name)

    def check_if_collision(self, name_id, position_x, position_y, width, height):
        for self.human_bullet_name, (x, y, w, h) in self.human_bullet_position_dic.items():
            if name_id != self.human_bullet_name and self.human_bullet_name != "enemy1" and self.human_bullet_name != "enemy2":
                if position_x + width >= x and \
                        position_x <= x + w and \
                        position_y + height >= y and \
                        position_y <= y + h:
                    # Return name of the object in collision not the player
                    self.enemy_need_to_destroy.clear()
                    self.enemy_need_to_destroy.append(name_id)
                    # print("collision")
                    # print(self.enemy_need_to_destroy)
                    # if self.human_bullet_name == "bullet1":
                    # self.destroy_enemy_in_dict(name)
                    return self.human_bullet_name
        return False
