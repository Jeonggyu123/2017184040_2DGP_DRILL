from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.x = 0
        self.y = 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self): pass


