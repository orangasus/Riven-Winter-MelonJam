import constants
from Managers.audio_manager import AudioManager
from Managers.visual_manager import VisualManager
from game_class import Game
from scene_functions import main_menu

player_animations = []

def load_animations():
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Idle_4"), 32, 32, 130))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Run_6"), 32, 32, 130))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Jump_8"), 32, 32, 130, repeat=False))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Climb_4"), 32, 32, 130, flipable=False))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Death_8"), 32, 32, 130))

def start():
    Game("Example game", constants.WIDTH, constants.HEIGHT, AudioManager(), VisualManager("Assets/images"),
         fullscreen=False)
    constants.set_tile_textures()
    
start()
main_menu()
# level1()
constants.game.loop()