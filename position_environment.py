class PositionEnvironment:
    def __init__(self):
        # create the dictionary for the name: x, y
        self.human_bullet_position_dic = {}
        # create a list who tell management environment to destroy enemy
        self.enemy_need_to_destroy = []
        self.bullet_need_to_destroy = []
        # add bullet in the inventory of the player
        self.new_ammo = None
        self.human_or_bullet_name = None
        # to check if he died
        self.player_pv = 2
        self.player_alive = True

    def reset_ammo_variable(self):
        self.new_ammo = None

    def manage_player_pv(self):
        if self.player_pv > 0:
            self.player_pv -= 1
        elif self.player_pv <= 0:
            self.player_alive = False

    def get_player_alive_or_not(self):
        return self.player_alive

    def get_list_of_bullet_to_destroy(self):
        return self.bullet_need_to_destroy

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
        for self.human_or_bullet_name, (x, y, w, h) in self.human_bullet_position_dic.items():
            # to can take all the enemy
            all_number_to_100 = str(list(range(1, 100)))
            if name_id != self.human_or_bullet_name and self.human_or_bullet_name != "enemy"+all_number_to_100:
                if position_x + width >= x and \
                        position_x <= x + w and \
                        position_y + height >= y and \
                        position_y <= y + h:
                    # Return name of the object in collision not the player
                    self.enemy_need_to_destroy.clear()
                    self.bullet_need_to_destroy.clear()
                    # put the enemy in a list
                    self.enemy_need_to_destroy.append(name_id)
                    self.bullet_need_to_destroy.append(self.human_or_bullet_name)
                    # check collision with player
                    if self.human_or_bullet_name == "player":
                        self.manage_player_pv()
                    return self.human_or_bullet_name
        return False
