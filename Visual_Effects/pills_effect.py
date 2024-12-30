import pygame

from Visual_Effects.effects import VisualEffect
import constants

class TakePills(VisualEffect):

    def __init__(self, duration):
        self.duration = duration
        self.time = 0

    def start(self):
        if constants.game.took_pills:
            return
        super().start()
        self.time = 0
        #TODO: Play sound effect
        self.update()


    def update(self):
        self.time += 1
        if self.time >= 10:
            pygame.time.wait(self.duration)
            self.stop()
        constants.game.screen.fill((0, 0, 0))
