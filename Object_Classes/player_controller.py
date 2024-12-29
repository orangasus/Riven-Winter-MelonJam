import pygame
from pygame.sprite import collide_rect

import constants
from Object_Classes.base_object import BaseObject


class Player(BaseObject):
    def __init__(self, sprite, position, object_type):
        super().__init__(sprite, position, object_type)
        self.mask = pygame.mask.from_surface(self.sprite)

        self.alive = True

        self.can_climb = True

        self.position = position

        # is player on the ground currently
        self.is_grounded = False

        # is player mid-jump at the moment
        self.is_jumping = False

        self.space_pressed = False

        self.is_midair = True

        # how hard do you want the gravity to hit
        self.gravity = 0.002

        # horizontal velocity of the player
        self.top_horizontal_velocity = 0.4
        # initial vertical velocity of the player (when jumps)
        # 0.4
        self.top_vertical_velocity = 0.5

        # what is the velocity of the player in given frame (moment)
        self.immediate_x_vel = 0
        self.immediate_y_vel = 0

        self.currently_collides = {'left': None, 'right': None,
                                   'top': None, 'bottom': None}

    def sprite_update(self):
        self.rect = self.sprite.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.sprite)

    def jump(self):
        self.is_grounded = False
        self.is_midair = True
        self.immediate_y_vel = -self.top_vertical_velocity

    def hit_head(self):
        self.rect.top = self.currently_collides['top'].rect.bottom
        self.immediate_y_vel *= -1

    def land(self):
        self.rect.bottom = self.currently_collides['bottom'].rect.top
        self.is_grounded = True
        self.is_midair = False
        self.immediate_y_vel = 0
        #
        if self.currently_collides['left'] or self.currently_collides['right']:
            self.immediate_x_vel = 0
            print("Landed. Position:", self.position)

    def move_right(self):
        self.immediate_x_vel = (self.top_horizontal_velocity
                                * constants.game.delta_time)

    def move_left(self):
        self.immediate_x_vel = (-self.top_horizontal_velocity
                                * constants.game.delta_time)

    def climb_up(self):
        self.is_grounded = False
        self.immediate_y_vel = -self.top_vertical_velocity

    def move(self, dx, dy):
        self.position.x += dx
        self.position.y += dy
        self.rect.center = self.position

    def player_controls(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE]:
            if self.is_grounded and not self.space_pressed and not self.is_midair:
                self.jump()
                self.space_pressed = True

        if not keys_pressed[pygame.K_SPACE]:
            self.space_pressed = False

        if keys_pressed[pygame.K_w] and self.can_climb:
            self.climb_up()

        if keys_pressed[pygame.K_a] and not self.currently_collides['left']:
            self.move_left()

        if keys_pressed[pygame.K_d] and not self.currently_collides['right']:
            self.move_right()

    def apply_gravity(self):
        self.immediate_y_vel += min(1, constants.game.delta_time * self.gravity)

    def movement_update(self):
        self.immediate_x_vel = 0

        self.get_cur_collision_info()
        print(self.currently_collides)
        self.handle_collisions()

        self.player_controls()

        if self.is_midair or not self.can_climb:
            self.apply_gravity()
        self.move(self.immediate_x_vel, self.immediate_y_vel)

    def check_for_spikes(self):
        for v in self.currently_collides.values():
            if v is not None:
                if v.object_type == constants.ObjectType.SPIKE:
                    self.die()
                    break

    def check_for_ladders(self):
        for v in self.currently_collides.values():
            if v is not None:
                if v.object_type == constants.ObjectType.LADDER:
                    self.can_climb = True
                    return
        self.can_climb = False


    def handle_collisions(self):
        self.check_for_spikes()
        if self.currently_collides['bottom']:
            if self.is_midair:
                self.land()
        else:
            self.is_midair = True

        self.check_for_ladders()

        if self.currently_collides['top']:
            self.hit_head()

    def get_cur_collision_info(self):
        self.currently_collides['right'] = self.get_collision_right()
        self.currently_collides['left'] = self.get_collision_left()
        self.currently_collides['top'] = self.get_collision_top()
        self.currently_collides['bottom'] = self.get_collision_bottom()

    def get_collision_right(self):
        original_pos = self.position.copy()
        self.move(self.top_horizontal_velocity, 0)
        collide_obj = None
        for obj in constants.game.objects:
            if obj == self:
                continue
            if pygame.sprite.collide_rect(self, obj):
                collide_obj = obj
                break
        self.position = original_pos
        self.rect.center = self.position
        return collide_obj

    def get_collision_top(self):
        original_pos = self.position.copy()
        self.move(0, -self.top_vertical_velocity)
        collide_obj = None
        for obj in constants.game.objects:
            if obj == self:
                continue
            if pygame.sprite.collide_rect(self, obj):
                collide_obj = obj
                break
        self.position = original_pos
        self.rect.center = self.position
        return collide_obj

    def get_collision_bottom(self):
        original_pos = self.position.copy()
        self.move(0, self.top_vertical_velocity)
        collide_obj = None
        for obj in constants.game.objects:
            if obj == self:
                continue
            if pygame.sprite.collide_rect(self, obj):
                collide_obj = obj
                break
        self.position = original_pos
        self.rect.center = self.position
        return collide_obj

    def get_collision_left(self):
        original_pos = self.position.copy()
        self.move(-self.top_horizontal_velocity, 0)
        collide_obj = None
        for obj in constants.game.objects:
            if obj == self:
                continue
            if pygame.sprite.collide_rect(self, obj):
                collide_obj = obj
                break
        self.position = original_pos
        self.rect.center = self.position
        return collide_obj

    def die(self):
        self.is_alive = False
        self.die()

    def update(self):
        self.movement_update()
        self.sprite_update()
