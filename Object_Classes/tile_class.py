import constants
from constants import ObjectType
from Object_Classes.base_object import BaseObject

tile_list = []

class Tile(BaseObject):
    tile_size = 32

    def __init__(self, sprite,
                 position, object_type,
                 is_real=False, is_climbable=False, is_lethal=False, sound_effect=None):
        super().__init__(sprite=sprite, position=position, object_type=object_type)

        self.is_real = is_real
        self.is_climbable = is_climbable
        self.is_lethal = is_lethal
        self.sound_effect = sound_effect
        self.tile_type = ObjectType.GENERIC
        self.sound_effect = sound_effect

# adds a tile to a tile list based on it's location in the tile_set and it's TileType
# returns the tile
def add_tile(tile_type, row, column):
    if tile_type != 0:
        sprite = None
        object_type = ObjectType.GENERIC
        if tile_type == 1:
            sprite = constants.game.get_sprite("generic")
            object_type = ObjectType.GENERIC
        elif tile_type == 2:
            sprite = constants.game.get_sprite("ladder")
            object_type = ObjectType.LADDER
        elif tile_type == 3:
            sprite = constants.game.get_sprite("spike")
            object_type = ObjectType.SPIKE

        if sprite:  # Ensure the sprite is valid
            position = (column * Tile.tile_size, row * Tile.tile_size)
            tile = Tile(sprite, position, object_type, is_real=True)
            tile_list.append(tile)
            return tile
    return None

# iterates through the tile_set
# adds tiles to a list and draws them using the object draw method
def draw_tile_list(tile_set):
    row_num = 0
    for row in tile_set:
        column_num = 0  # Reset column number for each row
        for tile_type in row:
            tile = add_tile(tile_type, row_num, column_num)
            # if tile:
            #     tile.draw()  # Call the object's draw method
            column_num += 1
        row_num += 1

def delete_tile(self):
    tile_list.remove(self)
