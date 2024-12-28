import pygame
from pygame import *
import random
# Initialize pygame
pygame.init()
# Initialize pygame mixer
pygame.mixer.init()

# set sound files
run_sound = pygame.mixer.Sound('audiofile/footstep1.wav')
jump_sound = pygame.mixer.Sound('audiofile/jump.wav')
run_sound.set_volume(0.1)

#overall music for the game havent decided yet
#pygame.mixer.music.load('audiofile/videoplayback2.wav')
#pygame.mixer.music.play(-1)

# Define the Audio_Manager class
class Audio_Manager:
    def __init__(self, sounds):
        sounds = [run_sound, jump_sound]
        self.sounds = sounds
    
    def play_sound(self, file):
        pygame.mixer.Sound.play(file)
    
    def stop_sound(self):
        pygame.mixer.Sound.stop()

    def play_music(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    
    def stop_music(self):
        pygame.mixer.music.stop()

#Testing player movement with audio and sound (tmr will try lol)
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

surface = pygame.Surface((40, 40))

pygame.display.set_caption('window')

class Base():
    def __init__(self, x, y, velocity, size):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.size = size

    def draw(self):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.size, self.size))

    
class Player(Base):
    def __init__(self, x, y, velocity, size):
        super().__init__(x, y, velocity, size)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.velocity
            run_sound.play()
        elif keys[pygame.K_d]:
            self.x += self.velocity
            run_sound.play()
        elif keys[pygame.K_s]:
            self.y += self.velocity
            run_sound.play()
        elif keys[pygame.K_w]:
            self.y -= self.velocity
            run_sound.play()
        elif keys[pygame.K_SPACE]:
            jump_sound.play()

player = Player(400, 300, 5, 40)

gamerun = True
while gamerun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False
    
    player.move()
    player.draw()
    pygame.display.update()

    window.fill((0, 0, 0))

pygame.quit()