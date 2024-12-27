import pygame


class Player():
    def __init__(self, size, position):

        self.is_grounded = True
        self.is_alive = True
        self.is_climbing = False

        self.gravity = 1.0
        self.fall_count = 0

        self.x_velocity = 0.0
        self.y_velocity = 0.0

        self.size = size
        self.position = position

        self.hit_box = pygame.Rect((0, 0), size)
        self.hit_box.center = position

    def move(self,dx, dy):
        self.position.x += dx
        self.position.y += dy

    def update(self):
        self.y_velocity += min(1, (self.fall_count/fps) * self.gravity)
        self.fall_count += 1
        self.hit_box.center = self.position
        self.move(self.x_velocity, self.y_velocity)

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.hit_box)

    def climb_up(self):
        pass

    def climb_down(self):
        pass

    def interact(self, other):
        pass


screen = pygame.display.set_mode((700, 700))
player = Player((50, 50), pygame.Vector2(300, 100))
running = True
fps = 60
clock = pygame.time.Clock()
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    player.draw()
    player.update()
    pygame.display.flip()
pygame.quit()
