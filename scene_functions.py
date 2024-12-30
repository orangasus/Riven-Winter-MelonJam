import pygame

import constants
from Object_Classes.player_controller import Player
from Object_Classes.ui import Button, Label
from Visual_Effects.animation import SpriteSheet


def main_menu():
    game = constants.game
    game.objects.clear()

    upload_background()
    title_img = pygame.image.load('Assets/images/game_title.png').convert_alpha()
    button_img = pygame.image.load('Assets/images/button_start.png').convert_alpha()
    button_img_hover = pygame.image.load('Assets/images/button_hover.png').convert_alpha()
    button_img_pressed = pygame.image.load('Assets/images/button_pressed.png').convert_alpha()
    title_label = Label(title_img, (game.width // 2, game.height // 2 - 100), (250, 150))
    play_button = Button(button_img, button_img_hover, button_img_pressed,
                         (constants.CENTER_WIDTH, constants.CENTER_HEIGHT + 50), (128, 64), start_button)


def start_button():
    game = constants.game
    game.objects.clear()

    load_animations()
    global player_animations
    player = Player(game.get_sprite("spike"), pygame.Vector2(300, 400), size=(12, 32), offset=(-10, 0),
                    idle_animation=player_animations[0],
                    walk_animation=player_animations[1], jump_animation=player_animations[2],
                    climb_animation=player_animations[3], die_animation=player_animations[4])
    game.player = player

    game.level_manager.next_level()


def upload_background():
    temp_bg = pygame.image.load('Assets/images/free-swamp-game-tileset-pixel-art/Background/Background.png')
    resized_bg = pygame.transform.scale(temp_bg, (constants.WIDTH, constants.HEIGHT))
    constants.game.background = resized_bg


def ending_screen():
    game = constants.game
    game.objects.clear()
    thx_img = pygame.image.load('Assets/images/thx_img.png').convert_alpha()
    thx_label = Label(thx_img, (constants.CENTER_WIDTH, constants.CENTER_HEIGHT), (250, 150))
    upload_background()
    # message_label = Label(None, (game.width // 2, game.height // 2 + 150), (200, 50))


player_animations = []


def load_animations():
    global player_animations
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Idle_4"), 32, 32, 130))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Run_6"), 32, 32, 130))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Jump_8"), 32, 32, 130, repeat=False))
    player_animations.append(
        SpriteSheet(constants.game.get_sprite("Owlet_Monster_Climb_4"), 32, 32, 130, flipable=False))
    player_animations.append(SpriteSheet(constants.game.get_sprite("Owlet_Monster_Death_8"), 32, 32, 130))
