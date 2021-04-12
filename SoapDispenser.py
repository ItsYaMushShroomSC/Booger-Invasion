import pygame
import sys
from pygame.locals import *
from cleaningSupply import *
from main import *

soapDispenserGroup = pygame.sprite.Group()

#The soap dispenser dispenses suds, the currency of the game. It is equivalent to the sunflower.

class SoapDispenser(CleaningSupply):

    def __init__(self, row, column):
        self.image = pygame.image.load("sprayneutral.png")

        super().__init__(row, column, self.image)

        self.cooldown = 2400 #15 seconds
        self.health = 10
        self.startcooldownframes = self.cooldown


soapDispenserGroup.add(SoapDispenser(0, 0))