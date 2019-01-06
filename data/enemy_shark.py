import random
import data.config as c
import data.fuction as func


class EnemyShark:
    def __init__(self):
        self.gameDisplay = func.gameDisplay()
        self.name = func.load_image(c.FISHIMG_GOG).convert_alpha()
        self.x = c.display_width + 800
        self.y = random.randrange(40, c.display_height - 40)
        self.speed = random.randrange(5, 15)
        self.dodger = 0
        self.width = self.name.get_width()
        self.height = self.name.get_height()

    def update(self):
        self.x = self.x - self.speed
        if self.x > - 200:
            self.gameDisplay.blit(self.name, (self.x, self.y))
        else:
            self.randoms()
            self.dodger += 1

    def randoms(self):
        self.speed = random.randrange(5, 15)
        self.x = c.display_width + 800
        self.y = random.randrange(40, c.display_height - 40)

    def collision(self, player):
        if self.x < player.x < self.x + self.width and self.y < player.y < self.y + self.height or \
                self.x < player.x < self.x + self.width and self.y < player.y + 41 < self.y + self.height or \
                self.x < player.x + 75 < self.x + self.width and self.y < player.y < self.y + self.height or \
                self.x < player.x + 75 < self.x + self.width and self.y < player.y + 41 < self.y + self.height:
            self.randoms()
            self.dodger += 1  # счетчик плюс 1
            player.death()  # сердечко минус
