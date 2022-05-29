from object_scene import ObjectScene


class Enemy(ObjectScene):
    def __init__(self,  root, name, position_x: int, position_y: int, height: int, width: int, speed: int):
        super().__init__(root, name, position_x, position_y, height, width, speed)

