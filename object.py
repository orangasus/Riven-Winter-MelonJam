import pygame
from pygame import Vector2
import constants

# Define our generic object class
# give it all the properties and methods of pygame.sprite.Sprite
class Object(pygame.sprite.Sprite):
    def __init__(self, name, size = (25, 25), position = (constants.WIDTH/2, constants.HEIGHT/2), velocity = (0, 10), sprite = None, color = None):
        super(Object, self).__init__()
        # name such as "player", "enemy", "bullet", "spike"
        self.name = name
        self.position = position
        self.size = size
        # creates the visible texture (sprite / rectangle)
        if sprite:
            # loads the sprite and scales it to the size
            self.surf = pygame.transform.scale(pygame.image.load(sprite), size)
        else:
            # creates a rectangle
            self.surf = pygame.Surface(size)
            # sets color
            self.surf.fill(color if color else (200, 200, 200))

        self.velocity = velocity
        
        # creates the "hit-box"
        self.rect = self.surf.get_rect(center=self.position)

        # adds object to a list of objects
        self.add_object()

    def add_object(self):
        constants.game.objects.append(self)

    def move(self, direction):
        self.position += direction
        self.rect.center = self.position # Update the rect position

    def update(self):
        pass

    def draw(self):
        constants.game.screen.blit(self.surf, self.position)

    def delete(self):
        constants.game.objects.remove(self)
