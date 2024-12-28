import pygame
from pygame import Vector2
import constants
from enum import Enum

# Define our generic object class
# give it all the properties and methods of pygame.sprite.Sprite
class Object(pygame.sprite.Sprite):
    def __init__(self, name, sprite = None, color = None,
                 position = (constants.WIDTH/2, constants.HEIGHT/2), ObjectType = 0):
        super(Object, self).__init__()
        self.name = name
        self.position = position
                     
        # creates the visible texture
        self.sprite = pygame.image.load(sprite)
        
        # creates the "hit-box"
        self.rect = self.sprite.get_rect(center=self.position)

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
    def draw(self):
        # Offset the sprite's position to center it
        constants.game.screen.blit(self.sprite, self.rect.topleft - constants.game.camera)

    def delete(self):
        constants.game.objects.remove(self)

    # decides what happens when an object is interacted with
    def on_interact(self, Object):
        if Object.ObjectType == 3:
            self.delete()
