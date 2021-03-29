# Authors: Sophia, Ayushi, Theo

# Imports:
import pygame
import sys
from pygame.locals import *

pygame.init()


#This is a test to see if I can do a pull request

# Global Variables:

 # Surface:
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Cleaning Supplies vs Bugs')


 # Constants:
windowWidth = DISPLAYSURF.get_width() # resized to fullscreen
windowHeight = DISPLAYSURF.get_height() # resized to fullscreen
scaleFactorW = int(windowWidth/1536)
scaleFactorH = int(windowHeight/864)

 # Text Font:
bugFont = pygame.font.Font('bugFont.ttf', 54*scaleFactorH)
cleaningFont = pygame.font.Font('CleaningSupplyFont.otf', 54 * scaleFactorH)

 # Time:
FPS = 160
FPSCLOCK = pygame.time.Clock()

 # Colors:
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (230,  47,  47)
GREEN = (  0, 102,   0)
LBLUE = (102, 102, 255)
CYAN  = (  0, 153, 153)
PINK  = (255, 153, 204)
 # Game variables:

gameLevel = 0 # 0 means that there is no game being played and the opening screen should be displayed
openScreenRects = []  # stores rectangles/buttons of the opening screen


# Classes Are in other .py files

# Non-Class Methods:

def drawBackground():

    img = pygame.transform.smoothscale(pygame.image.load('bugsWorldBackground.jpg').convert_alpha(),  (windowWidth, windowHeight))
    DISPLAYSURF.blit(img, (0, 0))

def determineLevel(mousePosX, mousePosY):
    global openScreenRects

    if openScreenRects[0].collidepoint(mousePosX, mousePosY):
        return 1
    elif openScreenRects[1].collidepoint(mousePosX, mousePosY):
        return 2
    elif openScreenRects[2].collidepoint(mousePosX, mousePosY):
        return 3
    elif openScreenRects[3].collidepoint(mousePosX, mousePosY):
        return 4
    elif openScreenRects[4].collidepoint(mousePosX, mousePosY):
        return 5
    else:
        return 0

def drawOpeningScreen():
    global openScreenRects

    DISPLAYSURF.fill(WHITE)

    textSurface = cleaningFont.render('Cleaning Supplies Vs. Bugs:', True, WHITE, BLACK)
    textRect = textSurface.get_rect()
    textRect.midtop = (windowWidth / 2, windowHeight / 7)
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level One', True, BLACK, RED) #LADYBUGS??
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))  # adds Classic snake rect at index 0
    textRect.midtop = (windowWidth / 2, 2 * windowHeight / 7)
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Two', True, BLACK, GREEN)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))  # adds Accelerate snake rect at index 1
    textRect.midtop = (windowWidth / 2, 3 * windowHeight / 7)
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Three', True, BLACK, LBLUE)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))  # adds 2P snake rect at index 2
    textRect.midtop = (windowWidth / 2, 4 * windowHeight / 7)
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Four', True, BLACK, CYAN)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))  # adds Holiday snake rect at index 3
    textRect.midtop = (windowWidth / 2, 5 * windowHeight / 7)
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Five', True, BLACK, PINK)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))  # adds Holiday snake rect at index 3
    textRect.midtop = (windowWidth / 2, 6 * windowHeight / 7)
    DISPLAYSURF.blit(textSurface, textRect)



def resetVariables():
    pass

def terminate(): # terminates game
   pygame.quit()
   sys.exit()

def main():
    global DISPLAYSURF, gameLevel

    clicked = False

    while True:
        for event in pygame.event.get():

            posX, posY = pygame.mouse.get_pos()

            if event.type == MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False

            if gameLevel == 0:
                drawOpeningScreen()
                if clicked:
                    gameLevel = determineLevel(posX, posY)

            if gameLevel == 1:
                drawBackground()

            if gameLevel == 2:
                drawBackground()

            if gameLevel == 3:
                drawBackground()

            if gameLevel == 4:
                drawBackground()

            if gameLevel == 5:
                drawBackground()

            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# RUN MAIN

if __name__ == '__main__':
   main()


# TESTS

