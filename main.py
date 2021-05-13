# Authors: Sophia, Ayushi, Theo

# Imports:
import pygame
from pygame.locals import *
import sys
#import cleaningSupply
from bug import *
from supremeBug import *
from cleaningSupply import *
import time
from pygame.locals import *
from defaults import *
from cleaningSupplies import *
from cleaningSupplySeed import *
from bubbleMoney import *
from projectile import *

pygame.init()

# This is a test to see if I can do a pull request

# Global Variables:

# Surface:
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Cleaning Supplies vs Bugs')

# Constants:
windowWidth = DISPLAYSURF.get_width()  # resized to fullscreen
windowHeight = DISPLAYSURF.get_height()  # resized to fullscreen
scaleFactorW = int(windowWidth / 1536)
scaleFactorH = int(windowHeight / 864)
XMARGIN = 200 * scaleFactorW
YMARGIN = 100 * scaleFactorH

# Text Font:
fontSize1 = 54 * scaleFactorH
bugFont = pygame.font.Font('bugFont.ttf', fontSize1)
cleaningFont = pygame.font.Font('CleaningSupplyFont.otf', fontSize1)
bubbleFont = pygame.font.Font('cloudBubbleFont.ttf', fontSize1)
enterFont = pygame.font.Font('EnterFont.ttf', fontSize1)

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

floorGrid = []  # floor grid 2D array stores the cleaning supply name at each position, None if there isn't one
floorGridRects = [] # stores the rectangles of the tiles in the floorGrid

tileWidth = None
tileHeight = None

bugEnterAry = []
bugEnterIndex = 0

gameMessageOn = False
currMessage = None

logNum = 1
winTimeCount = 0
nearEnd = False

# dictionary where (key: <name of cleaningsupply>, value: tuple(<order>, <price>))
# @see https://www.w3schools.com/python/python_dictionaries.asp



seedDictGroup1 = {1: ("spraybottle", 100, 5000), 2: ("sponge", 50, 8000),
            3: ("soapdispenser", 50, 5000), 4: ('toiletplunger', 150, 9000)}

seedDictGroup2 = {1: ("doublesoapdispenser", 150, 8000), 2: ("doublespraybottle", 200, 5000), 3: ("thiccsponge", 300, 12000),
                  4: ('toiletplunger', 150, 9000), 5: ("flypaper", 25, 10000), 6: ("acidpool", 150, 12000)}

seedDictGroup3 = {1: ("icebottle", 200, 8000), 2: ("thiccsponge", 300, 12000),
            3: ("doublesoapdispenser", 150, 8000), 4: ("flypaper", 25, 10000),
            5: ("doublespraybottle", 200, 5000), 6: ('toiletplunger', 150, 9000),
            7: ("bleach", 350, 10000), 8:("broom", 50, 9000), 9: ("acidpool", 150, 12000)}

currSeedDictGroup = seedDictGroup1

seedInventoryRects = [] # seed rects for mouse collision

# Sprite Groups:
cleaningSupplyBackGrounds = pygame.sprite.Group()
cleaningSupplySeedsGroup = pygame.sprite.Group()

# Money currency
bubbleCoins = 0
bubbleCoinGroup = pygame.sprite.Group()

# Classes Are in other .py files


# Non-Class Methods:

# the dictionary will be read and the appropriate img will be

def activateBleach():
    for cleaningSupply in cleaningSupplyGroup:
        for bug in enemy_sprites:
            if cleaningSupply.name == "bleach":
                for bug in enemy_sprites:
                    if(bug.row == cleaningSupply.y) and not bug.name == 'giantbug':
                        print("bleach")
                        bug.health = 0
                cleaningSupply.health = 0

def gameMessage(message):
    global gameLevel, bubbleFont, gameMessageOn, currMessage

    textSurface = enterFont.render(message, True, BLACK, GREEN)
    textRect = textSurface.get_rect()
    textRect.center = (windowWidth/2, windowHeight/2)
    left, top = textRect.topleft
    DISPLAYSURF.blit(textSurface, (left, top))

