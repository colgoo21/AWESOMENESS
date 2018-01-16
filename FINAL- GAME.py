import pygame, sys
from pygame.locals import *

# this is where all of the variables will be defined
FPS = 15
WINDOWWIDTH = 1000
WINDOWHEIGHT = 1000
SPEED = 25

# this is where we have all of the colors
#           R    G    B
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
BLUE = (    0,   0, 255)

# this is where we have our controls

UP = 'up'
DOWN = 'down'
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
