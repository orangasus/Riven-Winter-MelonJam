import pygame
from pygame import Vector2
import constants
from enum import Enum
import game
from game import *

<<<<<<< Updated upstream
object_list = [] # stores a list of game objects for easy access


class ObjectType(Enum): # differentiates between types of interactable objects

    GENERIC = 0

    LADDER = 1

    SPIKE = 2
ObjectType = ObjectType.GENERIC
=======
>>>>>>> Stashed changes

# Define our generic object class
# give it all the properties and methods of pygame.sprite.Sprite
class Object(pygame.sprite.Sprite):
<<<<<<< Updated upstream
    def __init__(self, name, sprite,
                 position = (constants.WIDTH/2, constants.HEIGHT/2), ObjectType = 0):
=======
    def __init__(self, name, sprite = None, color = None,
                 position = (constants.CENTER_HEIGHT, constants.CENTER_HEIGHT),):
>>>>>>> Stashed changes
        super(Object, self).__init__()
        self.name = name
        self.position = position
        # load the sprite by using its file location
        self.sprite = pygame.image.load(sprite)
        # adds object to a list of objects
        object_list.append(self)
        # creates the "hit-box"
        self.rect = self.sprite.get_rect()

    def add_object(self):
        object_list.append((self))

    def move(self, direction):
        self.position += direction
        self.rect.topleft = self.position  # Update the rect position

    # updates the sprite
    def update(self):
<<<<<<< Updated upstream
        pygame.sprite.Sprite.update(self)
=======
        pass
>>>>>>> Stashed changes

    # draws the object on the screen
    def draw(self, display_screen):
        # Offset the sprite's position to center it
        centered_position = (self.position[0] - self.rect.width / 2,
                             self.position[1] - self.rect.height / 2)
        display_screen.blit(self.sprite, centered_position)
        print("drew")


    def delete(self):
        object_list.remove(self)

    # decides what happens when an object is interacted with
    def on_interact(self, Object):
        if Object.ObjectType is 3:
            self.delete()
