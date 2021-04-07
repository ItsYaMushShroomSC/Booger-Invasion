import pygame
import sys
from pygame.locals import *
from cleaningSupply import *

class SprayBottle(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):

        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("sprayneutral.png"), (tileW-2, tileH-2)), XMARG, YMARG, tileW, tileH)

        self.cooldown = 480
        self.health = 10
        self.startcooldownframes = self.cooldown


