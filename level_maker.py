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
'''
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
'''
empty_tile_set = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -223, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -224, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 340, 341, 342, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -224, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 364, 365, 366, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -224, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 388, 389, 390, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 223, 0, 0, 0, 0, 0, 0, 0, -224, 0, 0, 0, 250, 0, 322, 0],
[0, 0, 0, 412, 413, 414, 0, 268, 268, 0, 223, 0, 0, 246, 247, 0, 224, 0, 0, 0, 292, 293, 0, 100, 155, 101, 101, 101, 101, 101, 101, 101],
[101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 155, 101, 101, 101, 101, 101, 155, 101, 101, 101, 101, 101, 101, 153, 125, 125, 125, 125, 125, 125, 125, 125],
[125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125],
[125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125],
[125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125],
[125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125]
]
existing_tiles = []
selected_tile = 101
last_tile = (0, 0)

class LevelMaker(Game):

    def refresh_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.SRCALPHA)

    def loop(self):
        global empty_tile_set, selected_tile, last_tile
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

            if not pygame.mouse.get_pressed()[2]:
                last_tile = (0, 0)

            if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
                mouse_tile = (pygame.mouse.get_pos()[1]//32, pygame.mouse.get_pos()[0]//32)
                if mouse_tile[0] >= 0 and mouse_tile[1] >= 0:
                    if mouse_tile[0] <= 17 and mouse_tile[1] < 32:
                        if pygame.mouse.get_pressed()[0]:
                            empty_tile_set[mouse_tile[0]][mouse_tile[1]] = selected_tile
                        if pygame.mouse.get_pressed()[2]:
                            if last_tile != mouse_tile:
                                if empty_tile_set[mouse_tile[0]][mouse_tile[1]] < 0:
                                    empty_tile_set[mouse_tile[0]][mouse_tile[1]] = 0
                                else:
                                    empty_tile_set[mouse_tile[0]][mouse_tile[1]] *= -1
                                last_tile = mouse_tile
                    else:
                        mouse_tile = (mouse_tile[0], mouse_tile[1]+1)
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
                        texture = constants.tile_textures[abs(empty_tile_set[i][j])]
                        if empty_tile_set[i][j] < 0:
                            texture = pygame.transform.scale(texture, (24, 24))
                            self.screen.blit(texture, (j * 32+4, i * 32+4))
                            #texture.set_alpha(25)
                        else:
                            self.screen.blit(texture, (j * 32, i * 32))
                    else:
                        pygame.draw.rect(self.screen, (255, 255, 255), (j * 32+1, i * 32+1, 30, 30))

            for i in range(constants.SPRITESHEET_SIZE):
                for j in range(constants.SPRITESHEET_SIZE):
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
    if i + j * constants.SPRITESHEET_SIZE >= len(existing_tiles):
        return None
    return existing_tiles[i + j * constants.SPRITESHEET_SIZE]

def print_tile_set():
    print("[")
    for i in range(len(empty_tile_set)):
        print("[", end="")
        for j in range(len(empty_tile_set[i])):
            if j != 31:
                print(empty_tile_set[i][j], end=", ")
            else:
                print(empty_tile_set[i][j], end="")
        if i == len(empty_tile_set)-1:
            print("]")
        else:
            print("],")
    print("]")

def start():
    LevelMaker("Level Maker", constants.WIDTH+600, constants.HEIGHT, AudioManager(), VisualManager("Assets/images"), None, fullscreen=False)
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
    #tiles.draw_tile_list(empty_tile_set)

start()
main_menu()
constants.game.loop()
print_tile_set()