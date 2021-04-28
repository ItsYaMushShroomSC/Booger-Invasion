import pygame
import sys
from pygame.locals import *
import defaults
from cleaningSupply import *

cleaningSupplyGroup = pygame.sprite.Group()


class SprayBottle(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):

        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("spraybottle.png"), (tileW-2, tileH-2)), XMARG, YMARG, tileW, tileH)

        self.name = 'spraybottle'
        self.cooldown = 480
        self.health = 7
        self.damage = 1
        self.startcooldownframes = self.cooldown

    def updateHealth(self, bugDamage, DISPLAYSURF):
        self.health -= bugDamage

        font = pygame.font.Font('cloudBubbleFont.ttf', 32 * defaults.scaleFactorH)
        textSurface = font.render('-' + str(bugDamage), True, defaults.RED)
        textRect = textSurface.get_rect()
        textRect.midright = self.rect.midright
        left, top = textRect.topleft
        DISPLAYSURF.blit(textSurface, (left, top))
        pygame.display.update()


#The sponge can absorb a lot of hits. It is equivalent to a Wall-nut. It has no abilities but has way more health than most plants.

class Sponge(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):

        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("sponge.png"), (tileW-2, tileH-2)), XMARG, YMARG, tileW, tileH)
        self.name = 'sponge'
        self.health = 30

    def updateHealth(self, bugDamage, DISPLAYSURF):
        self.health -= bugDamage

        font = pygame.font.Font('cloudBubbleFont.ttf', 32 * defaults.scaleFactorH)
        textSurface = font.render('-' + str(bugDamage), True, defaults.RED)
        textRect = textSurface.get_rect()
        textRect.midright = self.rect.midright
        left, top = textRect.topleft
        DISPLAYSURF.blit(textSurface, (left, top))
        pygame.display.update()

#spongeGroup.add(Sponge(0, 0))

#flypaper is a trap, equivalent to a potato mine. It will kill one bug instantly when it touches it but will then dissapear.

class Flypaper(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):

        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("flypaper.png"), (tileW-2, tileH-2)), XMARG, YMARG, tileW, tileH)
        self.name = 'flypaper'
        self.health = 1 # when flypaper is stepped on, it will explode
        self.explode = False
        self.shouldRemove = False
        self.tileW, self.tileH = tileW, tileH

    def updateHealth(self, bugDamage, DISPLAYSURF):
        self.health -= bugDamage

        font = pygame.font.Font('cloudBubbleFont.ttf', 32 * defaults.scaleFactorH)
        textSurface = font.render('-' + str(bugDamage), True, defaults.RED)
        textRect = textSurface.get_rect()
        textRect.midright = self.rect.midright
        left, top = textRect.topleft
        DISPLAYSURF.blit(textSurface, (left, top))
        pygame.display.update()

        if self.explode == True:
            self.shouldRemove = True

        if self.health <= 0:
            self.explode = True
            self.image = pygame.transform.smoothscale(pygame.image.load('explosionimg.PNG'), (self.tileW-2, self.tileH-2))


#flypaperGroup.add(Flypaper(0, 0))

#The soap dispenser dispenses suds, the currency of the game. It is equivalent to the sunflower.

class SoapDispenser(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):
        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("soapdispenser.png"), (tileW-2, tileH-2)), XMARG, YMARG, tileW, tileH)
        self.name = 'soapdispenser'

        self.cooldown = 8000 #8 seconds
        self.health = 7
        self.timeElapsed = 0
        self.startcooldownframes = self.cooldown

    def updateHealth(self, bugDamage, DISPLAYSURF):
        self.health -= bugDamage

        font = pygame.font.Font('cloudBubbleFont.ttf', 32 * defaults.scaleFactorH)
        textSurface = font.render('-' + str(bugDamage), True, defaults.RED)
        textRect = textSurface.get_rect()
        textRect.midright = self.rect.midright
        left, top = textRect.topleft
        DISPLAYSURF.blit(textSurface, (left, top))
        pygame.display.update()

    # should be called every 1 second that elapses
    def getShouldSpawnBubble(self): # returns boolean of whether shouldspawn bubble, and also the rect of the Soapdispenser
        if self.timeElapsed >= self.cooldown:
            self.timeElapsed = 0
            return True, self.rect
        else:
            self.timeElapsed += 1000
            return False, None


class BowlCleaner(CleaningSupply):

    def __init__(self, row, column, XMARG, YMARG, tileW, tileH):
        super().__init__(row, column, pygame.transform.smoothscale(pygame.image.load("bowlcleaner.png"), (tileW-2, tileH-2)), XMARG, YMARG, tileW, tileH)
        self.name = 'bowlcleaner'

        self.cooldown = 2400 #15 seconds
        self.health = 7
        self.startcooldownframes = self.cooldown

    def updateHealth(self, bugDamage, DISPLAYSURF):
        self.health -= bugDamage

        font = pygame.font.Font('cloudBubbleFont.ttf', 32 * defaults.scaleFactorH)
        textSurface = font.render('-' + str(bugDamage), True, defaults.RED)
        textRect = textSurface.get_rect()
        textRect.midright = self.rect.midright
        left, top = textRect.topleft
        DISPLAYSURF.blit(textSurface, (left, top))
        pygame.display.update()
