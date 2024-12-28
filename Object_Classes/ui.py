from Object_Classes.base_object import BaseObject
from constants import ObjectType
import pygame

class Clickable(BaseObject):

    hover = False
    clicked = False

    def update(self):
        BaseObject.update(self)
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            if not self.hover:
                self.hover = True
                self.on_hover()
        elif self.hover:
            self.hover = False
            self.clicked = False
            self.on_hover_stop()

        if self.hover:
            if pygame.mouse.get_pressed()[0]:
                if not self.clicked:
                    self.clicked = True
                    self.on_click()
            elif self.clicked:
                self.clicked = False
                self.on_click_release()

    def on_hover(self):
        pass

    def on_hover_stop(self):
        pass

    def on_click(self):
        pass

    def on_click_release(self):
        pass

class Button(Clickable):

    def __init__(self, sprite, sprite_hover, sprite_clicked, position, size, on_press):
        super(Button, self).__init__(sprite, position, ObjectType.UI, size)

        self.on_press = on_press

        self.sprite_normal = self.sprite
        self.sprite_hover = pygame.transform.scale(sprite_hover, size)
        self.sprite_clicked = pygame.transform.scale(sprite_clicked, size)


    def on_hover(self):
        self.sprite = self.sprite_hover

    def on_hover_stop(self):
        self.sprite = self.sprite_normal

    def on_click(self):
        self.sprite = self.sprite_clicked
        self.draw()
        
    def on_click_release(self):
        self.sprite = self.sprite_hover
        self.on_press()
