import pygame

# Define the Audio_Manager class
class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sfx = {}
        self.music = {}



        # overall music for the game havent decided yet (4 musicfiles to choose from)
        self.mainmusic = pygame.mixer.music.load('Assets/audio/music/mm1.wav')
        self.levelmusic = pygame.mixer.music.load('Assets/audio/music/Lanterns.wav')
        pygame.mixer.music.play(-1)

        # define sound effects dictionary
        self.sfx = {
        }

        # define music dictionary
        self.music = {
            'mainmusic': self.mainmusic,
        }

    def play_sound(self, sfx):
        self.sfx[sfx].play()

    def stop_sound(self, sfx):
        self.sfx[sfx].stop()

    def play_music(self, music):
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()