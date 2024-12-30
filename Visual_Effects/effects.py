<<<<<<< HEAD
import constants, pygame, random
from pygame.locals import *
pygame.init()
=======
import constants, pygame, random, math
>>>>>>> 0443c97dba37ed84c0db308b04ffb767bf8ebc58

class VisualEffect:

    def start(self):
        constants.game.effects.append(self)

    def stop(self):
        constants.game.effects.remove(self)

    def update(self):
        pass

    def draw(self):
        pass

    def flash(self, object_to_flash):
        red_tint = pygame.Surface(object_to_flash.sprite.get_size(), flags=pygame.SRCALPHA)
        red_tint.fill((255, 255, 255, 128))
        object_to_flash.blit(red_tint, object_to_flash.position, special_flags=pygame.BLEND_RGBA_MULT)

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

def create_vignette(width, height, intensity=255):
    vignette_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    center_x, center_y = width // 2, height // 2
    max_distance = math.sqrt(center_x**2 + center_y**2)

    for y in range(height):
        for x in range(width):
            # Calculate distance from the center
            dx = x - center_x
            dy = y - center_y
            distance = math.sqrt(dx**2 + dy**2)

            # Determine alpha based on inverted distance
            alpha = min(int((distance / max_distance) * intensity), intensity)
            vignette_surface.set_at((x, y), (0, 0, 0, alpha))

    return vignette_surface

class Vignette(VisualEffect):

    def __init__(self, intensity):
        self.vignette = create_vignette(constants.WIDTH, constants.HEIGHT, intensity)

    def draw(self):
        constants.game.screen.blit(self.vignette, (0, 0))