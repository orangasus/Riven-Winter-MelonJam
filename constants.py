import pygame
from enum import Enum

WIDTH = 1024
HEIGHT = 576
CENTER_WIDTH = WIDTH/2
CENTER_HEIGHT = HEIGHT/2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
colors = red, green, blue

class ObjectType(Enum):
    GENERIC = 1
    LADDER = 2
    SPIKE = 3
    PLAYER = 4
    UI = 20
    NEXT_SCREEN_TRANSITION = 5
    PREVIOUS_SCREEN_TRANSITION = 6
    NEXT_LEVEL = 10
    FAKE_GENERIC = 11
    FAKE_LADDER = 22
    FAKE_SPIKE = 33
    FAKE_PLAYER = 44

    # Used to store the instance of Game to be accessed by other modules
game = None

