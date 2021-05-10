
from defaults import *


# spider should take 5 hits before its death


projectileGroup = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        scaleFactor = scaleFactorH
        if scaleFactorW < scaleFactorH:
            scaleFactor = scaleFactorW
        self.health = 5
        if(type == 'spraydroplet'):
            self.image = pygame.transform.scale(pygame.image.load("waterdroplet.png"), (50,50))
            self.type = "spraydroplet"
        #self.image = pygame.transform.rotate(self.image, 90)
        if(type == 'icedroplet'):
            self.type = "icedroplet"
            self.image = pygame.transform.scale(pygame.image.load("icedroplet.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        if(self.type == "spraydroplet"):
            self.rect.x += 25
        if(self.type == "icedroplet"):
            self.rect.x += 12
