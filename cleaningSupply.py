import pygame
import sys
from pygame.locals import *

class CleaningSupply(pygame.sprite.Sprite):
    def __init__(self, row, column, type, price, img):
        self.x = row
        self.y = column
        self.type = type # string name
        self.price = price
        self.destroyed = False
        self.image = img
        self.rect = self.image.getRect()

    #this will be used to activate the cleaning supply's ability, whether it is attacking bugs, healing other plants, producing money, etc.
    def activate(self):
        print("cleaningsupply activated")
        return

    #this will be used to keep track of the cleaningsupply's health when it is attacked by bugs.
    def attacked(self):
        print("cleaningsupply attacked")
        return