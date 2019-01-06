import data.config as c
import data.fuction as func


class InfoObject:
    def __init__(self):
        self.gameDisplay = func.gameDisplay()
        self.clock = func.init_clock()
        self.life = func.load_image(c.LIFE)
        self.dead = func.load_image(c.DEAD)
        self.xp = [1, 1, 1, 1, 1]
        self.position = [75, 100, 125, 150, 175]
        self.max_life = 5

        self.star = func.load_image(c.STAR).convert_alpha()
        self.info = func.load_image(c.INFO).convert_alpha()

    def update(self, dodger, level, life):
        surf = func.surface(210, 110)
        surf.blit(self.info, (50, 0))
        surf.blit(self.star, (0, 0))
        levels = func.number_level(level)
        score = func.text("Score", dodger)
        surf.blit(levels, (40, 25))
        surf.blit(score, (80, 55))
        self.lifes(surf, life)
        self.gameDisplay.blit(surf, (0, 0))
        func.update(self.clock)

    def input_text(self, surf, info_text, parameters, x, y):
        text = func.text(info_text, parameters)
        surf.blit(text, (x, y))

    def lifes(self, surf, life):
        pos = 0
        i = 0
        while pos < self.max_life:  # создается массив мз максимального уровня жизней(сердечек)
            if pos < life:
                self.xp[pos] = 1
            else:
                self.xp[pos] = 0
            pos += 1
        for xps in self.xp:
            if xps == 0:
                surf.blit(self.dead, (self.position[i], 13))
            else:
                surf.blit(self.life, (self.position[i], 13))
            i = (i + 1) % len(self.position)
