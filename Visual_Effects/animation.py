import pygame


class SpriteSheet:

    def __init__(self, image, width, height, frame_duration, scale=None, color = None):
        self.sheet = image
        self.width = width
        self.height = height
        self.scale = scale
        self.color = color
        self.frame_duration = frame_duration
        self.last_frame_time = 0
        self.frame = 0
        self.length = (self.sheet.get_width() // self.width)
        self.frames = []
        for i in range(self.length):
            self.frames.append(self.get_image(i))

    def get_image(self, frame):
        image = pygame.Surface((self.width, self.height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * self.width), 0, self.width, self.height))
        if self.scale:
            image = pygame.transform.scale(image, self.scale)
        if self.color:
            image.set_colorkey(self.color)

        return image

    def start_animation(self):
        self.last_frame_time = 0
        self.frame = 0

    def get_current_frame(self, time):
        if time - self.last_frame_time > self.frame_duration:
            self.last_frame_time = time
            self.frame = (self.frame+1) % self.length
        return self.frames[self.frame]

    def flip(self):
        self.frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]

