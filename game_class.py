import constants, pygame
from pygame.math import Vector2
from Object_Classes.camera_object import Camera
import time

from scene_functions import draw_ending_screen


# Define our game class
# This is the main class that will run the game loop and store all necessary data
# A unique instance of it is stored in constants.game
class Game:

    def __init__(self, title, width, height, audio_manager, visual_manager, level_manager, fullscreen=True):
        constants.game = self

        self.objects = []
        self.decorations = []
        self.camera = Camera()
        self.effects = []
        self.screen = None
        self.clock = None
        self.time, self.delta_time = 0, 0
        self.gameOn = True
        self.player = None
        self.background = None
        self.title = title
        self.width = width
        self.height = height
        self.fullscreen = fullscreen

        # for ending cutscene
        self.end_count = 0
        self.end_limit = 400

        self.audio_manager = audio_manager
        self.visual_manager = visual_manager
        self.level_manager = level_manager

        self.took_pills = False
        self.ended = False

        self.start()

    # Set up the game with pygame
    def start(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.gameOn = True
        self.refresh_screen()

    # Refresh the screen with the current width, height, and fullscreen settings
    def refresh_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))

    # The main game loop
    def loop(self):
        while self.gameOn:
            self.clock.tick(constants.FPS)
            self.time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.gameOn = False
                    elif event.key == pygame.K_F11:
                        self.fullscreen = not self.fullscreen
                        self.refresh_screen()
                    elif event.key == pygame.K_r:
                        self.level_manager.previous_scene()
                    elif event.key == pygame.K_t:
                        self.level_manager.next_scene()
                if event.type == pygame.QUIT:
                    self.gameOn = False

            self.screen.fill((0, 0, 0))
            if self.background:
                self.screen.blit(self.background, (0, 0))

            if self.ended:
                print("ENDING", self.end_count)
                self.end_count += 1
                if self.end_count <= self.end_limit:
                    print("DRAW")
                    draw_ending_screen()
                else:
                    print("FAKE")
                    self.gameOn = False


            for decoration in self.decorations:
                if not decoration.is_foreground:
                    if not decoration.is_real and self.took_pills:
                        continue
                    decoration.draw()

            self.camera.update()
            for obj in self.objects:
                obj.update()
                obj.draw()

            if self.player:
                self.player.update()
                self.player.draw()

            for decoration in self.decorations:
                if decoration.is_foreground:
                    decoration.draw()


            for effect in self.effects:
                effect.update()
                effect.draw()

            pygame.display.flip()

    def get_sprite(self, name):
        return self.visual_manager.sprites[name]