import pygame, time
import sys
from pygame.locals import *
from supremeBug import *
from defaults import *
import random

# spider should take 5 hits before its death
choices = [DISPLAYSURF.get_height() / 2, DISPLAYSURF.get_height() / 2 - 121, DISPLAYSURF.get_height() / 2 - 242,
           DISPLAYSURF.get_height() / 2 + 121, DISPLAYSURF.get_height() / 2 + 242]

enemy_sprites = pygame.sprite.Group()


class Spider(Bug):

    def __init__(self, x, y):
        img = pygame.image.load('spider.png')
        super().__init__(x, y, img, False) # check out supremeBug.py to see what this initializes

        self.health = 5


    def update(self):
        self.rect.x -= 10
        if (self.rect.x <= (DISPLAYSURF.get_width()) / 4):
            self.rect.x += 10
            self.health = 0
        super().die(enemy_sprites)


class Cockroach(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('cockroach.png')
        super().__init__(x, y, img, False)  # check out supremeBug.py to see what this initializes

        self.health = 7

    def update(self):
        self.rect.x -= 10
        if (self.rect.x <= (DISPLAYSURF.get_width()) / 4):
            self.rect.x += 10
            self.health = 0
        super().die(enemy_sprites)


class LadyBug(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('ladybug.png')
        super().__init__(x, y, img, False)  # check out supremeBug.py to see what this initializes

        self.health = 7

    def update(self): # hasObstacle is a boolean that represents whether the bug has a plant colliding in front of it
        self.rect.x -= 10
        if (self.rect.x <= (DISPLAYSURF.get_width()) / 4):
            self.rect.x += 10
            self.health = 0
        super().die(enemy_sprites)

class Wasp(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('wasp.png')
        super().__init__(x, y, img, True)  # check out supremeBug.py to see what this initializes

        self.health = 7


    def update(self):
        self.rect.x -= 30
        if (self.rect.x <= (DISPLAYSURF.get_width()) / 4):
            self.rect.x += 10
            self.health = 0
        super().die(enemy_sprites)

class Ant(Bug):

    def __init__(self, x, y):

        img = pygame.image.load('ant.png')
        super().__init__(x, y, img, False)  # check out supremeBug.py to see what this initializes

        self.health = 7

    def update(self):
        self.rect.x -= 10
        if (self.rect.x <= (DISPLAYSURF.get_width()) / 4):
            self.rect.x += 10
            self.health = 0
        super().die(enemy_sprites)

