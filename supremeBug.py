import pygame, time
import sys
from pygame.locals import *
import defaults
import random

DISPLAYSURF = defaults.DISPLAYSURF

choices = [DISPLAYSURF.get_height() / 2, DISPLAYSURF.get_height() / 2 - 121, DISPLAYSURF.get_height() / 2 - 242,
           DISPLAYSURF.get_height() / 2 + 121, DISPLAYSURF.get_height() / 2 + 242]

enemy_sprites = pygame.sprite.Group()

defaults.setMargins()
XMARG = defaults.XMARGIN
YMARG = defaults.YMARGIN

class Bug(pygame.sprite.Sprite):

    def __init__(self, x, y, img, shouldFlip):
        self.x = x
        self.y = y

        scaleFactor = defaults.scaleFactorH
        if defaults.scaleFactorW < defaults.scaleFactorH:
            scaleFactor = defaults.scaleFactorW

        self.image = pygame.transform.scale(img, (100 * scaleFactor, 121 * scaleFactor))

        if shouldFlip == True:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.frozen = False # WHETHER OR NOt the bug is frozen because there's a cleaning supply obstructing its path

    def update(self, speed):
        global XMARG

        if self.frozen == False:
            self.rect.x -= speed

        if (self.rect.x <= XMARG):
            self.rect.x += speed
            self.health = 0
        self.die()

    def die(self):
        if self.health <= 0:
            enemy_sprites.remove_internal(self)


