import pygame
import sys
from pygame.locals import *
from cleaningSupply import *

class SprayBottle(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):

        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("spraybottle.png"), (tileW, tileH)), XMARG, YMARG, tileW, tileH)
        pygame.sprite.Sprite.__init__(self)
        self.name = 'spraybottle'
        self.cooldown = 480
        self.health = 10
        self.startcooldownframes = self.cooldown


#The sponge can absorb a lot of hits. It is equivalent to a Wall-nut. It has no abilities but has way more health than most plants.

class Sponge(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):
        pygame.sprite.Sprite.__init__(self)

        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("sponge.png"), (tileW, tileH)), XMARG, YMARG, tileW, tileH)
        self.name = 'sponge'
        self.health = 50



#spongeGroup.add(Sponge(0, 0))

#flypaper is a trap, equivalent to a potato mine. It will kill one bug instantly when it touches it but will then dissapear.

class Flypaper(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("flypaper.png"), (tileW, tileH)), XMARG, YMARG, tileW, tileH)
        self.name = 'flypaper'
        self.health = 10 # when flypaper is stepped on, it will explode


#flypaperGroup.add(Flypaper(0, 0))

#The soap dispenser dispenses suds, the currency of the game. It is equivalent to the sunflower.

class SoapDispenser(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("soapdispenser.png"), (tileW, tileH)), XMARG, YMARG, tileW, tileH)
        self.name = 'soapdispenser'

        self.cooldown = 2400 #15 seconds
        self.health = 10
        self.startcooldownframes = self.cooldown


class BowlCleaner(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):
        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("bowlcleaner.png"), (tileW, tileH)), XMARG, YMARG, tileW, tileH)
        self.name = 'bowlcleaner'

        self.cooldown = 2400 #15 seconds
        self.health = 20
        self.startcooldownframes = self.cooldown


