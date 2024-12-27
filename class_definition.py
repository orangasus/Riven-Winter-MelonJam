from enum import Enum
import pygame
from pygame import Vector2

#
class Object:
    def __init__(self, name, size, position, sprite, object_type):

    def add_object(self):
        pass

    def draw(self):
        pass

    def destroy(self):
        pass

    def update(self):
        pass

    def on_interact(self):
        pass

class Object_Type(Enum):
    Generic = 1

    Ladder = 2

    Spike = 3


class Tile(Object):
    def __init__(self, size, position, is_real, is_lethal, is_climbable, sprite, sound_effect):
        super().__init__()

class spike(Object):
    def __init__(self, size, position, is_real, is_lethal, is_climbable, sprite, sound_effect):
        super().__init__()


    def kill(self):
        # player.kill()

class Player(Object):
    def __init__(self):
        super().__init__(is_grouded, is_alive)

    def move(self):
        pass

    def jump(self):
        pass

    def climb(self):
        pass

    def interact(self):
        pass

class Game:
    object_list = []
    def __init__(self, screen, clock, player, objects, audio_manager, visual_manager, ):
        pass

    def open_main_menu():
        game.objects.clear()
        Title()
        Object()


    def open_level_1():
        game.objects.clear()
        Player()
        Wall()
        Ground()


class Audio_Manager:
    def __init__(self, sounds):
        self.sounds = sounds

    def play_sound(self, sound):
    # play self.sounds[sound]


