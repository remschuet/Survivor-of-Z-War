class PositionEnvironment:
    def __init__(self, player_pv):
        # dictionary for object name: x, y, w, h
        self.object_position_dict = {}
        # list to know enemy need to destroy
        self.enemy_need_to_destroy = []
        # list to know bullet need to destroy
        self.bullet_need_to_destroy = []
        # list to know ammo need to destroy
        self.box_ammo_image_need_to_destroy = []
        # for the opponent collision
        self.opponent_object = None
        # player pv
        self.player_pv = player_pv
        # bool to know if alive
        self.player_alive = True
        # list of every possibility of box ammo
        self.possibility_box_ammo = ["box_ammo1", "2"]

    def get_player_pv(self):
        return self.player_pv

    def get_box_ammo_to_destroy(self):
        return self.box_ammo_image_need_to_destroy

    def get_bool_player_alive_or_not(self):
        return self.player_alive

    def get_list_of_bullet_to_destroy(self):
        return self.bullet_need_to_destroy

    def get_list_of_enemy_to_destroy(self):
        return self.enemy_need_to_destroy

    def get_position_player(self):
        return self.object_position_dict["player"]

    def set_ammo_variable_true(self):
        self.box_ammo_image_need_to_destroy = True

    def manage_player_pv(self):
        if self.player_pv > 1:
            self.player_pv -= 1
        elif self.player_pv <= 1:
            self.player_alive = False

    def set_new_position_in_dict(self, name, position_x, position_y, width, height):
        # set up position for every object
        self.object_position_dict[name] = (position_x, position_y, width, height)

    def destroy_object_in_dict(self, name):
        self.object_position_dict.pop(name)

    def check_if_enemy_collision(self, name_id, position_x, position_y, width, height):
        for self.opponent_object, (x, y, w, h) in self.object_position_dict.items():
            # to can take all the enemy
            all_number_to_100 = str(list(range(1, 100)))
            if name_id != self.opponent_object and self.opponent_object != "enemy"+all_number_to_100 \
                    and self.opponent_object != "box_ammo1" and self.opponent_object != "box_ammo2" \
                    and self.opponent_object != "box_ammo3" and self.opponent_object != "box_ammo4"\
                    and self.opponent_object != "box_ammo5" and self.opponent_object != "box_ammo6"\
                    and self.opponent_object != "box_ammo7" and self.opponent_object != "box_ammo8":
                if position_x + width >= x and \
                        position_x <= x + w and \
                        position_y + height >= y and \
                        position_y <= y + h:

                    # clear some list
                    self.enemy_need_to_destroy.clear()
                    self.bullet_need_to_destroy.clear()
                    # add enemy and bullet in list
                    self.enemy_need_to_destroy.append(name_id)
                    self.bullet_need_to_destroy.append(self.opponent_object)
                    # check collision with player
                    if self.opponent_object == "player":
                        # decrease player pv
                        self.manage_player_pv()
                    return self.opponent_object
        return False

    def check_if_box_ammo_collision(self, name_id, position_x, position_y, width, height):
        for self.opponent_object, (x, y, w, h) in self.object_position_dict.items():
            if name_id != self.opponent_object and self.opponent_object == "player":
                if position_x + width >= x and \
                        position_x <= x + w and \
                        position_y + height >= y and \
                        position_y <= y + h:
                    print("player collision with ammo")
                    self.box_ammo_image_need_to_destroy.append(name_id)
