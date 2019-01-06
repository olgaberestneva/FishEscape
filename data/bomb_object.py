import random
import data.config as c
import data.fuction as func
from pygame.sprite import Rect


class BombObject(func.Strite()):
    def __init__(self):
        super(BombObject, self).__init__()
        self.name = func.load_image(c.BOMB)
        self.rect = self.name.get_rect(
            center=(random.randint(40, c.display_width - 40), - 200)
        )
        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > c.display_height - 10:
            self.kill()

    def collision(self, player):
        player_rect = Rect(player.x, player.y, 50, 50)
        if self.rect.colliderect(player_rect):
            player.death()
            self.kill()
