import pygame
import sys
from pygame.locals import *
from main import *
all_sprites = pygame.sprite.Group()

class Bug(pygame.sprite.Sprite):

    def __init__(self, pos):
        (x , y) = pos
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load("spider.png")
        # self.rect = self.image.get_rect()
        # self.rect.center = (200,200)
        self.image = pygame.Surface((50, 50))
        self.image = pygame.transform.scale(pygame.image.load("spider.png"), (100,100))

        self.rect = self.image.get_rect()
        self.rect.center = (x , y)


    def update(self):
        self.rect.x += 5
        if self.rect.left > DISPLAYSURF.get_width():
            self.rect.right = 0


bug1 = Bug((DISPLAYSURF.get_width() / 2, DISPLAYSURF.get_height() / 2))
bug2 = Bug((DISPLAYSURF.get_width() / 2 + 121, DISPLAYSURF.get_height() / 2 + 121))
bug3 = Bug((DISPLAYSURF.get_width() / 2 + 242, DISPLAYSURF.get_height() / 2 + 241))
bug4 = Bug((DISPLAYSURF.get_width() / 2 - 121, DISPLAYSURF.get_height() / 2 - 121))
bug5 = Bug((DISPLAYSURF.get_width() / 2 - 242, DISPLAYSURF.get_height() / 2 - 242))
all_sprites.add(bug1)
all_sprites.add(bug2)
all_sprites.add(bug3)
all_sprites.add(bug4)

