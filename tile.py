import pygame
import constants
from enum import Enum
from object import Object
import game
from game import *

class TileType(Enum):
    GENERIC = 1

    LADDER = 2

    SPIKE = 3

    SCREEN_TRANSITION = 4
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
            sprite = None
            name = "generic"
            if tile_type == 1:
                sprite = "game_sprites/generic.png"
                name = "generic"
            elif tile_type == 2:
                sprite = "game_sprites/ladder.png"
                name = "ladder"
            elif tile_type == 3:
                sprite = "game_sprites/spike.png"
                name = "spike"

            if sprite:  # Ensure the sprite is valid
                position = (column * Tile.tile_size, row * Tile.tile_size)
                tile = Tile(name=name, sprite=sprite, position=position, is_real=True)
                Tile.tile_list.append(tile)
                return tile
        return None

    # iterates through the tile_set
    # adds tiles to a list and draws them using the object draw method
    def draw_tile_list(tile_set, screen):
        row_num = 0
        for row in tile_set:
            column_num = 0  # Reset column number for each row
            for tile_type in row:
                tile = Tile.add_tile(tile_type, row_num, column_num)
                if tile:
                    tile.draw(screen)  # Call the object's draw method
                column_num += 1
            row_num += 1

    def delete_tile(self):
        Tile.tile_list.remove(self)
