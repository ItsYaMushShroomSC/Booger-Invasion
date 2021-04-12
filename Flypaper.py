import pygame
import sys
from pygame.locals import *
from cleaningSupply import *
from main import *

flypaperGroup = pygame.sprite.Group()

#flypaper is a trap, equivalent to a potato mine. It will kill one bug instantly when it touches it but will then dissapear.

class Flypaper(CleaningSupply):

    def __init__(self, row, column):
        self.image = pygame.image.load("sprayneutral.png")

        super().__init__(row, column, self.image)
        self.health = 1


flypaperGroup.add(Flypaper(0, 0))