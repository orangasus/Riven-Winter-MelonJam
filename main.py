from game_class import Game
import pygame
import constants
from Managers.audio_manager import AudioManager
from Managers.visual_manager import VisualManager
from Object_Classes.player_controller import Player
from Object_Classes.ui import Button
from Visual_Effects.animation import SpriteSheet
from levels.tutorial.screen_1 import screen
from Visual_Effects.effects import CircleScreenTransition
import Object_Classes.tile_class as tiles
from levels import level_1

player_animations = []

def load_animations():
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Idle_4"), 32, 32, 130))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Run_6"), 32, 32, 130))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Jump_8"), 32, 32, 130, repeat=False))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Climb_4"), 32, 32, 130, flipable=False))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Death_8"), 32, 32, 130))

def start():
    Game("Example game", constants.WIDTH, constants.HEIGHT, AudioManager(), VisualManager("Assets/images"), fullscreen=False)
    constants.set_tile_textures()

def main_menu():
    game = constants.game
    game.objects.clear()
    play_button = Button(game.get_sprite("ladder"), game.get_sprite("spike"), game.get_sprite("generic"),
                         (constants.CENTER_WIDTH, constants.CENTER_HEIGHT), (100, 100), start_button)

def start_button():
    ve = CircleScreenTransition(60, (255, 255, 255), 50, 70, 8, 1, level1)
    ve.start()

def level1():
    game = constants.game
    game.objects.clear()
    load_animations()
    player = Player(game.get_sprite("spike"), pygame.Vector2(300, 400),
                    ide_animation=player_animations[0],
                    walk_animation=player_animations[1],
                    jump_animation=player_animations[2],
                    climb_animation=player_animations[3],
                    die_animation=player_animations[4])
    game.player = player
    #animation = SpriteSheet(game.get_sprite("Owlet_Monster_Idle_4"), 32, 32, 100)
    #player.play_animation(animation)
    #game.camera.target = player
    tiles.draw_tile_list(screen)

start()
#main_menu()
level1()
constants.game.loop()