def activatePlungers():
    for cleaningSupply in cleaningSupplyGroup:
        for bug in enemy_sprites:

            tempRect = cleaningSupply.rect

            if cleaningSupply.name == 'toiletplunger':

                if cleaningSupply.targetRect.colliderect(bug.rect) or pygame.sprite.collide_mask(cleaningSupply, bug):

                    cleaningSupply.hasTarget = True
                    cleaningSupply.updateHealth(bug)

                cleaningSupply.rect = cleaningSupply.targetRect


            if cleaningSupply.name == 'toiletplunger' and not pygame.sprite.spritecollideany(cleaningSupply, enemy_sprites):
                cleaningSupply.becomeUpright()
                cleaningSupply.hasTarget = False

            cleaningSupply.rect = tempRect


def removeDeadSprites():
    for cleaningSupply in cleaningSupplyGroup:
        if cleaningSupply.health <= 0 and not cleaningSupply.name == 'flypaper':
            setTile(cleaningSupply.x, cleaningSupply.y, None)
            cleaningSupplyGroup.remove_internal(cleaningSupply)
            notAcidPoolGroup.remove_internal(cleaningSupply)

    for bug in enemy_sprites:
        if bug.health <= 0:
            enemy_sprites.remove_internal(bug)




def sendDamage(): # every 1 second senddamage should be caleld and damages the cs by the bugs, and removes dead ones

    for cleaningSupply in cleaningSupplyGroup:
        for bug in enemy_sprites:
            if pygame.sprite.collide_mask(cleaningSupply, bug) and bug.frozen == True:
                if not cleaningSupply.name == 'toiletplunger' and not cleaningSupply.name == 'acidpool' and not cleaningSupply.name == 'broom':
                    cleaningSupply.updateHealth(bug.damage, DISPLAYSURF)

            if cleaningSupply.name == 'flypaper' and cleaningSupply.shouldRemove == True and pygame.sprite.collide_mask(cleaningSupply, bug):
                enemy_sprites.remove_internal(bug)

            if cleaningSupply.name == 'acidpool' and pygame.sprite.collide_mask(cleaningSupply, bug):
                cleaningSupply.damageBugOnAcid(DISPLAYSURF, bug)

            if cleaningSupply.name == 'broom' and pygame.sprite.collide_mask(cleaningSupply, bug):
                cleaningSupply.updateHealth(DISPLAYSURF, bug)

        if cleaningSupply.health <= 0 and not cleaningSupply.name == 'flypaper':
            setTile(cleaningSupply.x, cleaningSupply.y, None)
            cleaningSupplyGroup.remove_internal(cleaningSupply)
            notAcidPoolGroup.remove_internal(cleaningSupply)


        if cleaningSupply.name == 'flypaper' and cleaningSupply.shouldRemove:
            setTile(cleaningSupply.x, cleaningSupply.y, None)
            cleaningSupplyGroup.remove_internal(cleaningSupply)
            notAcidPoolGroup.remove_internal(cleaningSupply)


def checkBugCleaningSupplyCollision():

    for cleaningSupply in cleaningSupplyGroup:
        for bug in enemy_sprites:

            if pygame.sprite.collide_mask(cleaningSupply, bug) and not cleaningSupply.name == 'acidpool':
                bug.frozen = True

                if cleaningSupply.name == 'toiletplunger':

                    if cleaningSupply.uprightRect.colliderect(bug.rect):
                        bug.frozen = True
                        bug.damageCS(cleaningSupply)
                        cleaningSupply.drawAttack(bug.damage, DISPLAYSURF)
                    else:
                        bug.frozen = False

            if not pygame.sprite.spritecollideany(bug, cleaningSupplyGroup):
                bug.frozen = False

            if not pygame.sprite.spritecollideany(bug, notAcidPoolGroup) and pygame.sprite.spritecollideany(bug, acidPoolGroup):
                bug.frozen = False

    if len(cleaningSupplyGroup) == 0:
        for bug in enemy_sprites:
            bug.frozen = False


