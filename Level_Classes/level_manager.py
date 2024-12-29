import constants
import Object_Classes.tile_class as tiles
from Visual_Effects.effects import CircleScreenTransition

class LevelManager:

    def __init__(self, levels_list):
        self.levels = levels_list
        self.current_level = -1
        self.current_scene = 0

        self.level_transition = CircleScreenTransition(60, (255, 255, 255), 50, 70, 8, 1, self.load_level)
        self.scene_transition = CircleScreenTransition(60, (255, 255, 255), 50, 70, 8, 1, self.load_scene)

    def load_level(self):
        constants.game.objects.clear()
        constants.game.decorations.clear()
        self.current_scene = 0
        self.load_scene()

    def load_scene(self):
        constants.game.objects.clear()
        constants.game.decorations.clear()
        scene = self.levels[self.current_level].scenes[self.current_scene]
        constants.game.background = scene.background
        tiles.draw_tile_list(scene.tiles)
        constants.game.player.set_position(scene.player_position)

    def next_scene(self):
        self.current_scene += 1
        if self.current_scene >= len(self.levels[self.current_level].scenes):
            self.next_level()
        else:
            self.scene_transition.direction = 0
            self.scene_transition.start()

    def previous_scene(self):
        self.current_scene -= 1
        if self.current_scene < 0:
            self.current_scene = 0
            self.previous_level()
        else:
            self.scene_transition.direction = 1
            self.scene_transition.start()

    def next_level(self):
        self.current_level += 1
        if self.current_level >= len(self.levels):
            self.win()
        else:
            self.level_transition.direction = 0
            self.level_transition.start()

    def previous_level(self):
        self.current_level -= 1
        if self.current_level < 0:
            self.current_level = 0
        else:
            self.level_transition.direction = 1
            self.level_transition.start()

    def win(self):
        constants.game.gameOn = False
