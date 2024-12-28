from pygame.math import Vector2
import constants, random
import pygame

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
            zoom_correction = (constants.CENTER_WIDTH / self.zoom, constants.CENTER_HEIGHT / self.zoom)
            target_position = (self.target.position.x - zoom_correction[0],
                               self.target.position.y - zoom_correction[1])
            self.position += (target_position - self.position) * self.follow_speed * game.delta_time
        if self.camera_shake_duration > 0:
            self.camera_shake_duration -= game.delta_time
            self.position += Vector2((0.5 - random.random()) * self.camera_shake_intensity,
                                     (0.5 - random.random()) * self.camera_shake_intensity)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.zoom += 0.01
        if key_pressed[pygame.K_DOWN]:
            self.zoom -= 0.01

    def camera_shake(self, amount, duration):
        self.camera_shake_intensity = amount
        self.camera_shake_duration = duration