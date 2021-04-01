import pygame
import sys
from pygame.locals import *

class CleaningSupply(pygame.sprite.Sprite):
    def __init__(self, row, column, type, price, supplyhealth, cooldown, img):
        self.x = row #the row and column are in the game board grid, not the pixel x coordinate
        self.y = column
        self.type = type # string name
        self.price = price
        self.destroyed = False
        self.image = img
        self.rect = self.image.getRect()
        self.cooldown = cooldown #how long between the supply being able to use its abilities.
        self.supplyhealth = supplyhealth #the amount of times the supply can be attacked before it is destroyed.

    #this will be used to activate the cleaning supply's ability, whether it is attacking bugs, healing other plants, producing money, etc.
    def activate(self):
        if (elapsedcooldown == 0):
            

    #this will be used to keep track of the cleaningsupply's health when it is attacked by bugs.
    def attacked(self):
        supplyhealth -= 1