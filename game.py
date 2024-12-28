import constants, pygame

class Game:

    def __init__(self, title, width, height, audio_manager, visual_manager, fullscreen=True):
        constants.game = self

        self.objects = []
        self.screen = None
        self.clock = None
        self.time, self.delta_time = 0, 0
        self.gameOn = True
        self.player = None
        self.title = title
        self.width = width
        self.height = height
        self.fullscreen = fullscreen

        self.audio_manager = audio_manager
        self.visual_manager = visual_manager

        self.start()

    def start(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.gameOn = True
        self.refresh_screen()

    def refresh_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN if self.fullscreen else 0, pygame.SCALED)

    def loop(self):
        while self.gameOn:
            self.delta_time = self.clock.tick_busy_loop()
            self.time = pygame.time.get_ticks()

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

            for obj in self.objects:
                obj.update()
                obj.draw()

            pygame.display.flip()