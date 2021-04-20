import random
import defaults
import pygame
import sys
from pygame.locals import *

class Bubble(pygame.sprite.Sprite):

    def __init__(self, isCleaninSupplyBubble):

        self.image = pygame.image.load('bubbleimg.PNG')
        w, h = self.image.get_width() * defaults.scaleFactorH, self.image.get_height() * defaults.scaleFactorH
        self.image = pygame.transform.smoothscale(pygame.sprite.load('bubbleimg.PNG'), (w, h))
        self.rect = self.image.get_rect()

        if isCleaninSupplyBubble == False: # random bubble position for a bubble unrelated to cleaning supply
            self.setRandomPosDefault()

    def setRandomPosCleaningSupply(self):
        pass

    def setRandomPosDefault(self):
        choices = ['left', 'top', 'right', 'bottom']

        dir = random.choice(choices)
        if dir == 'left':
            y = random.randint(0, defaults.windowHeight)
            self.rect.midright = (defaults.XMARGIN, y)

        if dir == 'right':
            y = random.randint(0, defaults.windowHeight)
            self.rect.midleft = (defaults.windowWidth - defaults.XMARGIN, y)

        if dir == 'top':
            x = random.randint(0, defaults.windowWidth)
            self.rect.midbottom = (x, defaults.YMARGIN)

        if dir == 'bottom':
            x = random.randint(0, defaults.windowWidth)
            self.rect.midtop = (x, defaults.windowHeight - defaults.YMARGIN)
