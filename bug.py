import pygame, time
import sys
from pygame.locals import *
from supremeBug import *
import defaults
import random


defaults.setMargins()
XMARG = defaults.XMARGIN
YMARG = defaults.YMARGIN


# spider should take 5 hits before its death

class Spider(Bug):

    def __init__(self, x, y):
        img = pygame.image.load('spider.png')
        super().__init__(x, y, img, False) # check out supremeBug.py to see what this initializes

        self.health = 5
        self.defaultSpeed = 10
        self.speed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed)





class Cockroach(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('cockroach.png')
        super().__init__(x, y, img, False)  # check out supremeBug.py to see what this initializes

        self.health = 7
        self.speed = 10
        self.defaultSpeed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed)

class LadyBug(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('ladybug.png')
        super().__init__(x, y, img, False)  # check out supremeBug.py to see what this initializes

        self.health = 9
        self.speed = 10
        self.defaultSpeed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed)

class Wasp(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('wasp.png')
        super().__init__(x, y, img, True)  # check out supremeBug.py to see what this initializes

        self.health = 11
        self.speed = 10
        self.defaultSpeed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed)

class Ant(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('ant1.png')
        super().__init__(x, y, img, False)  # check out supremeBug.py to see what this initializes

        self.health = 13
        self.speed = 10
        self.defaultSpeed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed)

class GiantBug(Bug):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        scaleFactor = defaults.scaleFactorH
        if defaults.scaleFactorW < defaults.scaleFactorH:
            scaleFactor = defaults.scaleFactorW
        self.image = pygame.transform.scale(pygame.image.load("ant (1).png"), (400,600))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = 13
        self.speed = 6
        self.defaultSpeed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed)