# Authors: Sophia, Ayushi, Theo

# Imports:
import pygame
from pygame.locals import *
import sys
#import cleaningSupply
from bug import *
from cleaningSupply import *
import time
from pygame.locals import *

from cleaningSupplies import *
from cleaningSupplySeed import *

pygame.init()

# This is a test to see if I can do a pull request

# Global Variables:

# Surface:
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Cleaning Supplies vs Bugs')

# Constants:
windowWidth = DISPLAYSURF.get_width()  # resized to fullscreen
windowHeight = DISPLAYSURF.get_height()  # resized to fullscreen
scaleFactorW = int(windowWidth / 1536) * int(windowWidth/1536)
scaleFactorH = int(windowHeight / 864) * int(windowHeight/864)
XMARGIN = 200 * scaleFactorW
YMARGIN = 100 * scaleFactorH

# Text Font:
fontSize = 54 * scaleFactorH
bugFont = pygame.font.Font('bugFont.ttf', fontSize)
cleaningFont = pygame.font.Font('CleaningSupplyFont.otf', fontSize)

# Time:
frames = 0
FPS = 160
FPSCLOCK = pygame.time.Clock()

# Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 47, 47)
GREEN = (0, 102, 0)
LBLUE = (102, 102, 255)
CYAN = (0, 153, 153)
PINK = (255, 153, 204)

# Game variables:

gameLevel = 0  # 0 means that there is no game being played and the opening screen should be displayed
openScreenRects = []  # stores rectangles/buttons of the opening screen

floorGrid = []  # floor grid 2D array
tileWidth = None
tileHeight = None

bugEnterAry = []
bugEnterIndex = 0

# dictionary where (key: <name of cleaningsupply>, value: tuple(<order>, <price>))
# @see https://www.w3schools.com/python/python_dictionaries.asp
seedDict = {1: ("spraybottle", 100, 5000), 2: ("sponge", 50, 8000), 3: ("soapdispenser", 50, 5000), 4: ("flypaper", 10000, 25)}

# Sprite Groups:
cleaningSupplyGroup = pygame.sprite.Group()
cleaningSupplyBackGrounds = pygame.sprite.Group()
cleaningSupplySeedsGroup = pygame.sprite.Group()

# Classes Are in other .py files


# Non-Class Methods:

# the dictionary will be read and the appropriate img will be

def getBugsEntering(timeElapsed): # adds the bugs entering the screen
    # timeElapsed is seconds from since the game started
    global bugEnterIndex

    print(str(len(bugEnterAry)))
    index = 0
    for i in range(len(bugEnterAry)):
        bug = str(bugEnterAry[i][0])
        time = int(bugEnterAry[i][1]) * 1000
        print(bug)

        if timeElapsed >= time and bugEnterIndex <= index:
            print('woo')
            bugEnterIndex += 1
            buggy = getBugRandomPos(bug)

            if not buggy == None:
                enemy_sprites.add(buggy)

        index += 1


def readFile(): # opens txt note and adds letters to gameAry which is '2D'
    global bugEnterAry
    bugEnterAry.clear()
    if gameLevel == 1:
        level1 = open('Level1BugTimes.txt')
        for line in level1:
            bugEnterAry.append(line.rstrip().split(' '))

def getBugRandomPos(bugName):
    choices = [DISPLAYSURF.get_height() / 2, DISPLAYSURF.get_height() / 2 - 121, DISPLAYSURF.get_height() / 2 - 242,
               DISPLAYSURF.get_height() / 2 + 121, DISPLAYSURF.get_height() / 2 + 242]

    x = 3 * DISPLAYSURF.get_width() / 4
    y = random.choice(choices)

    if bugName == 'spider':
        return Spider(x, y)
    if bugName == 'cockroach':
        return Cockroach(x, y)




def addCleaningSupplySeeds():
    global cleaningSupplySeedsGroup

    img = pygame.image.load('SeedPacketBackground.png')
    w, h = img.get_width()*scaleFactorH, img.get_height()*scaleFactorH
    img = pygame.transform.smoothscale(img, (w, h))

    indexOrder = 1

    for i in range(1, 10):
        cleaningSupplyBackGrounds.add_internal(CleaningSupplySeed(img, 'bg', 1, i, 1, XMARGIN, windowWidth, windowHeight))

    for order, values in seedDict.items():
        name, price, restockTime = values
        img = pygame.transform.smoothscale(getImg(name), (w, h))
        cleaningSupplySeedsGroup.add_internal(CleaningSupplySeed(img, name, price, order, restockTime, XMARGIN, windowWidth, windowHeight))

def getImg(name):

    if name == "spraybottle":
        return pygame.image.load('spraybottle.PNG')
    if name == "sponge":
        return pygame.image.load('sponge.PNG')
    if name == "soapdispenser":
        return pygame.image.load('soapdispenser.PNG')
    if name == "flypaper":
        return pygame.image.load('flypaper.PNG')

