import pygame
import sys
from pygame.locals import *
bug = pygame.sprite.Group()

class Bug(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, bug)
        self.image = pygame.image.load("spider.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200,200)
        spider = Bug()
        bug.add(spider)
