import pygame
import sys
from pygame.locals import *
from cleaningSupply import *
import defaults

class SprayBottle(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):

        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("spraybottle.png"), (tileW, tileH)), XMARG, YMARG, tileW, tileH)

        self.name = 'spraybottle'
        self.cooldown = 3000  # 3 seconds
        self.health = 20
        self.timeElapsed = 0
        self.startcooldownframes = self.cooldown

        # should be called every 1 second that elapses
    def getShouldSpawnDroplet(
            self):  # returns boolean of whether it should spawn a droplet
        if self.timeElapsed >= self.cooldown:
            print("getShouldSpawnDroplet working")
            self.timeElapsed = 0
            return True, self.rect
        else:
            self.timeElapsed += 1000
            return False, None

class Droplet(pygame.sprite.Sprite):
    def __init__(self, shouldSpawn, cleaningSupplyRect):

        self.image = pygame.image.load('IMG_1711.PNG')
        w, h = 54 * defaults.scaleFactorH, 54 * defaults.scaleFactorH
        self.image = pygame.transform.smoothscale(pygame.image.load('IMG_1711.PNG'), (w, h))
        self.rect = self.image.get_rect()
        self.xpos = 0
       # self.setRandomPosCleaningSupply(cleaningSupplyRect)

        def getShouldRemove(self):  # updates and gets should the droplet be removed

            pass
            #if 
            #    return True
            #else:
            #    return False
        if(shouldSpawn == True):
            self.spawnDroplet(cleaningSupplyRect)


    def spawnDroplet(self, cleaningSupplyRect):
        print("spawnDroplet working")
        self.rect.center = cleaningSupplyRect.center
        self.rect.x += 12
        self.rect.y -= 25

    def update(self):
        self.rect.x += 20


#The sponge can absorb a lot of hits. It is equivalent to a Wall-nut. It has no abilities but has way more health than most plants.

class Sponge(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):

        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("sponge.png"), (tileW, tileH)), XMARG, YMARG, tileW, tileH)
        self.name = 'sponge'
        self.health = 50



#spongeGroup.add(Sponge(0, 0))

#flypaper is a trap, equivalent to a potato mine. It will kill one bug instantly when it touches it but will then dissapear.

class Flypaper(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):

        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("flypaper.png"), (tileW, tileH)), XMARG, YMARG, tileW, tileH)
        self.name = 'flypaper'
        self.health = 10 # when flypaper is stepped on, it will explode


#flypaperGroup.add(Flypaper(0, 0))

#The soap dispenser dispenses suds, the currency of the game. It is equivalent to the sunflower.

class SoapDispenser(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):
        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("soapdispenser.png"), (tileW, tileH)), XMARG, YMARG, tileW, tileH)
        self.name = 'soapdispenser'

        self.cooldown = 8000  # 8 seconds
        self.health = 10
        self.timeElapsed = 0
        self.startcooldownframes = self.cooldown

    # should be called every 1 second that elapses
    def getShouldSpawnBubble(
            self):  # returns boolean of whether shouldspawn bubble, and also the rect of the Soapdispenser
        if self.timeElapsed >= self.cooldown:
            self.timeElapsed = 0
            return True, self.rect
        else:
            self.timeElapsed += 1000
            return False, None


class BowlCleaner(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):
        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("bowlcleaner.png"), (tileW, tileH)), XMARG, YMARG, tileW, tileH)
        self.name = 'bowlcleaner'

        self.cooldown = 2400 #15 seconds
        self.health = 20
        self.startcooldownframes = self.cooldown


