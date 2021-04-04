import pygame, time
import sys
from pygame.locals import *
from main import *
# spider should take 5 hits before its death


all_sprites = pygame.sprite.Group()

class Spider(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        x,y = pos
        self.image = pygame.Surface((50, 50))
        self.image = pygame.transform.scale(pygame.image.load("spider.png"), (100,100))

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)



    def update(self):

        # your code

        self.rect.x += 5
        if self.rect.left > DISPLAYSURF.get_width():
            self.rect.right = 0

class Cockroach(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        x,y = pos
        self.image = pygame.Surface((50, 50))
        self.image = pygame.transform.scale(pygame.image.load("cockroach.png"), (100,100))

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


    def update(self):
        self.rect.x += 5
        if self.rect.left > DISPLAYSURF.get_width():
            self.rect.right = 0


bug1 = Spider((DISPLAYSURF.get_width() / 2, DISPLAYSURF.get_height() / 2))
bug2 = Spider((DISPLAYSURF.get_width() / 2, DISPLAYSURF.get_height() / 2 - 121))
bug3 = Spider((DISPLAYSURF.get_width() / 2, DISPLAYSURF.get_height() / 2 - 242))
bug4 = Spider((DISPLAYSURF.get_width() / 2, DISPLAYSURF.get_height() / 2 + 121))
bug5 = Spider((DISPLAYSURF.get_width() / 2, DISPLAYSURF.get_height() / 2 + 242))
all_sprites.add(bug1)
all_sprites.add(bug2)
all_sprites.add(bug3)
all_sprites.add(bug4)
all_sprites.add(bug5)

