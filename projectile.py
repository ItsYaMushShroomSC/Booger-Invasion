
from defaults import *


# spider should take 5 hits before its death


projectileGroup = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        scaleFactor = scaleFactorH
        if scaleFactorW < scaleFactorH:
            scaleFactor = scaleFactorW
        self.health = 5
        self.image = pygame.transform.scale(pygame.image.load("bullet.png"), (50,50))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += 10
        # if (self.rect.x <= (DISPLAYSURF.get_width()) / 4):
        #     self.rect.x += 10
        #     self.health = 0
        # if self.health == 0:
        #     self.kill()