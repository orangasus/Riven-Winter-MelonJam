import pygame
import constants
from enum import Enum
from object import Object
import game
from game import *
# Differentiates between types of interactable objects
class TileType(Enum):

<<<<<<< Updated upstream
class Tile():
    def __init__(self, position, is_real, is_lethal, is_climbable, sprite, sound_effect):
        super().__init__()
        self.position = position
        self.is_real = is_real
        self.is_climbable = is_climbable
        self.sprite = sprite
        self.sound_effect = sound_effect

=======
    GENERIC = 1

    LADDER = 2

    SPIKE = 3

    screen_transition = 4
TileType = TileType.GENERIC

class Tile(Object):
    tile_size = 32
    tile_list = []

    def __init__(self, name, sprite=None, color=None,
                 position= (constants.CENTER_HEIGHT, constants.CENTER_HEIGHT, ),
                 is_real=False, is_climbable=False, is_lethal=False, sound_effect=None):
        super().__init__(name=name, sprite=sprite, color=color, position=position)

        self.is_real = is_real
        self.is_climbable = is_climbable
        self.is_lethal = is_lethal
        self.sound_effect = sound_effect
        self.tile_type = TileType.GENERIC
        self.sound_effect = sound_effect

    # adds a tile to a tile list based on it's location in the tile_set and it's TileType
    # returns the tile
    def add_tile(tile_type, row, column):
        if tile_type != 0:
            if tile_type == 1:
                sprite = "game_sprites/generic.png"
                name = "generic"
            if tile_type == 2:
                sprite = "game_sprites/ladder.png"
                name = "ladder"
            if tile_type == 3:
                sprite = "game_sprites/spike.png"
                name = "spike"

            position = (row * 32, column * 32)
            tile = Tile(name=name, sprite=sprite, position=position, is_real=True)
            Tile.tile_list.append(tile)
            return tile

    # iterates through the tile_set
    # adds tiles to a list and draws them using the object draw method
    def draw_tile_list(tile_set):
        row_num = 0
        column_num = 0
        for row in tile_set:
            for item in row:
                tile = Tile.add_tile(item, row_num, column_num)
                if tile:
                    Object.draw(tile, constants.screen)
                column_num += 1
            row_num += 1

    def delete_tile(self):
        Tile.tile_list.remove(self)

    
>>>>>>> Stashed changes
