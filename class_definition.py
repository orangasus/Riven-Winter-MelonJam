
class Object:
    def __init__(self, name, size, position, sprite, is_grouded, is_alive):

    def add_object(self):
        pass

    def draw(self):
        pass

    def destroy(self):
        pass

    def update(self):
        pass

    def on_interact(self):
        pass






class Tile:
    def __init__(self, size, position, is_real, is_lethal, is_climbable, sprite, sound_effect):


class Player(Object):
    def __init__(self):
        super().__init__()

    def move(self):
        pass

    def jump(self):
        pass

    def climb(self):
        pass

    def interact(self):
        pass

class Game:
    def __init__(self, screen, clock, player, objects, audio_manager, visual_manager):
        pass

    def

class Audio_Manager:
    def __init__(self):
        pass

    def play_sound(self):
        pass

