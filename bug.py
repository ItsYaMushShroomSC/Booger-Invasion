import pygame, time
import sys
from pygame.locals import *
from main import *
# spider should take 5 hits before its death


enemy_sprites = pygame.sprite.Group()

class Spider(pygame.sprite.Sprite):

    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        scaleFactor = scaleFactorH
        if scaleFactorW < scaleFactorH:
            scaleFactor = scaleFactorW

        self.image = pygame.transform.scale(pygame.image.load("spider.png"), (100 * scaleFactor, 121 * scaleFactor))

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)




    def update(self):

        self.rect.x -= 20
        if self.rect.left > DISPLAYSURF.get_width():
            self.rect.x = 0



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



def death(self):

    if self.x == DISPLAYSURF.get_width() / 4 and self.y == DISPLAYSURF.get_height() / 2:
        enemy_sprites.remove(self)

bug1 = Spider(3*DISPLAYSURF.get_width() / 4, DISPLAYSURF.get_height() / 2)
bug2 = Spider(3*DISPLAYSURF.get_width() / 4, DISPLAYSURF.get_height() / 2 - 121)
bug3 = Spider(3*DISPLAYSURF.get_width() / 4, DISPLAYSURF.get_height() / 2 - 242)
bug4 = Spider(3*DISPLAYSURF.get_width() / 4, DISPLAYSURF.get_height() / 2 + 121)
bug5 = Spider(3*DISPLAYSURF.get_width() / 4, DISPLAYSURF.get_height() / 2 + 242)
enemy_sprites.add(bug1)
enemy_sprites.add(bug2)
enemy_sprites.add(bug3)
enemy_sprites.add(bug4)
enemy_sprites.add(bug5)
