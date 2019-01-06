import random
import data.config as c
import data.fuction as func


class BonusObject(func.Strite()):
    def __init__(self):
        super(BonusObject, self).__init__()
        self.name = func.load_image(c.BONUS)
        self.rect = self.name.get_rect(
            center=(random.randint(40, c.display_width - 40), - 200)
        )
        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > c.display_height - 10:
            self.kill()

    def collision(self, player):
        if (self.rect.x < player.x < self.rect.x + 50 and self.rect.y < player.y < self.rect.y + 50) or \
                (self.rect.x < player.x < self.rect.x + 50 and self.rect.y < player.y + 25 < self.rect.y + 50) or \
                (self.rect.x < player.x + 50 < self.rect.x + 50 and self.rect.y < player.y < self.rect.y + 50) or \
                (self.rect.x < player.x + 50 < self.rect.x + 50 and self.rect.y < player.y + 25 < self.rect.y + 50):
                    if player.life < 5:
                        player.life += 1
                    self.kill()
