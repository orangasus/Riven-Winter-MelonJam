import os, pygame

image_formats = ['.png', '.jpg']

class VisualManager:

    def __init__(self, path):
        self.path = path
        self.sprites = {}
        self._load_images()

    def _load_images(self):
        for root, dir, images in os.walk(self.path):
            for image in images:
                if image[-4:] in image_formats:
                    self.sprites[image[:-4]] = pygame.image.load(os.path.join(root, image)).convert_alpha()

