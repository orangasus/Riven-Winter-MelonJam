from pygame.math import Vector2
import constants, random

class Camera:

    def __init__(self):
        self.position = Vector2(0, 0)
        self.target = None
        self.zoom = 1
        self.follow_speed = 0.01
        self.camera_shake_intensity = 0
        self.camera_shake_duration = 0

    def update(self):
        game = constants.game
        if self.target:
            self.position += ((self.target.position.x - constants.CENTER_WIDTH, self.target.position.y - constants.CENTER_HEIGHT) - self.position) * self.follow_speed * game.delta_time
        if self.camera_shake_duration > 0:
            self.camera_shake_duration -= game.delta_time
            self.position += Vector2((0.5 - random.random()) * self.camera_shake_intensity,
                                     (0.5 - random.random()) * self.camera_shake_intensity)

    def camera_shake(self, amount, duration):
        self.camera_shake_intensity = amount
        self.camera_shake_duration = duration