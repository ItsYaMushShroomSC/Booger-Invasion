import pygame
import sys
from pygame.locals import *

# global variables

XMARGIN = None
YMARGIN = None
tileWidth = None
tileHeight = None

class CleaningSupply(pygame.sprite.Sprite):

    def __init__(self, row, column, img, XMARG, YMARG, tW, tH):
        global XMARGIN, YMARGIN, tileWidth, tileHeight
        self.x = row  # the row Reand column are in the game board grid, not the pixel x coordinate
        self.y = column
        self.destroyed = False
        self.image = img
        XMARGIN = XMARG
        YMARGIN = YMARG
        tileWidth = tW
        tileHeight = tH
        self.rect = self.image.get_rect() # how long between the supply being able to use its abilities.
        self.rect.center = self.getCleaningSupplyPos(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image) # setMask must be called every time the position of the sprite changes

    def setMask(self):
        self.mask = pygame.mask.from_surface(self.image)

    def getCleaningSupplyPos(self, x, y):  # the pixel position of the top left corner of the box is returned
        xHalf = tileWidth/2
        yHalf = tileHeight/2
        return XMARGIN + (x * tileWidth) + xHalf + 1, YMARGIN + (y * tileHeight) + yHalf + 1

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
