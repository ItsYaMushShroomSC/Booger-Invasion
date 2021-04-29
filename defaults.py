import time
import pygame
from pygame.locals import *
import sys
# Surface:
pygame.init()
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Cleaning Supplies vs Bugs')

# Constants:
windowWidth = DISPLAYSURF.get_width()  # resized to fullscreen
windowHeight = DISPLAYSURF.get_height()  # resized to fullscreen
scaleFactorW = int(windowWidth / 1536)
scaleFactorH = int(windowHeight / 864)
XMARGIN = 200 * scaleFactorW
YMARGIN = 100 * scaleFactorH

game_l = 0
# Text Font:
fontSize = 54 * scaleFactorH
bugFont = pygame.font.Font('bugFont.ttf', fontSize)
cleaningFont = pygame.font.Font('CleaningSupplyFont.otf', fontSize)

# Time:
time_since_enter = 0
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

lives = 3

def setMargins():
    global scaleFactorH, scaleFactorW, XMARGIN, YMARGIN

    scaleFactor = scaleFactorH
    if scaleFactorW < scaleFactorH:
        scaleFactor = scaleFactorW

    XMARGIN, YMARGIN = int((windowWidth - (100 * scaleFactor * 9)) / 2), int(
        (windowHeight - (121 * scaleFactor * 5)) / 2)