def updateSoapDispenserBubbles():# should be called every second

    for cleaningSupply in cleaningSupplyGroup:

        if cleaningSupply.name == 'soapdispenser':
            shouldSpawn, rect = cleaningSupply.getShouldSpawnBubble()

            if shouldSpawn == True:
                bubbleCoinGroup.add_internal(Bubble(True, rect, False))

        if cleaningSupply.name == 'doublesoapdispenser':
            shouldSpawn, rect = cleaningSupply.getShouldSpawnBubble()

            if shouldSpawn == True:
                bubbleCoinGroup.add_internal(Bubble(True, rect, True))

def removeClickedBubbles(mouseX, mouseY):
    global bubbleCoins

    for coin in bubbleCoinGroup:
        if coin.rect.collidepoint((mouseX, mouseY)) == True and coin.isDouble == False:
            bubbleCoinGroup.remove_internal(coin)
            bubbleCoins += 50
        if coin.rect.collidepoint((mouseX, mouseY)) == True and coin.isDouble == True:
            bubbleCoinGroup.remove_internal(coin)
            bubbleCoins += 100


def removeExpiredBubbles():
    global bubbleCoins

    for coin in bubbleCoinGroup:
        if coin.getShouldRemove() == True and coin.isDouble == False:
            bubbleCoinGroup.remove_internal(coin)
            bubbleCoins += 50
        if coin.getShouldRemove() == True and coin.isDouble == True:
            bubbleCoinGroup.remove_internal(coin)
            bubbleCoins += 100





def addBubbleCoin(isCleaningSupplyBubble):
    global bubbleCoinGroup

    bubbleCoinGroup.add_internal(Bubble(isCleaningSupplyBubble, None, False))

def drawSeedLoadingBars(timeElapsed):
    for supplySeed in cleaningSupplySeedsGroup:
            supplySeed.updateLoadingBar(timeElapsed, DISPLAYSURF)

def addSelectedCleaningSupply(dictKey, seedSelected, posX, posY):
    global bubbleCoins
    counter = 0

    if not dictKey == 0 and not seedSelected == None:
        supplySeed = getCleaningSupplySeed(dictKey)

        if bubbleCoins >= supplySeed.price:

            for row in range(5):
                for col in range(9):

                    if floorGridRects[col][row].collidepoint((posX, posY)) and floorGrid[col][row] == None and supplySeed.inStock:
                        #print(str(col))
                        #print(str(row))
                        supplySeed.resetRestockTime()
                        bubbleCoins -= supplySeed.price
                        addCleaningSupply(col, row, seedSelected)
                        return None

    return seedSelected


def getSeedSelected(mouseX, mouseY, seedSelected, dictIndex): # seedSelected is None when it wasn't set yet
    index = 1
    price = None

    for seedInventoryRect in seedInventoryRects:

        if seedInventoryRect.collidepoint((mouseX, mouseY)):
            values = currSeedDictGroup.get(index)
            seedSelected, price, noOneCares = values
            dictIndex = index

        index += 1

    return dictIndex, seedSelected # seedSelected and price return None when no seedpackets were selected


def getBugsEntering(timeElapsed): # adds the bugs entering the screen
    # timeElapsed is seconds from since the game started
    global bugEnterIndex, gameMessageOn, currMessage, nearEnd, winTimeCount

    index = 0

    if nearEnd == True and len(enemy_sprites) == 0:
        gameMessageOn = True
        currMessage = 'Winner'
        winTimeCount += 1
    if winTimeCount >= 3:
        terminate()

    for i in range(len(bugEnterAry)):
        bug = str(bugEnterAry[i][0])
        time = int(bugEnterAry[i][1]) * 1000

        if timeElapsed >= time and bugEnterIndex <= index:
            bugEnterIndex += 1
            buggy = getBugRandomPos(bug)


            if not buggy == None:
                enemy_sprites.add_internal(buggy)
            if bug == 'near_end':
                nearEnd = True
            if buggy == None and not bug == 'near_end':
                gameMessageOn = True
                currMessage = bug

        index += 1


