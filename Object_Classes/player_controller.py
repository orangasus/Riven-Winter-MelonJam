import pygame
from Object_Classes.base_object import BaseObject
import constants



# pygame.sprite.Sprite for 'pixel-perfect collisions'
class Player(BaseObject):
    def __init__(self, sprite, position, object_type):
        super().__init__(sprite, position, object_type)
        self.mask = pygame.mask.from_surface(self.sprite)

        self.position = position

        # which direction is player currently facing
        self.facing_direction = 'right'

        # is player on the ground currently
        self.is_grounded = False
        # is player alive
        self.is_alive = True
        # is player climbing at the moment
        self.is_climbing = False

        # how hard do you want the gravity to hit
        self.gravity = 0.001
        # how many frames the character is in the air
        self.fall_count = 0

        # horizontal velocity of the player
        self.top_horizontal_velocity = 1
        # initial vertical velocity of the player (when jumps)
        self.top_vertical_velocity = 0.5

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
        self.immediate_x_vel = 0

        collide_left = self.check_for_horizontal_collisions(-self.top_horizontal_velocity)
        collide_right = self.check_for_horizontal_collisions(self.top_horizontal_velocity)

        collide_top = self.check_for_vertical_collisions(self.top_vertical_velocity)
        collide_bottom = self.check_for_vertical_collisions(-self.top_vertical_velocity)

        if collide_bottom:
            self.on_vertical_collision_bottom(collide_bottom)
        else:
            self.is_grounded = False

        if collide_top:
            self.on_vertical_collision_bottom(collide_top)

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

        self.immediate_x_vel = -velocity*constants.game.delta_time
        self.facing_direction = 'left'

    def flip_sprite_horiz(self):
        self.sprite = pygame.transform.flip(self.sprite, True, False)

    # move player right once
    def move_right(self, velocity):
        if self.facing_direction == 'left':
            self.flip_sprite_horiz()

        self.immediate_x_vel = velocity*constants.game.delta_time
        self.facing_direction = 'right'

    # general update function for the player, handles all movements
    def movement_update(self):
        print('is grounded', self.is_grounded)
        # get user input for this frame
        self.player_controls()

        # if midair then apply gravity
        if not self.is_grounded:
            self.immediate_y_vel += min(1, constants.game.delta_time * self.gravity)
            self.fall_count += 1

        self.move(self.immediate_x_vel, self.immediate_y_vel)

    def update(self):
        self.movement_update()
        self.sprite_update()

    # what happens to player on vertical collision from below
    def on_vertical_collision_bottom(self, other):
        self.immediate_y_vel = 0
        self.fall_count = 0
        self.is_grounded = True
        self.rect.bottom = other.rect.top

    # what happens to player on vertical collision from above
    def on_vertical_collision_top(self, other):
        # making the player bounce back
        self.immediate_y_vel *= -1
        self.rect.top = other.rect.bottom

    # prevents player from 'moving into the obstacles'
    # checks if the player is colliding and returning the collide object
    # otherwise player passes through an obstacle after a few key presses
    def check_for_horizontal_collisions(self, dx):
        # preemptively moving the player
        self.move(dx, 0)
        collided_object = None

        for obj in constants.game.objects:
            if obj == self:
                continue
            if pygame.sprite.collide_rect(self, obj):
                collided_object = obj
                break

        # moving the player back
        self.move(-dx, 0)
        return collided_object

    def check_for_vertical_collisions(self, dy):
        self.move(0, dy)
        collided_object = None

        for obj in constants.game.objects:
            if obj == self:
                continue
            if pygame.sprite.collide_rect(self, obj):
                collided_object = obj
                break

        self.move(0, -dy)
        return collided_object


    # draws the player
    def draw(self):
        constants.game.screen.blit(self.sprite, self.rect.topleft)

    def climb_up(self):
        pass

    def climb_down(self):
        pass

    def interact(self, other):
        pass


# def on_y_collision():
#     if pygame.sprite.collide_rect(player, ground):
#         player.on_vertical_collision_bottom(ground)
#     if pygame.sprite.collide_rect(player, ceiling):
#         player.on_vertical_collision_top(ceiling)
#
#
# def flip_sprite(sprite):
#     return pygame.transform.flip(sprite, True, False)


# screen = pygame.display.set_mode((700, 700))
# player = Player((50, 50), pygame.Vector2(300, 100))
# ground = Object((350, 600), (700, 50))
# wall = Object((50, 500), (50, 400))
# ceiling = Object((500, 300), (200, 50))
# game_objects = [ground, ceiling, wall]
# running = True
# fps = 60
# clock = pygame.time.Clock()
# while running:
#     clock.tick(fps)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     on_y_collision()
#     screen.fill((255, 255, 255))
#     ground.draw()
#     ceiling.draw()
#     wall.draw()
#     player.draw()
#     player.update()
#     pygame.display.flip()
# pygame.quit()
