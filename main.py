import constants
from Level_Classes.level_manager import LevelManager
from Managers.audio_manager import AudioManager
from Managers.visual_manager import VisualManager
from game_class import Game
from scene_functions import main_menu, intro_cutscene, ending_screen
from Level_Classes.levels_modules import level1, level2, level3
from Visual_Effects.effects import Vignette

def start():
    visual_manager = VisualManager("Assets/images")
    game = Game("Example game", constants.WIDTH, constants.HEIGHT,
         AudioManager(), visual_manager,
         LevelManager([level1.get_level(visual_manager), level2.get_level(visual_manager), level3.get_level(visual_manager)], main_menu, intro_cutscene=intro_cutscene, ending_cutscene=ending_screen),
         fullscreen=False)
    constants.set_tile_textures()
    game.effects.append(Vignette(40))
    
start()
main_menu()
constants.game.loop()
ending_screen()