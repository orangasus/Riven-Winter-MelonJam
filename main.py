import constants
from Level_Classes.level_manager import LevelManager
from Managers.audio_manager import AudioManager
from Managers.visual_manager import VisualManager
from game_class import Game
from scene_functions import main_menu
from Level_Classes.levels_modules import level1

def start():
    visual_manager = VisualManager("Assets/images")
    Game("Example game", constants.WIDTH, constants.HEIGHT,
         AudioManager(), visual_manager,
         LevelManager([level1.get_level(visual_manager)], main_menu),
         fullscreen=False)
    constants.set_tile_textures()
    
start()
main_menu()
# level1()
constants.game.loop()