def readFile(): # opens txt note and adds letters to gameAry which is '2D'
    global bugEnterAry
    bugEnterAry.clear()
    if gameLevel == 1:
        level1 = open('Level1BugTimes.txt')
        for line in level1:
            bugEnterAry.append(line.rstrip().split(' '))
    if gameLevel == 2:
        level2 = open('Level2BugTimes.txt')
        for line in level2:
            bugEnterAry.append(line.rstrip().split(' '))
    if gameLevel == 3:
        level3 = open('Level3BugTimes.txt')
        for line in level3:
            bugEnterAry.append(line.rstrip().split(' '))

def getBugRandomPos(bugName):
    choices = [DISPLAYSURF.get_height() / 2, DISPLAYSURF.get_height() / 2 - 121, DISPLAYSURF.get_height() / 2 - 242,
               DISPLAYSURF.get_height() / 2 + 121, DISPLAYSURF.get_height() / 2 + 242]

    x = 3 * DISPLAYSURF.get_width() / 4
    y = random.choice(choices)

    if y == DISPLAYSURF.get_height() / 2:
        row = 2
    if y == DISPLAYSURF.get_height() / 2 - 121:
        row = 1
    if y == DISPLAYSURF.get_height() / 2 - 242:
        row = 0
    if y == DISPLAYSURF.get_height() / 2 + 121:
        row = 3
    if y == DISPLAYSURF.get_height() / 2 + 242:
        row = 4

    if bugName == 'spider':
        return Spider(x, y, row)
    if bugName == 'wasp':
        return Wasp(x, y, row)
    if bugName == 'cockroach':
        return Cockroach(x, y, row)
    if bugName == 'ant':
        return Ant(x, y, row)
    if bugName == 'ladybug':
        return LadyBug(x, y, row)
    if bugName == 'giant':
        return GiantBug(x, DISPLAYSURF.get_height()/2, row)



def getCleaningSupplySeed(index):
    counter = 1
    for supplySeed in cleaningSupplySeedsGroup:
        if counter == index:
            return supplySeed
        counter += 1

    return None

def addCleaningSupplySeeds():
    global cleaningSupplySeedsGroup, currSeedDictGroup

    img = pygame.image.load('SeedPacketBackground.png')
    w, h = img.get_width()*scaleFactorH, img.get_height()*scaleFactorH
    img = pygame.transform.smoothscale(img, (w, h))

    indexOrder = 1

    for i in range(1, 10):

        if len(currSeedDictGroup) >= i:
            name, price, reloadTime = currSeedDictGroup.get(i)
            img = pygame.image.load('SeedPacketBackground' + str(price) + '.png')

            w, h = img.get_width() * scaleFactorH, img.get_height() * scaleFactorH
            img = pygame.transform.smoothscale(img, (w, h))

        if len(currSeedDictGroup) < i:
            #name, price, reloadTime = currSeedDictGroup.get(i)
            img = pygame.image.load('SeedPacketBackground.png')

            w, h = img.get_width() * scaleFactorH, img.get_height() * scaleFactorH
            img = pygame.transform.smoothscale(img, (w, h))

        cleaningSupplyBackGrounds.add_internal(CleaningSupplySeed(img, 'bg', 1, i, 1, XMARGIN, windowWidth, windowHeight, True))

    for order, values in currSeedDictGroup.items():
        name, price, restockTime = values
        img = pygame.transform.smoothscale(getImg(name), (w, h))
        supplySeed = CleaningSupplySeed(img, name, price, order, restockTime, XMARGIN, windowWidth, windowHeight, False)
        cleaningSupplySeedsGroup.add_internal(supplySeed)
        seedInventoryRects.append(supplySeed.flashRect)

def getImg(name):

    if name == "spraybottle":
        return pygame.image.load('spraybottle.PNG')
    if name == 'doublespraybottle':
        return pygame.image.load('doublespraybottle.PNG')
    if name == "sponge":
        return pygame.image.load('sponge.PNG')
    if name == "thiccsponge":
        return pygame.image.load('doublesponge.PNG')
    if name == "soapdispenser":
        return pygame.image.load('soapdispenser.PNG')
    if name == "doublesoapdispenser":
        return pygame.image.load('douplesoapdispenser.PNG')
    if name == "flypaper":
        return pygame.image.load('flypaper.PNG')
    if name == "bowlcleaner":
        return pygame.image.load('bowlcleaner.png')
    if name == "toiletplunger":
        return pygame.image.load('PlungerUpright.png.png')
    if name == "icebottle":
        return pygame.image.load('icespraybottle.PNG')
    if name == "acidpool":
        return pygame.image.load('acidpool.PNG')
    if name == "broom":
        return pygame.image.load('Broom.png')
    if name == "bleach":
        return pygame.image.load('bleach.png')



