import pygame
import sys
from pygame.locals import *
from main import DISPLAYSURF

pygame.init()

class Plant:
    def __init__(self, row, column, type, price):
        self.x = row
        self.y = column
        self.type = type
        self.price = price
        self.destroyed = False

    def activate(self):
        print("plant activated")
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (0, 0, 100, 100))
        return

    def attacked(self):
        print("plant attacked")
        return