import pygame, time
import sys
from pygame.locals import *
from main import *
import random

# spider should take 5 hits before its death
choices = [DISPLAYSURF.get_height() / 2, DISPLAYSURF.get_height() / 2 - 121, DISPLAYSURF.get_height() / 2 - 242,
           DISPLAYSURF.get_height() / 2 + 121, DISPLAYSURF.get_height() / 2 + 242]

# enemy_sprites = pygame.sprite.Group()


class Spider(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        scaleFactor = scaleFactorH
        if scaleFactorW < scaleFactorH:
            scaleFactor = scaleFactorW
        self.health = 5
        self.image = pygame.transform.scale(pygame.image.load("spider.png"), (100 * scaleFactor, 121 * scaleFactor))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x -= 10
        if (self.rect.x <= (DISPLAYSURF.get_width()) / 4):
            self.rect.x += 10
            self.health = 0
        self.die()

    def die(self):
        if self.health == 0:
            self.kill()


class Cockroach(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        scaleFactor = scaleFactorH
        if scaleFactorW < scaleFactorH:
            scaleFactor = scaleFactorW
        self.health = 7
        self.image = pygame.transform.scale(pygame.image.load("cockroach.png"), (100 * scaleFactor, 121 * scaleFactor))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x -= 10
        if (self.rect.x <= (DISPLAYSURF.get_width()) / 4):
            self.rect.x += 10
            self.health = 0
        self.die()

    def die(self):
        if self.health == 0:
            self.kill()


# cock1 = Cockroach(3*DISPLAYSURF.get_width() / 4 + 50, DISPLAYSURF.get_height() / 2 + 242)

# enemy_sprites.add(cock1)
# if gameLevel == 1:
class Dirt():
    def __init__(self):
        self.joy = 10

class Sprites:
    def __init__(self):
        self.enemy_sprites = pygame.sprite.Group()
        self.add_Sprite()

    def add_Sprite(self):
        for i in range(5):
            # random spawning

            x = 3 * DISPLAYSURF.get_width() / 4
            y = random.choice(choices)
            spider = Spider(x, y)
            # rep_time = pygame.time.get_ticks()
            # if rep_time - curr_time > 100:
            self.enemy_sprites.add(spider)





    #
    # print(f'{curr_time} 1')
    # print(f'{rep_time} 2')



