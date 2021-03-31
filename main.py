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
XMARGIN = 200 * scaleFactorW
YMARGIN = 100 * scaleFactorH

 # Text Font:
fontSize = 54 * scaleFactorH
bugFont = pygame.font.Font('bugFont.ttf', fontSize)
cleaningFont = pygame.font.Font('CleaningSupplyFont.otf', fontSize)

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
floorGrid = [] # floor grid 2D array

# Classes Are in other .py files

# Non-Class Methods:

def formFloorGridArray():
    pass

def drawTiles():
    global floorGrid # 5 by 7 grid 5 height and 7 length
    scaleFactor = scaleFactorH
    if scaleFactorW < scaleFactorH:
        scaleFactor = scaleFactorW

    img1 = pygame.transform.smoothscale(pygame.image.load('Floor Tile-1.png.png'), (100 * scaleFactor, 121 * scaleFactor))
    img2 = pygame.transform.smoothscale(pygame.image.load('Floor Tile-2.png.png'), (100 * scaleFactor, 121 * scaleFactor))
    img = img1
    XMARGIN, YMARGIN = int((windowWidth-(100*scaleFactor * 9))/2), int((windowHeight-(121 * scaleFactor * 5))/2)
    left, top = XMARGIN, YMARGIN
    floorNum = 1

    for col in range(9):
        for row in range(5):
            if floorNum % 2 == 0:
                img = img2
            else:
                img = img1

            floorNum += 1
            imgRect = img.get_rect()
            imgRect.topleft = (left + col*100, top + row*121)
            DISPLAYSURF.blit(img, imgRect)

def drawBackground():

    img = pygame.transform.smoothscale(pygame.image.load('bugsWorldBackground.jpg').convert_alpha(),  (windowWidth, windowHeight))
    DISPLAYSURF.blit(img, (0, 0))
    drawTiles()

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
    textRect.midtop = (windowWidth / 2, windowHeight / 8 + (fontSize))
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level One', True, BLACK, RED) #LADYBUGS??
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))  # adds Classic snake rect at index 0
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize*2))
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Two', True, BLACK, GREEN)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))  # adds Accelerate snake rect at index 1
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize*4))
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Three', True, BLACK, LBLUE)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))  # adds 2P snake rect at index 2
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize*6))
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Four', True, BLACK, CYAN)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))  # adds Holiday snake rect at index 3
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize*8))
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Five', True, BLACK, PINK)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))  # adds Holiday snake rect at index 3
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize*10))
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

