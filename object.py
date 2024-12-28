import pygame
from pygame import Vector2
import constants
from enum import Enum

# Differentiates between types of interactable objects
class ObjectType(Enum):

    GENERIC = 0

    LADDER = 1

    SPIKE = 2
ObjectType = ObjectType.GENERIC

# Define our generic object class
# give it all the properties and methods of pygame.sprite.Sprite
class Object(pygame.sprite.Sprite):
    def __init__(self, name, sprite = None, color = None,
                 position = (constants.WIDTH/2, constants.HEIGHT/2), size = (25, 25), ObjectType = 0):
        super(Object, self).__init__()
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
        
        # creates the "hit-box"
        self.rect = self.surf.get_rect(center=self.position)

        # adds object to a list of objects
        self.add_object()

    def add_object(self):
        constants.game.objects.append(self)

    def move(self, direction):
        self.position += direction
        self.rect.center = self.position # Update the rect position

    # updates the sprite
    def update(self):
        pygame.sprite.Sprite.update(self)
     
    # draws the object on the screen
    def draw(self, display_screen):
        # Offset the sprite's position to center it
        centered_position = (self.position[0] - self.rect.width / 2,
                             self.position[1] - self.rect.height / 2)
        display_screen.blit(self.surf, centered_position)

    def delete(self):
        constants.game.objects.remove(self)

    # decides what happens when an object is interacted with
    def on_interact(self, Object):
        if Object.ObjectType is 3:
            self.delete()
