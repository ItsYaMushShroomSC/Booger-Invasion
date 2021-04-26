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
        self.speed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)

class Cockroach(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('cockroach.png')
        super().__init__(x, y, img, False)  # check out supremeBug.py to see what this initializes

        self.health = 7
        self.speed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)

class LadyBug(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('ladybug.png')
        super().__init__(x, y, img, False)  # check out supremeBug.py to see what this initializes

        self.health = 7
        self.speed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)

class Wasp(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('wasp.png')
        super().__init__(x, y, img, True)  # check out supremeBug.py to see what this initializes

        self.health = 7
        self.speed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)

class Ant(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('ant.png')
        super().__init__(x, y, img, False)  # check out supremeBug.py to see what this initializes

        self.health = 7
        self.speed = 10
        self.damage = 1

    def update(self):
        super().update(self.speed)