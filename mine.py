from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

mine = Ursina()

class Block(Button):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
        parent = scene,
        position = position,
        model = "cube",
        origin_y = 0.5,
        texture = "white_cube",
        color = color.white,
        highlight_color = color.lime
        )
    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                block = Block(position = self.position + mouse.normal)
            elif key == "left mouse down":
                destroy(self)
for z in range(20):
    for x in range(20):
        block = Block(position = (z, 0, x))
player = FirstPersonController()

mine.run()
