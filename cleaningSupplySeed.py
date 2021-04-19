import pygame
import sys
from pygame.locals import *
import defaults

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
        self.RESTOCKLENGTH = restockTime
        self.restockTime = restockTime # if restockTime = 0, then the cleaningSupplySeed is in stock/available
        self.loadIncrement = self.rect.h/(self.RESTOCKLENGTH/250) # restocklength should be a multiple of 250
        self.countIncrement = 0
        self.inStock = True
        XMARGIN = XMARG
        windowWidth = windowW
        windowHeight = windowH
        self.setImgPos()

    def resetRestockTime(self): # resets the restockTime after the seed has been planted
        self.restockTime = self.RESTOCKLENGTH
        self.countIncrement = 0

    def setImgPos(self): # setsTheImgPos
        centerX = int(XMARGIN/2)
        centerY = int(windowHeight * 1/9 - self.rect.h + self.rect.h*self.order)
        self.rect.center = (centerX, centerY)

    def updateLoadingBar(self, timeElapsed): # draws a transparent gray loading bar while the seed is restocking
        if self.inStock == False:
            self.restockTime - 250 # every 250 milliseconds, the loading bar moves
            transparentRectSurf = pygame.Surface((self.rect.w, self.rect.h-self.loadIncrement*self.countIncrement))
            transparentRectSurf.set_alpha(128)
            transparentRectSurf.fill((255, 255, 255))
            #transparentRect= Rect(self.rect.left, self.rect.top, self.rect.w, self.rect.h-self.loadIncrement*self.countIncrement)
            self.countIncrement += 1
            defaults.DISPLAYSURF.blit(transparentRectSurf, (self.rect.left, self.rect.top))



    def updateRestockTime(self):
        if self.restockTime <= 0:
            self.inStock = False
        else:
            self.inStock = True




