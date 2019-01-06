import data.fuction as func


class Button:
    def __init__(self, active, not_active, x, y):
        self.gameDisplay = func.gameDisplay()
        self.image_active = active
        self.image_not_active = not_active
        self.width = self.image_active.get_width()
        self.height = self.image_active.get_height()
        self.x = x
        self.y = y

    def click(self, action):
        mouse, click = func.mouse_click()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            self.draw(self.image_active, (self.x, self.y))
            if click[0] == 1 and action is not None:  # если нажата левая кнопка мыши и есть функция
                action()  # переходим на функцию
        else:
            self.draw(self.image_not_active, (self.x, self.y))  # выводим неактивное состояние конпки

    def draw(self, Surf, Rect):
        self.gameDisplay.blit(Surf, Rect)   # выводим на дисплей