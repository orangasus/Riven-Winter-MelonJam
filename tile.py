import pygame

class Tile():
    def __init__(self, position, is_real, is_lethal, is_climbable, sprite, sound_effect):
        super().__init__()
        self.position = position
        self.is_real = is_real
        self.is_climbable = is_climbable
        self.sprite = sprite
        self.sound_effect = sound_effect

