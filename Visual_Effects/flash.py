from Visual_Effects.effects import VisualEffect
import constants

class Flash(VisualEffect):

    def __init__(self, color, duration, flash_interval, flash_duration):
        self.color = color
        self.duration = duration
        self.flash_interval = flash_interval
        self.flash_check = flash_duration
        self.time = 0

    def start(self):
        super().start()
        self.time = 0

    def update(self):
        self.time += 1
        if self.time >= self.duration:
            self.stop()

    def draw(self):
        if self.time % self.flash_interval >= self.flash_check:
            for obj in constants.game.decorations:
                if not obj.is_real:
                    img = obj.sprite.copy()
                    img.fill(self.color)
                    constants.game.screen.blit(img, obj.rect)
