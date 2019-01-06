import pygame
import random

from data.fish_object import FishObject
from data.enemy_shark import EnemyShark
from data.bonus_object import BonusObject
from data.bomb_object import BombObject
from data.info_object import InfoObject
from data.menu import Menu
from data.level import Level

import data.fuction as func


class Game:
    def __init__(self):
        self.gameDisplay = func.gameDisplay()
        self.clock = func.init_clock()
        self.pause = False
        self.menu = Menu()
        self.menu.loading(self.init)

    def init(self):
        while True:
            func.exit()
            self.menu.menu(self.start, func.game_quit)
            func.update(self.clock)

    def start(self):
        ############
        func.music_play('sound/pobega.wav', -1)
        ############
        level = Level()
        game_exit = False
        player = FishObject()
        enemy = EnemyShark()
        info = InfoObject()

        time_bonus = func.timer(1, 10000)
        all_bonus = pygame.sprite.Group()

        while not game_exit:

            for event in func.event():
                if event.type == func.QUIT:
                    func.game_quit()
                if event.type == time_bonus:
                    randoms = random.randint(0, 1)
                    if randoms == 1:
                        bonus = BonusObject()
                        all_bonus.add(bonus)
                    else:
                        bomb = BombObject()
                        all_bonus.add(bomb)

                if event.type == pygame.KEYDOWN:     # передвижение если клавиша нажата
                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and player.scene_u():
                        player.y_change = -5
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and player.scene_d():
                        player.y_change = 5
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player.scene_l():
                        player.x_change = -5
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and player.scene_r():
                        player.x_change = 5

                    if event.key == pygame.K_p:
                        self.pause = True
                        self.paused()
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        game_exit = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
                            event.key == pygame.K_w or event.key == pygame.K_s:
                        player.y_change = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a or \
                            event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.x_change = 0

            self.gameDisplay.blit(level.image_fons(), (0, 0))
            all_bonus.update()
            for bonusik in all_bonus:
                self.gameDisplay.blit(bonusik.name, bonusik.rect)
                bonusik.collision(player)

            enemy.update()
            enemy.collision(player)
            player.update()
            level.new_level(enemy.dodger)

            if not player.end():
                self.crash(level.image_fons())

            info.update(enemy.dodger, level.level, player.life)

            func.update(self.clock)

    def crash(self, image):
        ####################################
        crash_sound = pygame.mixer.Sound("sound/proigrysh.wav")
        #############
        pygame.mixer.Sound.play(crash_sound)
        pygame.mixer.music.stop()
        ####################################
        self.gameDisplay.blit(image, (0, 0))

        while True:
            func.exit()
            self.menu.game_over(self.start, func.game_quit)
            func.update(self.clock)

    def un_pause(self):
        pygame.mixer.music.unpause()
        self.pause = False

    def paused(self):
        ############
        pygame.mixer.music.pause()
        #############
        while self.pause:
            func.exit()
            self.menu.pause(self.un_pause, func.game_quit)
            func.update(self.clock)
