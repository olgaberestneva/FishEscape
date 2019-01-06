import data.config as c
import data.fuction as func


class FishObject:
    def __init__(self):
        self.gameDisplay = func.gameDisplay()
        self.name = func.load_image(c.FISHIMG_PL).convert_alpha()
        self.x = 50 * 0.45
        self.y = c.display_height * 0.8
        self.x_change = 0
        self.y_change = 0
        self.life = 3

    def update(self):
        self.x += self.x_change
        self.y += self.y_change
        self.gameDisplay.blit(self.name, (self.x, self.y))
        self.scene()

    def end(self):
        if self.life < 0:
            return False
        else:
            return True

    def death(self):
        if self.life >= 0:
            self.life -= 1

#####################################################

    def scene_d(self):
        if self.y > c.display_height - 40:
            return False
        return True

    def scene_u(self):
        if self.y < 100:
            return False
        return True

    def scene_r(self):
        if self.x > c.display_width - 100:
            return False
        return True

    def scene_l(self):
        if self.x < 10:
            return False
        return True

    def scene(self):
        if self.y > c.display_height - 40 or self.y < 100:
            self.y_change = 0
        if self.x > c.display_width - 100 or self.x < 10:
            self.x_change = 0