def addCleaningSupply(posX, posY, name):
    if name == "spraybottle":
        cs = SprayBottle(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "sponge":
        cs = Sponge(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "soapdispenser":
        cs = SoapDispenser(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "flypaper":
        cs = Flypaper(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        setTile(posX, posY, cs)

def getTile(x, y):  # (0, 0) is the top left tile
    return floorGrid[y][x]


def setTile(x, y, cleaningSupplyType):  # the tile in that position is set as cleaningSupplyType (0,0) is top left tile
    floorGrid[y][x] = cleaningSupplyType


def formFloorGridArray():  # Fills all places in FloorGridArray with None
    global floorGrid

    row = 5
    col = 9
    floorGrid = [[None] * row for i in range(col)]


def drawTiles(shouldDraw):
    global floorGrid, tileHeight, tileWidth, XMARGIN, YMARGIN  # 5 by 9 grid 5 height and 9 length
    scaleFactor = scaleFactorH
    if scaleFactorW < scaleFactorH:
        scaleFactor = scaleFactorW

    img1 = pygame.transform.smoothscale(pygame.image.load('Floor Tile-1.png.png'),
                                        (100 * scaleFactor, 121 * scaleFactor))
    img2 = pygame.transform.smoothscale(pygame.image.load('Floor Tile-2.png.png'),
                                        (100 * scaleFactor, 121 * scaleFactor))
    img = img1
    tileWidth, tileHeight = (100 * scaleFactor), (121 * scaleFactor)
    XMARGIN, YMARGIN = int((windowWidth - (100 * scaleFactor * 9)) / 2), int(
        (windowHeight - (121 * scaleFactor * 5)) / 2)
    left, top = XMARGIN, YMARGIN
    floorNum = 1

    if shouldDraw == True:
        for col in range(9):
            for row in range(5):
                if floorNum % 2 == 0:
                    img = img2
                else:
                    img = img1

                floorNum += 1
                imgRect = img.get_rect()
                imgRect.topleft = (left + col * 100, top + row * 121)
                DISPLAYSURF.blit(img, imgRect)


def drawBackground():
    img = pygame.transform.smoothscale(pygame.image.load('bugsWorldBackground.jpg').convert_alpha(),
                                       (windowWidth, windowHeight))
    DISPLAYSURF.blit(img, (0, 0))
    drawTiles(True)


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
    textSurface = bugFont.render('Level One', True, BLACK, RED)  # LADYBUGS??
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize * 2))
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Two', True, BLACK, GREEN)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize * 4))
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Three', True, BLACK, LBLUE)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize * 6))
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Four', True, BLACK, CYAN)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize * 8))
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Level Five', True, BLACK, PINK)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize * 10))
    DISPLAYSURF.blit(textSurface, textRect)


def resetVariables():
    formFloorGridArray()
    drawTiles(False)

def terminate():  # terminates game
    pygame.quit()
    sys.exit()


curr_time = 0
def mainGame():
    global DISPLAYSURF, gameLevel, frames, curr_time, bugEnterAry

    clicked = False

    resetVariables()

    my_eventTime = USEREVENT + 1
    pygame.time.set_timer(my_eventTime, 150)

    addCleaningSupply(0, 0, "spraybottle")
    addCleaningSupply(0, 1, "sponge")
    addCleaningSupply(0, 2, "soapdispenser")
    addCleaningSupply(0, 3, "flypaper")
    addCleaningSupplySeeds()

    timeSinceStart = 0
    curr_time = pygame.time.get_ticks()

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
                readFile()

                if curr_time + 1000 > pygame.time.get_ticks(): # every 1 second that passes this will happen
                    curr_time = pygame.time.get_ticks()
                    timeSinceStart += 1000
                    getBugsEntering(timeSinceStart)
                    #print('hi')

                if event.type == my_eventTime:
                    drawBackground()

                    enemy_sprites.draw(DISPLAYSURF)
                    enemy_sprites.update()

                    #addCleaningSupplySeeds()
                    cleaningSupplyBackGrounds.draw(DISPLAYSURF)
                    cleaningSupplySeedsGroup.draw(DISPLAYSURF)
                    #addCleaningSupply(0, 0, "spraybottle")
                    cleaningSupplyGroup.draw(DISPLAYSURF)
                    cleaningSupplyGroup.draw(DISPLAYSURF)
                    #printFloorGridAry()
                    #moveAll()
                    #all_sprites.draw(DISPLAYSURF)
                    #all_sprites.update()
                    #print(str(windowWidth))
                    #print(str(windowHeight))

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

        frames = frames + 1

        pygame.display.update()
        # all_sprites.update()
        FPSCLOCK.tick(FPS)


# TESTS
def printFloorGridAry():  # Print the floor grid array contents whenever you want to see it
    for row in range(5):
        for col in range(9):
            print(str(floorGrid[col][row]) + " ", end='')
        print()


# RUN MAIN

if __name__ == '__main__':
    mainGame()
