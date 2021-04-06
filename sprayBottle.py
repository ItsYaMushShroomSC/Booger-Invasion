import pygame
import sys
from pygame.locals import *
from cleaningSupply import *
from main import *

sprayBottleGroup = pygame.sprite.Group()

class SprayBottle(CleaningSupply):

    def __init__(self, row, column):
        self.image = pygame.image.load("sprayneutral.png")

        super().__init__(row, column, self.image)

        self.cooldown = 480
        self.health = 10
        self.startcooldownframes = self.cooldown


sprayBottleGroup.add(SprayBottle(0, 0))