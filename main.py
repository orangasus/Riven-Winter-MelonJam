from game_class import Game
from Object_Classes.base_object import BaseObject
import pygame
import constants
from audio_manager import Audio_Manager
from Object_Classes.player_controller import Player
import Object_Classes.tile_class as tiles

def start():
    Game("Example game", constants.WIDTH, constants.HEIGHT, Audio_Manager(), None, fullscreen=False)

def main_menu():
    game = constants.game
    game.objects.clear()
    player = Player('game_sprites/temp_player_sprite.png', pygame.Vector2(300, 400), constants.ObjectType.PLAYER)
    game.camera.target = player
    tiles.draw_tile_list(constants.tile_set_example)

start()
main_menu()
constants.game.loop()