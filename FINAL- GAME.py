import pygame, sys
from pygame.locals import *

# this is where all of the variables will be defined
FPS = 15
WINDOWWIDTH = 700
WINDOWHEIGHT = 700
SPEED = 25

# this is where we have all of the colors
#           R    G    B
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
BLUE = (    0,   0, 255)

# this is where we have our controls
LEFT = 'left'
RIGHT = 'right'

# this is the main method


def main():
    global DISPLAYSURF, BASICFONT
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Space Invaders')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

# this is where we define all of our functions

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Space Invaders', True, BLUE)

def runGame():
    # start him at the middle
    startx = WINDOWWIDTH / 2
    ship_coordinates = [{'x': startx,       'y':0},
                        {'x': startx-1,     'y':0},
                        {'x': startx-2,     'y':0},
                        {'x': startx+1,     'y': 0},
                        {'x': startx+2,     'y': 0},
                        {'x': startx,       'y': 1},
                        {'x': startx - 1,   'y': 1},
                        {'x': startx - 2,   'y': 1},
                        {'x': startx + 1,   'y': 1},
                        {'x': startx + 2,   'y': 1},
                        {'x': startx,       'y': 2},
                        {'x': startx - 1,   'y': 2},
                        {'x': startx - 2,   'y': 2},
                        {'x': startx + 1,   'y': 2},
                        {'x': startx + 2,   'y': 2},]

    # move him left/right, and how quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    direction = LEFT
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    direction = RIGHT
                elif event.key == pygame.K_ESCAPE:
                    terminate()


def showGameOverScreen():
    return 0

def terminate():
    pygame.quit()
    sys.exit()