import random
import data.config as c
import data.fuction as func


class Level:
    def __init__(self):
        self.level = 1
        self.pos_image = 0
        self.max = random.randint(10 * self.level, 15 * self.level)
        self.background = (func.load_image(c.backgroup1),
                           func.load_image(c.backgroup2),
                           func.load_image(c.backgroup3),
                           func.load_image(c.backgroup4),
                           func.load_image(c.backgroup5))

    def new_level(self, dodger):
        if dodger == self.max:
            self.level += 1
            self.pos_image += 1
            if self.pos_image == 5:
                self.pos_image = 0
            self.max = random.randint(10 * self.level, 15 * self.level) + dodger

    def image_fons(self):
        return self.background[self.pos_image]


