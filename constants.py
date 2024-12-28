import pygame
from enum import Enum
from Visual_Effects.animation import SpriteSheet

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

tile_textures: {}

def set_tile_textures():
    global tile_textures
    tiles = SpriteSheet(game.get_sprite("Tileset"), 32, 32, 0).frames
    tile_textures = {
        1: game.get_sprite("generic"),
        2: game.get_sprite("ladder"),
        3: game.get_sprite("spike"),
        # Normal ground tiles
        10: tiles[1][1],
        11: tiles[0][0],
        12: tiles[0][1],
        13: tiles[0][2],
        14: tiles[1][2],
        15: tiles[2][2],
        16: tiles[2][1],
        17: tiles[2][0],
        18: tiles[1][0],
        # Inner ground tiles
        110: tiles[1][4],
        110: tiles[0][3],
        120: tiles[0][4],
        130: tiles[0][5],
        140: tiles[1][5],
        150: tiles[2][5],
        160: tiles[2][4],
        170: tiles[2][3],
        180: tiles[1][3],
    }
