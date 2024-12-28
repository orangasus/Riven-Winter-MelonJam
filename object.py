import pygame
from pygame import Vector2
import constants

object_list = []
import pygame

# Define our generic object class
# give it all the properties and methods of pygame.sprite.Sprite
class Object(pygame.sprite.Sprite):
    def __init__(self, name, size = (25, 25), position = (constants.WIDTH/2, constants.HEIGHT/2), velocity = (0, 10), ):
        super(Object, self).__init__()
        # name such as "player", "enemy", "bullet", "spike"
        self.name = name
        self.position = position
        # creates the visible texture
        self.surf = pygame.Surface(size)
        self.velocity = velocity
        # sets color
        self.surf.fill((200, 200, 200))
        # creates the "hit-box"
        self.rect = self.surf.get_rect(center=self.position)
        # adds object to a list of objects
        object_list.append(self)

    def add_object(self):
        object_list.append((self))
    def move(self, direction):
        self.position += direction
        self.rect.center = self.position # Update the rect position

    def update(self):
        pass

    def draw(self, display_screen):
        display_screen.blit(self.surf, self.position)

    def delete(self):
        object_list.remove(self)
