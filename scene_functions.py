import Object_Classes.tile_class as tiles
import constants
from Object_Classes.player_controller import Player
from Object_Classes.ui import Button, Label
from Visual_Effects.effects import CircleScreenTransition
from Visual_Effects.animation import SpriteSheet
from levels import level_1
import pygame


def main_menu():
    game = constants.game
    game.objects.clear()

    upload_background()
    #title_label = Label(None, (game.width // 2, game.height // 2 + 150), (200, 50))
    play_button = Button(game.get_sprite("ladder"), game.get_sprite("spike"), game.get_sprite("generic"),
                         (constants.CENTER_WIDTH, constants.CENTER_HEIGHT), (100, 100), start_button)


def start_button():
    ve = CircleScreenTransition(60, (255, 255, 255), 50, 70, 8, 1, level1)
    ve.start()

def upload_background():
    temp_bg = pygame.image.load('Assets/images/free-swamp-game-tileset-pixel-art/Background/Background.png')
    resized_bg = pygame.transform.scale(temp_bg, (constants.WIDTH, constants.HEIGHT))
    constants.game.background = resized_bg

def level1():
    game = constants.game
    game.objects.clear()

    upload_background()
    tiles.draw_tile_list(level_1.level_1_screen_1)
    load_animations()
    player = Player(game.get_sprite("spike"), pygame.Vector2(300, 400),
                    idle_animation=player_animations[0],
                    walk_animation=player_animations[1], jump_animation=player_animations[2],
                    climb_animation=player_animations[3], die_animation=player_animations[4])
    game.player = player

def ending_screen():
    game = constants.game
    game.objects.clear()

    upload_background()
    #message_label = Label(None, (game.width // 2, game.height // 2 + 150), (200, 50))


player_animations = []

def load_animations():
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Idle_4"), 32, 32, 130))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Run_6"), 32, 32, 130))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Jump_8"), 32, 32, 130, repeat=False))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Climb_4"), 32, 32, 130, flipable=False))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Death_8"), 32, 32, 130))
