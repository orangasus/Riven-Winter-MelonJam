import Object_Classes.tile_class as tiles
import constants
from Object_Classes.player_controller import Player
from Object_Classes.ui import Button, Label
from Visual_Effects.effects import CircleScreenTransition
from levels import level_1
import pygame


def main_menu():
    game = constants.game
    game.objects.clear()

    #game.background = pygame.image.load('')
    #title_label = Label(None, (game.width // 2, game.height // 2 + 150), (200, 50))
    play_button = Button(game.get_sprite("ladder"), game.get_sprite("spike"), game.get_sprite("generic"),
                         (constants.CENTER_WIDTH, constants.CENTER_HEIGHT), (100, 100), start_button)


def start_button():
    ve = CircleScreenTransition(60, (255, 255, 255), 50, 70, 8, 1, level1)
    ve.start()


def level1():
    game = constants.game
    game.objects.clear()

    # game.background = pygame.image.load('')

    player = Player(game.get_sprite("spike"), pygame.Vector2(300, 400))
    game.player = player

    # animation = SpriteSheet(game.get_sprite("Owlet_Monster_Idle_4"), 32, 32, 100)
    # player.play_animation(animation)
    # game.camera.target = player

    tiles.draw_tile_list(level_1.level_1_screen_1)

def ending_screen():
    game = constants.game
    game.objects.clear()

    #game.background = pygame.image.load('')
    #message_label = Label(None, (game.width // 2, game.height // 2 + 150), (200, 50))
