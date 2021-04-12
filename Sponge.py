import pygame
import sys
from pygame.locals import *
from cleaningSupply import *
from main import *

spongeGroup = pygame.sprite.Group()

#The sponge can absorb a lot of hits. It is equivalent to a Wall-nut. It has no abilities but has way more health than most plants.

class Sponge(CleaningSupply):

    def __init__(self, row, column):
        self.image = pygame.image.load("sprayneutral.png")

        super().__init__(row, column, self.image)
        self.health = 50


spongeGroup.add(Sponge(0, 0))