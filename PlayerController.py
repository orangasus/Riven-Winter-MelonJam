import pygame


# pygame.sprite.Sprite for 'pixel-perfect collisions'
class Player(pygame.sprite.Sprite):
    def __init__(self, size, position):
        super().__init__()
        # collision hitbox of the player - use sprite_mask for sprite perfect hitbox
        self.sprite = pygame.image.load('Player_Assets/lmao_sprite.png').convert_alpha()
        self.rect = self.sprite.get_rect()
        self.rect.center = position

        #
        self.mask = pygame.mask.from_surface(self.sprite)

        self.size = size
        self.position = position

        # color of the player rect?
        self.color = (255, 0, 0)

        # which direction is player currently facing
        self.facing_direction = 'right'

        # is player on the ground currently
        self.is_grounded = False
        # is player alive
        self.is_alive = True
        # is player climbing at the moment
        self.is_climbing = False

        # how hard do you want the gravity to hit
        self.gravity = 10
        # how many frames the character is in the air
        self.fall_count = 0

        # horizontal velocity of the player
        self.top_horizontal_velocity = 10
        # initial vertical velocity of the player (when jumps)
        self.top_vertical_velocity = 20

        # what is the velocity of the player in given frame (moment)
        self.immediate_x_vel = 0
        self.immediate_y_vel = 0

    def sprite_update(self):
        self.rect = self.sprite.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.sprite)

    # initiates jumping motion
    def jump(self):
        self.is_grounded = False
        self.immediate_y_vel = -self.top_vertical_velocity

    # move the player based on coordinates changes
    def move(self, dx, dy):
        self.position.x += dx
        self.position.y += dy
        self.rect.center = self.position

    # registers user keyboard input
    def player_controls(self):
        # make not 0 for inertia movement
        self.immediate_x_vel = 0

        collide_left = self.check_for_horizontal_collisions(-self.top_horizontal_velocity)
        collide_right = self.check_for_horizontal_collisions(self.top_horizontal_velocity)
        if collide_right:
            print(collide_right)
        if collide_left:
            print(collide_left)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] and self.is_grounded:
            self.jump()
        if keys_pressed[pygame.K_a] and not collide_left:
            self.move_left(self.top_horizontal_velocity)
        if keys_pressed[pygame.K_d] and not collide_right:
            self.move_right(self.top_horizontal_velocity)

    # move player left once
    def move_left(self, velocity):
        if self.facing_direction == 'right':
            self.flip_sprite_horiz()

        self.immediate_x_vel = -velocity
        self.facing_direction = 'left'

    def flip_sprite_horiz(self):
        self.sprite = pygame.transform.flip(self.sprite, True, False)

    # move player right once
    def move_right(self, velocity):
        if self.facing_direction == 'left':
            self.flip_sprite_horiz()

        self.immediate_x_vel = velocity
        self.facing_direction = 'right'

    # general update function for the player, handles all movements
    def movement_update(self):
        # get user input for this frame
        self.player_controls()

        # if midair then apply gravity
        if not self.is_grounded:
            self.immediate_y_vel += min(1, (self.fall_count / fps) * self.gravity)
            self.fall_count += 1

        self.move(self.immediate_x_vel, self.immediate_y_vel)

    def update(self):
        self.movement_update()
        self.sprite_update()

    # what happens to player on vertical collision from below
    def on_vertical_collision_bottom(self, other):
        print('bottom collision')
        self.immediate_y_vel = 0
        self.fall_count = 0
        self.is_grounded = True
        self.rect.bottom = other.rect.top

    # what happens to player on vertical collision from above
    def on_vertical_collision_top(self, other):
        print('vertical collision')
        # making the player bounce back
        self.immediate_y_vel *= -1
        self.rect.top = other.rect.bottom

    # prevents player from 'moving into the obstacles'
    # checks if the player is colliding and returning the collide object
    # otherwise player passes through an obstacle after a few key presses
    def check_for_horizontal_collisions(self, dx):
        # preemptively moving the player
        player.move(dx, 0)
        collided_object = None
        # checking if player hits anything
        # !! should replace with game objects list
        if pygame.sprite.collide_rect(player, wall):
            collided_object = wall
        # moving the player back
        player.move(-dx, 0)
        return collided_object

    # draws the player
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.sprite, self.rect.topleft)

    def climb_up(self):
        pass

    def climb_down(self):
        pass

    def interact(self, other):
        pass


class Object(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.rect.center = position

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)


def on_y_collision():
    if pygame.sprite.collide_rect(player, ground):
        player.on_vertical_collision_bottom(ground)
    if pygame.sprite.collide_rect(player, ceiling):
        player.on_vertical_collision_top(ceiling)


def flip_sprite(sprite):
    return pygame.transform.flip(sprite, True, False)


screen = pygame.display.set_mode((700, 700))
player = Player((50, 50), pygame.Vector2(300, 100))
ground = Object((350, 600), (700, 50))
wall = Object((50, 500), (50, 400))
ceiling = Object((500, 300), (200, 50))
game_objects = [ground, ceiling, wall]
running = True
fps = 60
clock = pygame.time.Clock()
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    on_y_collision()
    screen.fill((255, 255, 255))
    ground.draw()
    ceiling.draw()
    wall.draw()
    player.draw()
    player.update()
    pygame.display.flip()
pygame.quit()
