import pygame
import sys
from pygame.locals import *
import main
#from main import getCleaningSupplyPos


class CleaningSupply(pygame.sprite.Sprite):

    XMARG = None
    YMARG = None
    tileWidth = None
    tileHeight = None

    def __init__(self, row, column, img, XMARG, YMARG, tW, tH):
        self.x = row  # the row Reand column are in the game board grid, not the pixel x coordinate
        self.y = column
        self.destroyed = False
        self.image = img
        self.XMARG = XMARG
        self.YMARG = YMARG
        self.tileWidth = tW
        self.tileHeight = tH
        self.rect = self.image.get_rect() # how long between the supply being able to use its abilities.
        self.rect.center = self.getCleaningSupplyPos(self.x, self.y)

    def getCleaningSupplyPos(self, x, y):  # the pixel position of the top left corner of the box is returned
        xHalf = self.tileWidth/2
        yHalf = self.tileHeight/2
        return self.XMARG + (x * self.tileWidth) + xHalf, self.YMARG + (y * self.tileHeight) + yHalf

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
