import pygame
import sys
from pygame.locals import *


#sprite object that represents the seed packet in your inventory for the game

# There is no need for any child classes of this because they are all the same

XMARGIN = None
windowWidth = None
windowHeight = None

class CleaningSupplySeed(pygame.sprite.Sprite):

    def __init__(self, img, name, price, order, restockTime, XMARG, windowW, windowH):
        global XMARGIN, windowWidth, windowHeight
        # order is a number that represents where the seed is in order from (1-9) top to bottom
        self.image = img
        self.name = name
        self.price = price
        self.rect = img.get_rect()
        self.order = order
        self.restockTime = restockTime # if restockTime = 0, then the cleaningSupplySeed is in stock/available
        XMARGIN = XMARG
        windowWidth = windowW
        windowHeight = windowH
        self.setImgPos()


    def setImgPos(self): # setsTheImgPos
        centerX = int(XMARGIN/2)
        centerY = int(windowHeight * 1/9 - self.rect.h + self.rect.h*self.order)
        self.rect.center = (centerX, centerY)

    def updateLoadingBar(self): # draws a transparent gray loading bar while the seed is restocking
        pass

    def getPrice(self):
        return self.price

    def getRestockTime(self):
        return self.restockTime

    def getInStock(self):
        if self.restockTime == 0:
            return True
        else:
            return False




