import random
import defaults
import pygame
import sys
from pygame.locals import *

class Bubble(pygame.sprite.Sprite):

    def __init__(self, isCleaningSupplyBubble, cleaningSupplyRect, isDouble):

        self.image = pygame.image.load('bubbleimg.PNG')

        if isDouble == True: self.image = pygame.image.load('doublebubble.PNG')

        w, h = 54 * defaults.scaleFactorH, 54 * defaults.scaleFactorH
        self.image = pygame.transform.smoothscale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.shouldRemoveCounter = 8

        if isCleaningSupplyBubble == False: # random bubble position for a bubble unrelated to cleaning supply
            self.setRandomPosDefault()

        if isCleaningSupplyBubble == True:
            self.setRandomPosCleaningSupply(cleaningSupplyRect)

    def getShouldRemove(self): # updates and gets should the bubble be removed

        self.shouldRemoveCounter -= 1
        if self.shouldRemoveCounter < 0:
            return True
        else:
            return False

    def setRandomPosCleaningSupply(self, cleaningSupplyRect):
        self.rect.center = cleaningSupplyRect.center

    def setRandomPosDefault(self):
        choices = ['left', 'top', 'right', 'bottom']

        defaults.setMargins()

        dir = random.choice(choices)
        if dir == 'left':
            y = random.randint(defaults.YMARGIN, defaults.windowHeight-defaults.YMARGIN)
            self.rect.midright = (defaults.XMARGIN, y)

        if dir == 'right':
            y = random.randint(defaults.YMARGIN, defaults.windowHeight-defaults.YMARGIN)
            self.rect.midleft = (defaults.windowWidth - defaults.XMARGIN, y)

        if dir == 'top':
            x = random.randint(defaults.XMARGIN, defaults.windowWidth-defaults.XMARGIN)
            self.rect.midbottom = (x, defaults.YMARGIN)

        if dir == 'bottom':
            x = random.randint(defaults.XMARGIN, defaults.windowWidth-defaults.XMARGIN)
            self.rect.midtop = (x, defaults.windowHeight - defaults.YMARGIN)
