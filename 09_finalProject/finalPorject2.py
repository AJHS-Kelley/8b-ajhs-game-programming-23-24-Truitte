# Truitte Moreland
import pygame
import sys
import random

class snake(object):
    def _init_(self):
        pass

    def get_head_position(self):
        pass
    
    def turn(self):
        pass

    def move(self):
        pass

    def reset(self):
        pass

    def draw(self, surface):
        pass

    def handle_keys(self):
        pass

class food(object):
    def _init_(self):
        pass

    def randomize_position(self):
        pass

    def draw(self, surface):
        pass
     
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

UP = (0,-1)
DOWN = (0, 1)
LEFT = (-1,0)
RIGHT = (-1,0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()


main()