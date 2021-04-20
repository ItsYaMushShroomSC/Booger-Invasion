import pygame, time
import sys
from pygame.locals import *
from defaults import *
import random

# spider should take 5 hits before its death
choices = [DISPLAYSURF.get_height() / 2, DISPLAYSURF.get_height() / 2 - 121, DISPLAYSURF.get_height() / 2 - 242,
           DISPLAYSURF.get_height() / 2 + 121, DISPLAYSURF.get_height() / 2 + 242]

enemy_sprites = pygame.sprite.Group()


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
        self.health = 7
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x -= 10
        if (self.rect.x <= (DISPLAYSURF.get_width()) / 4):
            self.rect.x += 10
            self.health = 0
        if self.health == 0:
            self.kill()

class LadyBug(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        scaleFactor = scaleFactorH
        if scaleFactorW < scaleFactorH:
            scaleFactor = scaleFactorW
        self.health = 7
        self.image = pygame.transform.scale(pygame.image.load("ladybug.png"), (100 * scaleFactor, 121 * scaleFactor))
        self.health = 7
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

class Wasp(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        scaleFactor = scaleFactorH
        if scaleFactorW < scaleFactorH:
            scaleFactor = scaleFactorW
        self.health = 7
        self.image = pygame.transform.scale(pygame.image.load("wasp.png"), (100 * scaleFactor, 121 * scaleFactor))
        self.image = pygame.transform.flip(self.image, True, False)
        self.health = 7
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

class Ant(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        scaleFactor = scaleFactorH
        if scaleFactorW < scaleFactorH:
            scaleFactor = scaleFactorW
        self.health = 7
        self.image = pygame.transform.scale(pygame.image.load("ant.png"), (100 * scaleFactor, 121 * scaleFactor))
        self.health = 7
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x -= 10
        if (self.rect.x <= (DISPLAYSURF.get_width()) / 4):
            self.rect.x += 10
            self.health = 0
        if self.health == 0:
            self.kill()



