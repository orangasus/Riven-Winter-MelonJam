import pygame

import constants
from Object_Classes.player_controller import Player
from Object_Classes.ui import Button, Label
from Visual_Effects.animation import SpriteSheet
from Visual_Effects.effects import BlockScreenTransition


def main_menu():
    game = constants.game
    game.objects.clear()
    game.decorations.clear()
    # game.player = None

    upload_background()
    title_img = pygame.image.load('Assets/images/labels/game_title.png').convert_alpha()
    button_img = pygame.image.load('Assets/images/buttons/play_button.png').convert_alpha()
    button_img_hover = pygame.image.load('Assets/images/buttons/play_hover.png').convert_alpha()
    button_img_pressed = pygame.image.load('Assets/images/buttons/play_pressed.png').convert_alpha()
    title_label = Label(title_img, (game.width // 2, game.height // 2 - 100), (250, 150))
    play_button = Button(button_img, button_img_hover, button_img_pressed,
                         (constants.CENTER_WIDTH, constants.CENTER_HEIGHT + 50), (128, 64), call_transition_to_cutscene)


def call_transition_to_cutscene():
    transition = BlockScreenTransition(30, (0, 0, 0), 0, on_finish=intro_cutscene)
    transition.start()


def intro_cutscene():
    game = constants.game
    game.objects.clear()
    game.decorations.clear()

    upload_background()
    intro_text_img = pygame.image.load('Assets/images/labels/intro_text.png').convert_alpha()
    button_img = pygame.image.load('Assets/images/buttons/start_button.png').convert_alpha()
    button_img_hover = pygame.image.load('Assets/images/buttons/start_hover.png').convert_alpha()
    button_img_pressed = pygame.image.load('Assets/images/buttons/start_pressed.png').convert_alpha()
    text_label = Label(intro_text_img, (constants.CENTER_WIDTH, constants.CENTER_HEIGHT),
                       (constants.WIDTH, constants.HEIGHT))
    play_button = Button(button_img, button_img_hover, button_img_pressed,
                         (constants.CENTER_WIDTH, constants.CENTER_HEIGHT + 185), (128, 64), start_button)

    # space_label = Label(press_space_img, (constants.CENTER_WIDTH, constants.CENTER_HEIGHT),
    #                    (constants.WIDTH, constants.HEIGHT))
    # key_pressed = pygame.key.get_pressed()
    #
    # if not key_pressed[pygame.K_SPACE]:
    #     flicker(space_label)


# def flicker(obj):
#     constants.cur_alpha += constants.d_alpha
#     if constants.cur_alpha <= constants.min_alpha or constants.cur_alpha >= constants.max_alpha:
#         constants.d_alpha *= -1
#     obj.sprite.set_alpha(constants.cur_alpha)


def start_button():
    game = constants.game
    game.objects.clear()

    load_animations()
    global player_animations
    player = Player(game.get_sprite("spike"), pygame.Vector2(300, 400), size=(16, 16), offset=(-8, -16),
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
    thx_img = pygame.image.load('Assets/images/labels/thx_img.png').convert_alpha()
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
