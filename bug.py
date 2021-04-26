import pygame
import sys
from pygame.locals import *
from main import *
all_sprites = pygame.sprite.Group()


class Bug(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.image = pygame.transform.scale(pygame.image.load("spider.png"), (100,100))
        self.rect = self.image.get_rect()
        self.rect.center = (DISPLAYSURF.get_width() / 2, DISPLAYSURF.get_height() / 2)




    def update(self):
        self.rect.x += 5
        if self.rect.left > DISPLAYSURF.get_width():
            self.rect.right = 0




bug1 = Bug()
all_sprites.add(bug1)
