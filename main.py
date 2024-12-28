from game import Game
from object import Object
import constants

def start():
    Game("Example game", constants.WIDTH, constants.HEIGHT, None, None, fullscreen=False)

def main_menu():
    constants.game.objects.clear()
    
    sprite = "game_sprites/player.jpg"
    object1 = Object("object", sprite, position = (constants.WIDTH/2, constants.HEIGHT/2), ObjectType = 0)

start()
main_menu()
constants.game.loop()