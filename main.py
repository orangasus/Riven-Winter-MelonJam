from game_class import Game
from Object_Classes.base_object import BaseObject
import pygame
import constants
from audio_manager import Audio_Manager
from Object_Classes.player_controller import Player
from Object_Classes.ui import Button
import Object_Classes.tile_class as tiles
from levels import level_1

def start():
    Game("Example game", constants.WIDTH, constants.HEIGHT, Audio_Manager(), None, fullscreen=False)

def main_menu():
    game = constants.game
    game.objects.clear()
    play_button = Button("game_sprites/ladder.png", "game_sprites/spike.png", "game_sprites/generic.png",
                         (constants.CENTER_WIDTH, constants.CENTER_HEIGHT), (100, 100), level1)

def level1():
    game = constants.game
    game.objects.clear()
    player = Player('game_sprites/temp_player_sprite.png', pygame.Vector2(300, 400), constants.ObjectType.PLAYER)
    #game.camera.target = player
    tiles.draw_tile_list(level_1.level_1_screen_1)

start()
main_menu()
constants.game.loop()