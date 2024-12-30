import constants, pygame, random
from pygame.locals import *
pygame.init()

class VisualEffect:

    def start(self):
        constants.game.effects.append(self)

    def stop(self):
        constants.game.effects.remove(self)

    def update(self):
        pass

    def draw(self):
        pass

    def flash(self):
        red_tint = self # pygame.Surface(sprite.get_size(), flags=pygame.SRCALPHA)
        red_tint.fill((255, 255, 255, 128))  # (R, G, B, A) with semi-transparency # Blit the red-tinted surface onto the sprite sprite.blit(red_tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.blit(red_tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

class BlockScreenTransition(VisualEffect):

    def __init__(self, speed, color, direction, on_finish):
        self.speed = speed
        self.color = color
        self.position = 0
        self.direction = direction
        self.step = 0
        self.on_finish = on_finish

    def start(self):
        super().start()
        self.position = 0

    def update(self):
        self.position += self.speed
        if self.position > constants.WIDTH:
            if self.step == 0:
                self.step = 1
                self.on_finish()
                self.position = 0
            else:
                self.stop()

    def draw(self):
        screen = constants.game.screen
        if self.direction == 0:
            if self.step == 0:
                pygame.draw.rect(screen, self.color, (0, 0, self.position, constants.HEIGHT))
            else:
                pygame.draw.rect(screen, self.color, (self.position, 0, constants.WIDTH- self.position, constants.HEIGHT))
        else:
            if self.step == 0:
                pygame.draw.rect(screen, self.color, (constants.WIDTH - self.position, 0, self.position, constants.HEIGHT))
            else:
                pygame.draw.rect(screen, self.color, (0, 0, constants.WIDTH - self.position, constants.HEIGHT))

circle_offsets = [(0, 0), (1, 0), (0, 1), (1, 1)]

class CircleScreenTransition(VisualEffect):
    def __init__(self, speed, color, radius, distance, random_variation, direction, on_finish):
        self.speed = speed
        self.color = color
        self.radius = radius
        self.distance = distance
        self.random_variation = random_variation
        self.density = int(constants.WIDTH / distance) + 1
        self.position = 0
        self.direction = direction
        self.step = 0
        self.on_finish = on_finish
        self.offsets = self._generate_offsets()

    def _generate_offsets(self):
        """Generate consistent offsets for the circle positions."""
        random.seed(42)  # Use a fixed seed for reproducibility
        offsets = {}
        for i in range(self.density):
            for j in range(self.density):
                offsets[(i, j)] = (
                    random.uniform(-self.random_variation, self.random_variation),
                    random.uniform(-self.random_variation, self.random_variation),
                )
        return offsets

    def start(self):
        super().start()
        self.step = 0
        self.position = 0

    def update(self):
        self.position += self.speed
        if self.position > constants.WIDTH * 2:
            if self.step == 0:
                self.step = 1
                self.on_finish()
                self.position = 0
            else:
                self.stop()

    def draw(self):
        screen = constants.game.screen
        half_radius = self.radius / 2
        if self.direction == 0:
            if self.step == 0:
                for i in range(self.density):
                    for j in range(self.density):
                        offset_x, offset_y = self.offsets[(i, j)]
                        x = half_radius + i * self.distance + offset_x
                        y = half_radius + j * self.distance + offset_y
                        radius = self.radius * ((self.position - i * self.radius) / constants.WIDTH)
                        pygame.draw.circle(screen, self.color, (x, y), radius)
            else:
                for i in range(self.density):
                    for j in range(self.density):
                        offset_x, offset_y = self.offsets[(i, j)]
                        x = half_radius + i * self.distance + offset_x
                        y = half_radius + j * self.distance + offset_y
                        radius = self.radius - self.radius * ((self.position - i * self.radius) / constants.WIDTH)
                        pygame.draw.circle(screen, self.color, (x, y), radius)
        else:
            if self.step == 0:
                for i in range(self.density):
                    for j in range(self.density):
                        offset_x, offset_y = self.offsets[(i, j)]
                        x = constants.WIDTH - half_radius - i * self.distance + offset_x
                        y = half_radius + j * self.distance + offset_y
                        radius = self.radius * ((self.position - i * self.radius) / constants.WIDTH)
                        pygame.draw.circle(screen, self.color, (x, y), radius)
            else:
                for i in range(self.density):
                    for j in range(self.density):
                        offset_x, offset_y = self.offsets[(i, j)]
                        x = constants.WIDTH - half_radius - i * self.distance + offset_x
                        y = half_radius + j * self.distance + offset_y
                        radius = self.radius - self.radius * ((self.position - i * self.radius) / constants.WIDTH)
                        pygame.draw.circle(screen, self.color, (x, y), radius)