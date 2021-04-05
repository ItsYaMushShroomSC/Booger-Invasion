import pygame
import sys
from pygame.locals import *


class CleaningSupply(pygame.sprite.Sprite):

    def __init__(self, row, column, type):
        self.x = row  # the row Reand column are in the game board grid, not the pixel x coordinate
        self.y = column
        self.type = type  # string name

        if(type == "spray bottle"):
            self.img = pygame.image.load("sprayneutral.png")
            self.cooldown = 480
            self.health = 10
        self.destroyed = False
        self.rect = self.img.get_rect() # how long between the supply being able to use its abilities.
        self.startcooldownframes


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
