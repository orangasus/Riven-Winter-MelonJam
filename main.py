<<<<<<< Updated upstream
from object import Object, object_list
import object
=======
from game import Game
from object import Object
import tile
from tile import *
>>>>>>> Stashed changes
import constants
import pygame
from pygame.locals import *

<<<<<<< Updated upstream

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

sprite = "game_sprites\player.jpg"
object1 = Object("object", sprite, position = (constants.WIDTH/2, constants.HEIGHT/2), ObjectType = 0)
# initialize pygame
pygame.init()

# Define the dimensions of screen object
screen = pygame.display.set_mode((800, 600))
gameOn = True
# Our game loop
while gameOn:
    # for loop through the event queue
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # If the Backspace key has been pressed set
            # running false to exit the main loop
            if event.key == K_BACKSPACE:
                gameOn = False

        # Check for QUIT event
        elif event.type == QUIT:
            gameOn = False

    # Draw background
    screen.fill((255, 255, 255))

    # Update all objects
    for obj in object_list:
        obj.update()

    # Draw all objects
    for obj in object_list:
        obj.draw(screen)


    # Update the display using flip
    pygame.display.flip()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
=======
game = Game(title="My Game", width=800, height=600, audio_manager=None, visual_manager=None)

def start():
    Game("Example game", constants.WIDTH, constants.HEIGHT, None, None, fullscreen=False)

def main_menu():
    constants.game.objects.clear()
    
    sprite = "game_sprites/player.jpg"
    object1 = Object("object", sprite, position = (constants.WIDTH/2, constants.HEIGHT/2))
Tile.draw_tile_list(constants.tile_set_example)
start()
main_menu()
constants.game.loop()

>>>>>>> Stashed changes