#adds cleaning supplies to the 2Darray field
def addCleaningSupply(posX, posY, name):
    if name == "spraybottle":
        cs = SprayBottle(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "doublespraybottle":
        cs = SprayBottlex2(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "sponge":
        cs = Sponge(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "thiccsponge":
        cs = ThiccSponge(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "soapdispenser":
        cs = SoapDispenser(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "doublesoapdispenser":
        cs = DoubleSoapDispenser(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "flypaper":
        cs = Flypaper(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "bowlcleaner":
        cs = BowlCleaner(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "toiletplunger":
        cs = ToiletPlunger(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "icebottle":
        cs = IceBottle(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "acidpool":
        cs = AcidPool(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        acidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "broom":
        cs = Broom(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)
    if name == "bleach":
        cs = Bleach(posX, posY, XMARGIN, YMARGIN, tileWidth, tileHeight)
        cleaningSupplyGroup.add_internal(cs)
        notAcidPoolGroup.add_internal(cs)
        setTile(posX, posY, cs)

def getTileRect(col, row):
    return floorGridRects[col][row]

def getTile(col, row):  # (0, 0) is the top left tile
    return floorGrid[col][row]


def setTile(col, row, cleaningSupplyType):  # the tile in that position is set as cleaningSupplyType (0,0) is top left tile
    floorGrid[col][row] = cleaningSupplyType

def formFloorGridRectsArray():
    global floorGridRects

    row = 5
    col = 9
    floorGridRects = [[None] * row for i in range(col)]

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

    for row in range(5):
        for col in range(9):
            if floorNum % 2 == 0:
                img = img2
            else:
                img = img1

            floorNum += 1
            imgRect = img.get_rect()
            imgRect.topleft = (left + col * 100, top + row * 121)
            if shouldDraw == True:
                DISPLAYSURF.blit(img, imgRect)

            floorGridRects[col][row] = imgRect

#generates projectile every 5 seconds
def proj(time):
    print(f'{time} o')
    for supply in cleaningSupplyGroup:

        if (time / 1000 ) % 3 == 0 and supply.name == "spraybottle" :

            projectileGroup.add(createProjectile(supply.rect.centerx, supply.rect.centery, 'spraydroplet'))

        if (time / 1000) % 3 == 0 and supply.name == "doublespraybottle":
            projectileGroup.add(createProjectile(supply.rect.centerx, supply.rect.centery, 'spraydroplet'))
            projectileGroup.add(createProjectile(supply.rect.centerx + 50, supply.rect.centery, 'spraydroplet'))

        if (time / 1000 ) % 3 == 0 and supply.name == "icebottle" :

            projectileGroup.add(createProjectile(supply.rect.centerx, supply.rect.centery, 'icedroplet'))


def createProjectile(mx,my,type):
    if(type=="spraydroplet"):
        bullet = Bullet(mx + 18, my - 33, "spraydroplet")
    if (type == "icedroplet"):
            bullet = Bullet(mx + 18, my - 33, "icedroplet")

    return bullet


def drawBackButton():
    global bubbleFont

    textSurface = bubbleFont.render('BACk bAbY', True, BLACK, WHITE)
    textRect = textSurface.get_rect()
    textRect.bottomright = (windowWidth, windowHeight)
    left, top = textRect.topleft
    DISPLAYSURF.blit(textSurface, (left, top))
    return textRect

def drawNextButton():
    global bubbleFont

    textSurface = bubbleFont.render('NeXT bAbY', True, BLACK, WHITE)
    textRect = textSurface.get_rect()
    textRect.bottomleft = (0, windowHeight)
    left, top = textRect.topleft
    DISPLAYSURF.blit(textSurface, (left, top))
    return textRect

def drawBackground():
    img = pygame.transform.smoothscale(pygame.image.load('bugsWorldBackground.jpg').convert_alpha(),
                                       (windowWidth, windowHeight))
    DISPLAYSURF.blit(img, (0, 0))
    drawTiles(True)
    drawBubbleMoneyAmount()
    drawLevelNumber()

def drawLevelNumber():
    global gameLevel, bubbleFont

    textSurface = bubbleFont.render('Level = ' + str(gameLevel), True, WHITE)
    textRect = textSurface.get_rect()
    textRect.bottomright = (windowWidth, windowHeight)
    left, top = textRect.topleft
    DISPLAYSURF.blit(textSurface, (left, top))

def drawBubbleMoneyAmount():
    global bubbleCoins, bubbleFont

    textSurface = bubbleFont.render('Bubbles = ' + str(bubbleCoins), True, WHITE)
    textRect = textSurface.get_rect()
    textRect.topright = (windowWidth, 0)
    left, top = textRect.topleft
    DISPLAYSURF.blit(textSurface, (left, top))

def drawLives():
    global lives
    textSurface = bubbleFont.render('Lives = ' + str(defaults.lives), True, WHITE)
    textRect = textSurface.get_rect()
    textRect.bottomleft = (0, windowHeight)
    left, top = textRect.topleft
    DISPLAYSURF.blit(textSurface, (left, top))


def determineLevel(mousePosX, mousePosY):
    global openScreenRects, currSeedDictGroup

    if openScreenRects[0].collidepoint(mousePosX, mousePosY):
        currSeedDictGroup = seedDictGroup1
        addCleaningSupplySeeds()
        return 1
    elif openScreenRects[1].collidepoint(mousePosX, mousePosY):
        currSeedDictGroup = seedDictGroup2
        addCleaningSupplySeeds()
        return 2
    elif openScreenRects[2].collidepoint(mousePosX, mousePosY):
        currSeedDictGroup = seedDictGroup3
        addCleaningSupplySeeds()
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
    textSurface = bugFont.render('Objective', True, BLACK, CYAN)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize * 8))
    DISPLAYSURF.blit(textSurface, textRect)
    textSurface = bugFont.render('Cleaning Supply Log', True, BLACK, PINK)
    textRect = textSurface.get_rect()
    openScreenRects.append((textRect))
    textRect.midtop = (windowWidth / 2, windowHeight / 7 + (fontSize * 10))
    DISPLAYSURF.blit(textSurface, textRect)


def resetVariables():
    formFloorGridArray()
    formFloorGridRectsArray()
    drawTiles(False)

def terminate():  # terminates game
    pygame.quit()
    sys.exit()

# projectile and bug collision WORKS
def collision2():
    for bug in enemy_sprites:
        for bullet in projectileGroup:
            if pygame.sprite.collide_rect(bug, bullet):
                if(bullet.type == "icedroplet" and bug.speed > 5):
                    bug.speed -= 5
                bug.health -= bullet.damage
                bullet.kill()


def mainGame():
    global DISPLAYSURF, gameLevel, frames, curr_time, bugEnterAry, gameMessageOn, currMessage, currSeedDictGroup, seedDictGroup1, seedDictGroup2, seedDictGroup3

    clicked = False

    resetVariables()

    my_eventTime = USEREVENT + 1
    pygame.time.set_timer(my_eventTime, 150)

    #addCleaningSupplySeeds()


    seedSelected = None
    dictIndex = 0
    price = None

    timeSinceStart = 0

    curr_time5000 = pygame.time.get_ticks()
    curr_time1000 = pygame.time.get_ticks()
    curr_time500 = pygame.time.get_ticks()
    curr_time250 = pygame.time.get_ticks()

    posX, posY = None, None

    while True:

        for event in pygame.event.get():
            collision2()
            if event.type == MOUSEBUTTONDOWN:
                posX, posY = pygame.mouse.get_pos()
                clicked = True
                if gameLevel == 0:
                    timeSinceStart = 0
                    curr_time5000 = pygame.time.get_ticks()
                    curr_time1000 = pygame.time.get_ticks()
                    curr_time500 = pygame.time.get_ticks()
                    curr_time250 = pygame.time.get_ticks()
            else:
                clicked = False

            if gameLevel == 0:
                logNum = 1
                drawOpeningScreen()
                if clicked:
                    gameLevel = determineLevel(posX, posY)

            if gameLevel == 1 or gameLevel == 2 or gameLevel == 3:

                readFile()

                if clicked == True:
                    dictIndex, seedSelected = getSeedSelected(posX, posY, seedSelected, dictIndex)
                    seedSelected = addSelectedCleaningSupply(dictIndex, seedSelected, posX, posY)

                    removeClickedBubbles(posX, posY)

                if curr_time5000 + 5000 <= pygame.time.get_ticks():
                    curr_time5000 = pygame.time.get_ticks()
                    addBubbleCoin(False)

                if curr_time1000 + 1000 <= pygame.time.get_ticks(): # every 1 second that passes this will happen
                    curr_time1000 = pygame.time.get_ticks()
                    timeSinceStart += 1000

                    gameMessageOn = False
                    getBugsEntering(timeSinceStart)

                    proj(timeSinceStart)
                    removeExpiredBubbles()
                    updateSoapDispenserBubbles()
                    activateBleach()

                    sendDamage()

                if curr_time500 + 500 <= pygame.time.get_ticks():
                    curr_time500 = pygame.time.get_ticks()
                    #checkPlungersHaveTarget()
                    activatePlungers()


                if curr_time250 + 250 <= pygame.time.get_ticks():
                    curr_time250 = pygame.time.get_ticks()
                    drawSeedLoadingBars(250) # seed will be drawn and updated

                if event.type == my_eventTime:
                    checkBugCleaningSupplyCollision()
                    removeDeadSprites()

                    drawBackground()

                    drawLives()

                    cleaningSupplyBackGrounds.draw(DISPLAYSURF)
                    cleaningSupplySeedsGroup.draw(DISPLAYSURF)

                    cleaningSupplyGroup.draw(DISPLAYSURF)
                    cleaningSupplyGroup.draw(DISPLAYSURF)
                    projectileGroup.draw(DISPLAYSURF)
                    projectileGroup.update()

                    enemy_sprites.draw(DISPLAYSURF)
                    enemy_sprites.update()

                    bubbleCoinGroup.draw(DISPLAYSURF)
                    bubbleCoinGroup.update()

                    if gameMessageOn == True:
                        gameMessage(currMessage)

                    #print(str(windowWidth))
                    #print(str(windowHeight))

            if gameLevel == 4:
                objectiveImg = pygame.transform.smoothscale(pygame.image.load('objective.PNG'), (windowWidth, windowHeight))

                DISPLAYSURF.blit(objectiveImg, (0, 0))
                backButtonRect = drawBackButton()

                if backButtonRect.collidepoint(posX, posY):
                    gameLevel = 0


            if gameLevel == 5:
                print(str(logNum))
                logImg = pygame.transform.smoothscale(pygame.image.load('log' + str(logNum) + '.PNG'),
                                                            (windowWidth, windowHeight))

                DISPLAYSURF.blit(logImg, (0, 0))
                backButtonRect = drawBackButton()

                if not logNum == 3:
                    nextButtonRect = drawNextButton()

                if backButtonRect.collidepoint(posX, posY):
                    gameLevel = 0

                if nextButtonRect.collidepoint(posX, posY) and not logNum == 3:
                    logNum += 1
                    posX, posY = 0, 0





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
            if floorGrid[col][row] == None:
                print('None' + " ", end='')
            else:
                print(str(floorGrid[col][row].name) + " ", end='')
        print()

def printFloorRectsAry():  # Print the floor grid array contents whenever you want to see it
    for row in range(5):
        for col in range(9):
            if floorGridRects[col][row] == None:
                print('None' + " ", end='')
            else:
                print(str(floorGridRects[col][row]) + " ", end='')
        print()
# RUN MAIN

if __name__ == '__main__':
    mainGame()