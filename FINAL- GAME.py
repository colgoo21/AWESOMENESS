import pygame, sys
from pygame.locals import *
from Cole_Demo3 import *

class Game (object):
    def __init__(self):
# this is where all of the variables will be defined
        self.FPS = 15
        self.WINDOWWIDTH = 700
        self.WINDOWHEIGHT = 700
        self.SPEED = 25

# this is where we have all of the colors
#           R    G    B
        self.BLACK = (   0,   0,   0)
        self.WHITE = ( 255, 255, 255)
        self.BLUE = (    0,   0, 255)

# this is where we have our controls
        self.LEFT = 'left'
        self.RIGHT = 'right'

# this is the main method


    def main(self):
        global DISPLAYSURF, BASICFONT
        pygame.init()
        DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, sel.WINDOWHEIGHT))
        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Space Invaders')

        self.showStartScreen()
        while True:
            self.runGame()
            self.showGameOverScreen()

    # this is where we define all of our functions

    def showStartScreen(self):
        titleFont = pygame.font.Font('freesansbold.ttf', 100)
        titleSurf1 = titleFont.render('Space Invaders', True, self.BLUE)

    def runGame(self):
        # start him at the middle
        startx = self.WINDOWWIDTH / 2
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
        self.left_right_stop()


    def showGameOverScreen(self):
        return 0

    def terminate(self):
        pygame.quit()
        sys.exit()