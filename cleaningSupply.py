import pygame
import sys
from pygame.locals import *
from main import *


class CleaningSupply(pygame.sprite.Sprite):

    def __init__(self, row, column, img):
        self.x = row  # the row Reand column are in the game board grid, not the pixel x coordinate
        self.y = column
        self.destroyed = False
        self.image = img
        self.rect = self.image.get_rect() # how long between the supply being able to use its abilities.
        self.startcooldownframes = self.cooldown

    def setRectPos(self):
        self.rect.topleft = getCleaningSupplyPos(self.x, self.y)



    # this will be used to activate the cleaning supply's ability, whether it is attacking bugs, healing other plants, producing money, etc.
    def activate(self):
        global frames, startcooldownframes, cooldown
        if (frames - startcooldownframes == cooldown):
            pass
            startcooldownframes = frames
    # this will be used to keep track of the cleaningsupply's health when it is attacked by bugs.
    def attacked(self):
        global health
        health -= 1
