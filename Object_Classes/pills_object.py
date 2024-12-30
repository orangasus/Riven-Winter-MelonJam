from Object_Classes.base_object import BaseObject
import constants

class Pills(BaseObject):

    ANIMATION_SPEED = 0.1
    MAXIMUM_DISTANCE = 6

    direction = False
    current_distance = 0

    def __init__(self, sprite, position):
        super().__init__(sprite, position, constants.ObjectType.PILLS)

    def update(self):
        super().update()
        step = self.ANIMATION_SPEED
        if self.direction:
            step = -step
        self.move((0, step))
        self.current_distance += step
        if abs(self.current_distance) > self.MAXIMUM_DISTANCE:
            self.direction = not self.direction
            self.current_distance = 0