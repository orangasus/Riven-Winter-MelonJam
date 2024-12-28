from game import Game
from object import Object
import constants

def start():
    Game("Example game", constants.WIDTH, constants.HEIGHT, None, None, fullscreen=False)

def main_menu():
    constants.game.objects.clear()
    Object("player")

start()
main_menu()
constants.game.loop()


