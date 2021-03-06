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

    def __init__(self, x, y, row):
        img = pygame.image.load('spider.png').convert_alpha()
        super().__init__(x, y, row, img, False) # check out supremeBug.py to see what this initializes
        self.name = 'spider'
        self.health = 5
        self.speed = 6
        self.defaultSpeed = 6
        self.damage = 1
        self.row = row

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed, False)

class Cockroach(Bug):

    def __init__(self, x, y, row):

        img = pygame.image.load('cockroach.png').convert_alpha()
        super().__init__(x, y, row, img, False)  # check out supremeBug.py to see what this initializes
        self.name = 'cochroach'
        self.health = 8
        self.speed = 6
        self.defaultSpeed = 6
        self.damage = 1
        self.row = row

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed, False)

class LadyBug(Bug):

    def __init__(self, x, y, row):

        img = pygame.image.load('ladybug.png').convert_alpha()
        super().__init__(x, y, row, img, False)  # check out supremeBug.py to see what this initializes
        self.name = 'ladybug'
        self.health = 6
        self.speed = 9
        self.defaultSpeed = 9
        self.damage = 1
        self.row = row

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed, False)

class Wasp(Bug):

    def __init__(self, x, y, row):

        img = pygame.transform.flip(pygame.image.load('wasp.png').convert_alpha(), True, False)
        super().__init__(x, y, row, img, False)  # check out supremeBug.py to see what this initializes
        self.name = 'wasp'
        self.health = 10
        self.speed = 8
        self.defaultSpeed = 8
        self.damage = 1
        self.row = row

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed, False)

class Ant(Bug):

    def __init__(self, x, y, row):

        img = pygame.image.load('ant.png').convert_alpha()
        super().__init__(x, y, row, img, False)  # check out supremeBug.py to see what this initializes
        self.name = 'ant'
        self.health = 6
        self.speed = 10
        self.defaultSpeed = 10
        self.damage = 1
        self.row = row

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed, False)

class GiantBug(Bug):

    def __init__(self, x, y, row):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'giantbug'

        super().__init__(x, y, row, pygame.transform.scale(pygame.image.load("ant (1).png").convert_alpha(), (400,600)), False)  # check out supremeBug.py to see what this initializes
        scaleFactor = defaults.scaleFactorH
        if defaults.scaleFactorW < defaults.scaleFactorH:
            scaleFactor = defaults.scaleFactorW
        self.image = pygame.transform.scale(pygame.image.load("ant (1).png").convert_alpha(), (400,600))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = 200
        self.speed = 6
        self.defaultSpeed = 6
        self.damage = 2
        self.row = row

    def update(self):
        super().update(self.speed)

    def damageCS(self, cleaningSupply):
        cleaningSupply.health -= self.damage

    def moveBack(self):
        super().moveBack(self.defaultSpeed, True)