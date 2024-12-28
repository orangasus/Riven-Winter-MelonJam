from game import Game
from object import Object
import constants
from audio_manager import Audio_Manager
from Object_Classes.player_controller import Player
import Object_Classes.tile_class as tiles
from levels import level_1

import levels
def start():
    Game("Example game", constants.WIDTH, constants.HEIGHT, None, None, fullscreen=False)

def main_menu():
    constants.game.objects.clear()
    
    sprite = "game_sprites/player.jpg"
    object1 = Object("object", sprite, position = (constants.WIDTH/2, constants.HEIGHT/2), ObjectType = 0)
    game = constants.game
    game.objects.clear()
    player = Player('game_sprites/temp_player_sprite.png', pygame.Vector2(300, 400), constants.ObjectType.PLAYER)
    game.camera.target = player
    tiles.draw_tile_list(level_1.level_1_screen_1)

start()
main_menu()
constants.game.loop()