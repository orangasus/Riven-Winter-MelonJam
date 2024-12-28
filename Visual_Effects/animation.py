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
        self.columns = (self.sheet.get_width() // self.width)
        self.rows = (self.sheet.get_height() // self.height)
        self.frames = []
        for j in range(self.rows):
            self.frames.append([])
            for i in range(self.columns):
                self.frames[j].append(self.get_image(i, j, self.width, self.height, self.scale, self.color))

    def get_image(self, x, y, width, height, scale, color=None):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((x * width), (y * height), width, height))
        if scale:
            image = pygame.transform.scale(image, (scale.x, scale.y))
        if color:
            image.set_colorkey(color)

        return image

    def start_animation(self):
        self.last_frame_time = 0
        self.frame = 0

    def get_current_frame(self, time):
        if time - self.last_frame_time > self.frame_duration:
            self.last_frame_time = time
            self.frame = (self.frame+1) % self.columns
        return self.frames[0][self.frame]

    def flip(self):
        for i in range(len(self.frames)):
            for j in range(len(self.frames[i])):
                self.frames[i][j] = pygame.transform.flip(self.frames[i][j], True, False)
