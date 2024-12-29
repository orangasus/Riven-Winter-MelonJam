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
        self.can_climb = False

        # how hard do you want the gravity to hit
        self.gravity = 0.002
        # how many frames the character is in the air
        self.fall_count = 0

        # horizontal velocity of the player
        self.top_horizontal_velocity = 0.4
        # initial vertical velocity of the player (when jumps)
        self.top_vertical_velocity = 0.4

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
        self.can_climb = self.check_for_ladder_interaction()
        standing_on_ladder = self.check_if_standing_on_ladder()
        print(standing_on_ladder)

        collide_left = self.check_for_horizontal_collisions(-self.top_horizontal_velocity)
        collide_right = self.check_for_horizontal_collisions(self.top_horizontal_velocity)

        collide_top = self.check_for_vertical_collisions(-self.top_vertical_velocity)
        collide_bottom = self.check_for_vertical_collisions(self.top_vertical_velocity)

        if collide_bottom:
            self.on_vertical_collision_bottom(collide_bottom)
        else:
            self.is_grounded = False

        if collide_top:
            self.on_vertical_collision_top(collide_top)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] and self.is_grounded:
            self.jump()

        if keys_pressed[pygame.K_w] and self.can_climb:
            self.climb_up(self.top_vertical_velocity)
        if keys_pressed[pygame.K_s] and self.can_climb and not collide_bottom:
            self.climb_down(self.top_vertical_velocity)

        if keys_pressed[pygame.K_a] and not collide_left:
            self.move_left(self.top_horizontal_velocity)
        if keys_pressed[pygame.K_d] and not collide_right:
            self.move_right(self.top_horizontal_velocity)

    def check_if_standing_on_ladder(self):
        self.move(0, self.top_vertical_velocity)

        for obj in constants.game.objects:
            if pygame.sprite.collide_rect(self, obj):
                if obj.object_type == constants.ObjectType.LADDER:
                    return True

        self.move(0, -self.top_vertical_velocity)
        return False

    def climb_up(self, velocity):
        self.immediate_y_vel = -velocity*constants.game.delta_time

    def climb_down(self, velocity):
        self.immediate_y_vel = velocity*constants.game.delta_time

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
        self.immediate_y_vel = 0.01
        self.rect.top = other.rect.bottom

    # prevents player from 'moving into the obstacles'
    # checks if the player is colliding and returning the collide object
    # otherwise player passes through an obstacle after a few key presses
    def check_for_horizontal_collisions(self, dx):
        # preemptively moving the player
        self.move(dx, 0)
        collided_object = None

        for obj in constants.game.objects:
            if obj == self or obj.object_type == constants.ObjectType.LADDER:
                continue
            if pygame.sprite.collide_rect(self, obj):
                collided_object = obj
                break

        # moving the player back
        self.move(-dx, 0)
        return collided_object

    def check_for_ladder_interaction(self):
        for obj in constants.game.objects:
            if pygame.sprite.collide_rect(self, obj):
                if obj.object_type == constants.ObjectType.LADDER:
                    return True
        return False

    def check_for_vertical_collisions(self, dy):
        self.move(0, dy)
        collided_object = None

        for obj in constants.game.objects:
            if obj == self or obj.object_type == constants.ObjectType.LADDER:
                continue
            if pygame.sprite.collide_rect(self, obj):
                collided_object = obj
                break

        self.move(0, -dy)
        return collided_object