import data.config as c


class TextObject:
    def __init__(self, text, font):
        self.text = text
        self.font = font

    def object(self):
        textSurface = self.font.render(self.text, True, c.black)
        return textSurface, textSurface.get_rect()
