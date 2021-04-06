import pygame
import sys
from pygame.locals import *
from cleaningSupply import *
from main import *

sprayBottleGroup = pygame.sprite.Group()

class SprayBottle(CleaningSupply):

    def __init__(self, row, column):

        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("sprayneutral.png"), (100, 121)))

        self.cooldown = 480
        self.health = 10
        self.startcooldownframes = self.cooldown


sprayBottleGroup.add_internal(SprayBottle(0, 0))