import constants
from Object_Classes.base_object import BaseObject
from constants import ObjectType

tile_list = []


class Tile(BaseObject):
    tile_size = 32

    def __init__(self, sprite,
                 position, object_type,
                 is_real=False, is_foreground=False, sound_effect=None, size=(32, 32)):

        offset = None
        if object_type in constants.half_top:
            size=(32, 16)
            position = (position[0], position[1] - 8)
        elif object_type in constants.half_bottom:
            size=(18, 16)
            position = (position[0], position[1] + 8)
            offset = (0, -16)

        super().__init__(sprite=sprite, position=position, object_type=object_type, register=False, hitbox_size=size, offset=offset)

        self.is_real = is_real
        self.is_foreground = is_foreground
        self.sound_effect = sound_effect
        self.tile_type = object_type
        self.sound_effect = sound_effect
        if self.object_type in constants.collidable and self.is_real:
            self.add_to_game_object_list()
        else:
            self.add_to_game_decoration_list()


# adds a tile to a tile list based on it's location in the tile_set and it's TileType
# returns the tile
def add_tile(tile_type, row, column):
    if tile_type != 0:
        sprite = None
        foreground = False
        real = True
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
        else:
            if tile_type > 10000:
                object_type = tile_type / 10000
                sprite = constants.tile_textures[object_type]
                foreground = True
            elif tile_type < 0:
                real = False
                object_type = tile_type * -1
                sprite = constants.tile_textures[object_type]
            else:
                sprite = constants.tile_textures[abs(tile_type)]
                object_type = tile_type

        if sprite:  # Ensure the sprite is valid
            position = (column * Tile.tile_size, row * Tile.tile_size)
            tile = Tile(sprite, position, object_type, is_real=real, is_foreground=foreground)
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
