import pygame
import sys
from pygame.locals import *


#sprite object that represents the seed packet in your inventory for the game

# There is no need for any child classes of this because they are all the same

class CleaningSupplySeed(pygame.sprite.Sprite):

    def __init__(self, img, price, order, restockTime): # order is a number that represents where the seed is in order from (1-9) top to bottom
        self.image = img
        self.price
        self.rect = img.getRect()
        self.order = order
        self.restockTime = restockTime # if restockTime = 0, then the cleaningSupplySeed is in stock/available

    def setImgPos(self): # setsTheImgPos
        pass

    def updateLoadingBar(self): # draws a transparent gray loading bar while the seed is restocking
        pass

    def getPrice(self):
        return self.price

    def getRestockTime(self):
        return self.restockTime




