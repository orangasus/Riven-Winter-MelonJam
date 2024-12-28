import object
from game import Game
from object import Object
import tile
from tile import *
import constants
import pygame
from pygame.locals import *

pygame.init()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
game = Game(title="My Game", width=800, height=600, audio_manager=None, visual_manager=None)

def start():
    Game("Example game", constants.WIDTH, constants.HEIGHT, None, None, fullscreen=False)

def main_menu():
    constants.game.objects.clear()

def game_loop():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Clear the screen
        constants.screen.fill((0, 0, 0))

        # Draw tiles
        Tile.draw_tile_list(constants.tile_set_example, constants.screen)

        # Update display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

def main():
    Tile.draw_tile_list(constants.tile_set_example, constants.screen)
    game_loop()


# Run the game
if __name__ == "__main__":
    main()

start()
main_menu()
constants.game.loop()
