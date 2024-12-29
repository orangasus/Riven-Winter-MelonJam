import constants
from Managers.audio_manager import AudioManager
from Managers.visual_manager import VisualManager
from game_class import Game
from scene_functions import main_menu


def start():
    Game("Example game", constants.WIDTH, constants.HEIGHT, AudioManager(), VisualManager("Assets/images"),
         fullscreen=False)
    constants.set_tile_textures()


start()
main_menu()
# level1()
constants.game.loop()
