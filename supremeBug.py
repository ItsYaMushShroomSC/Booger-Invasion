import pygame, time
import sys
from pygame.locals import *
from defaults import *
import random

class Bug(pygame.sprite.Sprite):

    def __init__(self, x, y, img, shouldFlip):
        self.x = x
        self.y = y

        scaleFactor = scaleFactorH
        if scaleFactorW < scaleFactorH:
            scaleFactor = scaleFactorW

        self.image = pygame.transform.scale(img, (100 * scaleFactor, 121 * scaleFactor))

        if shouldFlip == True:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.frozen = False # WHETHER OR NOt the bug is frozen because there's a cleaning supply obstructing its path

    def die(self, enemy_group):
        if self.health <= 0:
            self.remove_internal(enemy_group)


