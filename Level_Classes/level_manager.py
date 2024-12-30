import constants, pygame
import Object_Classes.tile_class as tiles
from Visual_Effects.effects import CircleScreenTransition, BlockScreenTransition
from Visual_Effects.flash import Flash
from Visual_Effects.pills_effect import TakePills

flash_effect = Flash((50, 0, 0, 50), 80, 40, flash_duration = 35)
pills_effect = TakePills(3000)

class LevelManager:

    def __init__(self, levels_list, main_menu):
        self.levels = levels_list
        self.current_level = -1
        self.current_scene = 0
        self.main_menu = main_menu

        self.level_transition = BlockScreenTransition(60, (0, 0, 0), 100, on_finish=self.load_level)
        self.scene_transition = CircleScreenTransition(60, (0, 0, 0), 50, 70, 8, 1, on_finish=self.load_scene)

    def load_level(self):
        self.current_scene = 0
        self.load_scene()

    def load_scene(self):
        game = constants.game
        game.objects.clear()
        game.decorations.clear()
        scene = self.levels[self.current_level].scenes[self.current_scene]
        game.background = pygame.transform.scale(scene.background, (constants.WIDTH, constants.HEIGHT))

        tiles.draw_tile_list(scene.tiles)
        game.player.set_position(scene.player_position)
        game.player.transition = False
        if not game.took_pills:
            flash_effect.start()
        if scene.on_load:
            scene.on_load()

    def restart_scene(self):
        self.scene_transition.direction = 0
        self.scene_transition.start()

    def next_scene(self):
        self.current_scene += 1
        if self.current_scene >= len(self.levels[self.current_level].scenes):
            self.next_level()
        else:
            self.scene_transition.direction = 1
            self.scene_transition.start()

    def previous_scene(self):
        self.current_scene -= 1
        if self.current_scene < 0:
            self.current_scene = 0
            self.previous_level()
        else:
            self.scene_transition.direction = 0
            self.scene_transition.start()

    def next_level(self):
        self.current_level += 1
        if self.current_level >= len(self.levels):
            self.take_pills()
        else:
            print("LEVEL: ", self.current_level)
            self.level_transition.direction = 1
            self.level_transition.start()

    def previous_level(self):
        self.current_level -= 1
        if self.current_level < 0:
            self.current_level = 0
            self.main_menu()
        else:
            self.level_transition.direction = 0
            self.level_transition.start()

    def take_pills(self):
        pills_effect.start()
        constants.game.player.transition = False
        constants.game.took_pills = True

    def finish(self):
        pass
