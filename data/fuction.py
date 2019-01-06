import pygame
import data.config as c


# TODO запуск
def init():
    pygame.init()


# TODO выход
def game_quit():
    pygame.quit()
    quit()


# TODO загрузка картинок
def load_image(name):
    return pygame.image.load(c.PATH + name)


# TODO загрузка и воспроизведение музыки
def music_play(name, count):
    pygame.mixer.music.load(name)
    pygame.mixer.music.play(count)


# TODO получение координат указателя мыши и нажатых её кнопок
def mouse_click():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    return mouse, click


# TODO обновление игровой облости
def update(clock):
    pygame.display.update()
    clock.tick(120)


# TODO создание параметра обновления FPS
def init_clock():
    return pygame.time.Clock()


# TODO для класса Sprite
def Strite():
    return pygame.sprite.Sprite


# TODO работа с текстом
def text(name, parameter=None):
    font = pygame.font.SysFont("comicsansms", 25)
    if parameter is None:
        info = font.render(name + ": ", True, c.red)
    else:
        info = font.render(name + ": " + str(parameter), True, c.red)
    return info

def number_level(name):
    font = pygame.font.SysFont("comicsansms", 35)
    info = font.render(str(name), True, c.red)
    return info

# TODO таймер
def timer(interval, time):
    load = pygame.USEREVENT + interval
    pygame.time.set_timer(load, time)
    return load


# TODO дисплей
def gameDisplay():
    gameIcon = load_image(c.ICON)
    pygame.display.set_caption('Fish')
    pygame.display.set_icon(gameIcon)
    return pygame.display.set_mode((c.display_width, c.display_height))


# TODO создание панелью Surface
def surface(width, height):
    return pygame.Surface((width, height), pygame.SRCALPHA, 32)


# TODO работа с параметром event
def event():
    return pygame.event.get()


QUIT = pygame.QUIT


def exit():  # кнопка крестик
    for events in event():
        if events.type == QUIT:
            game_quit()

def tick():
    return pygame.time.get_ticks()