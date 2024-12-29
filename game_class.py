import constants, pygame
from pygame.math import Vector2
from Object_Classes.camera_object import Camera
import time

# Define our game class
# This is the main class that will run the game loop and store all necessary data
# A unique instance of it is stored in constants.game
class Game:

    def __init__(self, title, width, height, audio_manager, visual_manager, fullscreen=True):
        constants.game = self

        self.objects = []
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

        self.audio_manager = audio_manager
        self.visual_manager = visual_manager

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
            self.delta_time = self.clock.tick(60)
            self.time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.gameOn = False
                    elif event.key == pygame.K_F11:
                        self.fullscreen = not self.fullscreen
                        self.refresh_screen()
                if event.type == pygame.QUIT:
                    self.gameOn = False

            self.screen.fill((0, 0, 0))
            if self.background:
                self.screen.blit(self.background, (0, 0))

            self.camera.update()
            for obj in self.objects:
                obj.update()
                obj.draw()

            for effect in self.effects:
                effect.update()
                effect.draw()


            pygame.display.flip()

    def get_sprite(self, name):
        return self.visual_manager.sprites[name]