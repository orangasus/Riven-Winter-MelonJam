import pygame
from enum import Enum
from Visual_Effects.animation import SpriteSheet

WIDTH = 992
HEIGHT = 542
FPS = 90
CENTER_WIDTH = WIDTH/2
CENTER_HEIGHT = HEIGHT/2
SPRITESHEET_SIZE = 24
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

collidable = [ObjectType.GENERIC, ObjectType.LADDER, ObjectType.SPIKE, ObjectType.NEXT_SCREEN_TRANSITION, ObjectType.PREVIOUS_SCREEN_TRANSITION,
              100, 101, 102, 172, 173, 174, 175, 107, 108, 177, 178, 106, 124, 126, 127, 176, 224, 196, 197, 198, 199, 201, 179, 148, 148, 150, 200, 223, 220, 221, 222, 225, 155]
climable = [ObjectType.LADDER]
deadly = [ObjectType.SPIKE]

half_top = [106]
half_bottom = []

# Used to store the instance of Game to be accessed by other modules
game = None

tile_textures: {}

def set_tile_textures():
    global tile_textures
    tiles = SpriteSheet(game.get_sprite("spritesheet"), 32, 32, 0, color=(0, 0, 0)).frames
    transparent = game.get_sprite("transparent")
    transparent.set_colorkey((0, 0, 0))
    tile_textures = {
        0: game.get_sprite("spike"),
        1: game.get_sprite("spike"),
        2: game.get_sprite("ladder"),
        3: game.get_sprite("spike"),
        22: game.get_sprite("ladder"),
        4: transparent,
        5: transparent,
        6: transparent
    }
    for i in range(SPRITESHEET_SIZE*SPRITESHEET_SIZE):
        column = i % SPRITESHEET_SIZE
        row = i // SPRITESHEET_SIZE
        tile_textures[100+i] = tiles[row][column]
