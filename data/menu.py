from data.animation import Animation
from data.button import Button

import data.config as c
import data.fuction as func


class Menu:
    def __init__(self):
        self.gameDisplay = func.gameDisplay()
        self.clock = func.init_clock()
        self.logo = func.load_image(c.LOGO).convert_alpha()
        self.image_game_over = func.load_image(c.GAMEOVER).convert_alpha()
        self.play_yes = func.load_image(c.PLAY_ACTIVE).convert_alpha()
        self.play_no = func.load_image(c.PLAY_NOT).convert_alpha()
        self.quit_yes = func.load_image(c.QUIT_ACTIVE).convert_alpha()
        self.quit_no = func.load_image(c.QUIT_NOT).convert_alpha()
        self.image_loading = func.load_image(c.LOADING).convert()
        self.image_menu = func.load_image(c.MENU).convert()
        self.image_pause = func.load_image(c.PAUSE).convert_alpha()

        self.start = Button(self.play_yes, self.play_no, c.display_width / 2 - self.play_no.get_width()/2, 300)
        self.quit = Button(self.quit_yes, self.quit_no, c.display_width / 2 - self.quit_no.get_width()/2, 400)

    def loading(self, action=None):
        image = func.load_image(c.WHEEL).convert_alpha()
        orig_image = image
        rect = image.get_rect(
            center=(c.display_width - image.get_width()/2, c.display_height - image.get_height()/2)
        )  # координаты центра(штурвала, загрузки)
        angle = 0
        events = False
        start_ticks = func.tick()  # starter tick
        while True:
            func.exit()
            seconds = (func.tick() - start_ticks) / 500  # calculate how many seconds
            if seconds > 5:
                events = True
            if seconds > 10:  # if more than 10 seconds close the game
                action()
            else:
                angle += 1
                image, rect = Animation().rotate(orig_image, rect, angle)
                self.gameDisplay.blit(self.image_loading, (0, 0))
                self.gameDisplay.blit(image, rect)
                if events:
                    self.draw(self.logo, c.display_width / 2 - self.logo.get_width()/2, 0)
            func.update(self.clock)

    def menu(self, play_action=None, quit_action=None):
        self.draw(self.image_menu, 0, 0)
        self.draw(self.logo, c.display_width / 2 - self.logo.get_width()/2, 0)
        self.start.click(play_action)
        self.quit.click(quit_action)

    def pause(self, continue_action=None, quit_action=None):
        self.draw(self.image_pause, c.display_width / 2 - self.logo.get_width() / 2, 0)
        self.start.click(continue_action)
        self.quit.click(quit_action)

    def game_over(self, play_action=None, quit_action=None):
        self.draw(self.image_game_over, c.display_width / 2 - 300, 0)
        self.start.click(play_action)
        self.quit.click(quit_action)

    def draw(self, name, x, y):
        self.gameDisplay.blit(name, (x, y))
