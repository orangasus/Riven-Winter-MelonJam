from game_class import Game
import pygame
import constants
from Managers.audio_manager import AudioManager
from Managers.visual_manager import VisualManager
from Object_Classes.player_controller import Player
from Object_Classes.ui import Button
from Visual_Effects.animation import SpriteSheet
from Visual_Effects.effects import CircleScreenTransition
import Object_Classes.tile_class as tiles
from levels import level_1

empty_tile_set = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

existing_tiles = []
selected_tile = 10

class LevelMaker(Game):

    def loop(self):
        global empty_tile_set, selected_tile
        while self.gameOn:
            self.delta_time = self.clock.tick_busy_loop()
            self.time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.gameOn = False
                    elif event.key == pygame.K_F11:
                        self.fullscreen = not self.fullscreen
                        self.refresh_screen()
                if event.type == pygame.QUIT:
                    self.gameOn = False

            if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
                mouse_tile = (pygame.mouse.get_pos()[1]//32, pygame.mouse.get_pos()[0]//32)
                if mouse_tile[0] >= 0 and mouse_tile[1] >= 0:
                    if mouse_tile[0] <= 17 and mouse_tile[1] < 32:
                        if pygame.mouse.get_pressed()[0]:
                            empty_tile_set[mouse_tile[0]][mouse_tile[1]] = selected_tile
                        if pygame.mouse.get_pressed()[2]:
                            empty_tile_set[mouse_tile[0]][mouse_tile[1]] = 0
                    else:
                        if mouse_tile[0] <= 17:
                            tt = get_existing_tile(mouse_tile[1]-32, mouse_tile[0])
                            if tt:
                                selected_tile = tt[0]

            self.screen.fill((0, 0, 0))
            if self.background:
                self.screen.blit(self.background, (0, 0))

            for i in range(len(empty_tile_set)):
                for j in range(len(empty_tile_set[i])):
                    if empty_tile_set[i][j] != 0:
                        self.screen.blit(constants.tile_textures[empty_tile_set[i][j]], (j * 32, i * 32))
                    else:
                        pygame.draw.rect(self.screen, (255, 255, 255), (j * 32+1, i * 32+1, 30, 30))

            for i in range(14):
                for j in range(14):
                    tile = get_existing_tile(i, j)
                    if tile:
                        self.screen.blit(tile[1], (constants.WIDTH + i * 32, j * 32))

            self.camera.update()
            for obj in self.objects:
                obj.update()
                obj.draw()


            for effect in self.effects:
                effect.update()
                effect.draw()


            pygame.display.flip()

def get_existing_tile(i, j):
    if i + j * 14 >= len(existing_tiles):
        return None
    return existing_tiles[i + j * 14]

def print_tile_set():
    print("[")
    for i in range(len(empty_tile_set)):
        print("[", end="")
        for j in range(len(empty_tile_set[i])):
            if j != 31:
                print(empty_tile_set[i][j], end=", ")
            else:
                print(empty_tile_set[i][j])
        if i == len(empty_tile_set)-1:
            print("]")
        else:
            print("],")
    print("]")

def start():
    LevelMaker("Level Maker", constants.WIDTH+600, constants.HEIGHT, AudioManager(), VisualManager("Assets/images"), fullscreen=False)
    constants.set_tile_textures()
    global existing_tiles
    ignore_textures = [0, 1, 2, 3, 4, 5]
    for name, texture in constants.tile_textures.items():
        if name in ignore_textures:
            continue
        existing_tiles.append((name, texture))

def main_menu():
    game = constants.game
    game.objects.clear()
    #game.camera.target = player
    tiles.draw_tile_list(empty_tile_set)

start()
main_menu()
constants.game.loop()
print_tile_set()