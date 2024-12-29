import pygame

import constants
from Object_Classes.base_object import BaseObject


class Player(BaseObject):
    def __init__(self, sprite, position, object_type):
        super().__init__(sprite, position, object_type)
        self.mask = pygame.mask.from_surface(self.sprite)

        self.alive = True

        # has player already collided with the ceiling
        self.hit_head_already = False

        self.position = position

        # is player on the ground currently
        self.is_grounded = False

        # is player midair at the moment
        self.is_midair = True

        # was space already pressed - prevents from jumping while holding space
        self.space_pressed = False

        # how hard do you want the gravity to hit
        self.gravity = 0.02

        # horizontal velocity of the player
        self.top_horizontal_velocity = 0.4
        # initial vertical velocity of the player (when jumps)
        self.top_vertical_velocity = 0.5
        self.top_climb_velocity = 0.2
        # what is the velocity of the player in given frame (moment)
        self.immediate_x_vel = 0
        self.immediate_y_vel = 0

        # objects player is currently colliding with except for ladders
        self.currently_collides = {'left': None, 'right': None,
                                   'top': None, 'bottom': None}
        # ladders player is currently colliding with
        self.cur_ladder_collides = {'left': None, 'right': None,
                                    'top': None, 'bottom': None}

    def sprite_update(self):
        self.rect = self.sprite.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.sprite)

    def jump(self):
        self.is_grounded = False
        self.is_midair = True
        self.immediate_y_vel = -self.top_vertical_velocity*constants.game.delta_time

    def land(self, other):
        self.rect.bottom = other.rect.top
        self.is_grounded = True
        self.is_midair = False
        self.hit_head_already = False
        self.immediate_y_vel = 0
        #
        if self.currently_collides['left'] or self.currently_collides['right']:
            self.immediate_x_vel = 0

    def hit_head(self):
        if not self.hit_head_already:
            self.hit_head_already = True
            self.rect.top = self.currently_collides['top'].rect.bottom
            self.immediate_y_vel *= -1

    def move_right(self):
        self.immediate_x_vel = (self.top_horizontal_velocity
                                * constants.game.delta_time)

    def move_left(self):
        self.immediate_x_vel = (-self.top_horizontal_velocity
                                * constants.game.delta_time)

    def climb_up(self):
        self.is_grounded = False
        self.is_midair = False
        self.immediate_y_vel = -self.top_climb_velocity * constants.game.delta_time

    def climb_down(self):
        self.is_grounded = False
        self.is_midair = False
        self.immediate_y_vel = self.top_climb_velocity * constants.game.delta_time

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

        if keys_pressed[pygame.K_w] and self.check_for_any_ladder_collisions() and not self.currently_collides['top']:
            self.climb_up()

        if keys_pressed[pygame.K_s] and self.cur_ladder_collides['bottom'] and not self.currently_collides['bottom']:
            self.climb_down()

        if keys_pressed[pygame.K_a] and not self.currently_collides['left']:
            self.move_left()

        if keys_pressed[pygame.K_d] and not self.currently_collides['right']:
            self.move_right()

    def print_ladder_collisions(self):
        collisions = []
        for direction, obj in self.cur_ladder_collides.items():
            if obj is None:
                collisions.append(f"{direction}: None")
            else:
                collisions.append(f"{direction}: {obj.object_type}")
        print(" | ".join(collisions))

    def apply_gravity(self):
        self.immediate_y_vel += min(1, constants.game.delta_time * self.gravity)

    def movement_update(self):
        self.immediate_x_vel = 0

        self.get_cur_collision_info()
        self.get_cur_ladder_collision_info()
        self.handle_collisions()

        self.player_controls()

        if self.is_midair:
            self.apply_gravity()
        self.move(self.immediate_x_vel, self.immediate_y_vel)

    def check_for_spikes(self):
        for v in self.currently_collides.values():
            if v is not None:
                if v.object_type == constants.ObjectType.SPIKE:
                    self.die()
                    break

    def handle_collisions(self):
        self.check_for_spikes()
        self.is_midair = True
        if self.currently_collides['bottom']:
            if self.is_midair:
                self.land(self.currently_collides['bottom'])

        if self.cur_ladder_collides['bottom']:
            if self.cur_ladder_collides['top'] is None and self.cur_ladder_collides['right'] is None \
                    and self.cur_ladder_collides['left'] is None:
                if self.is_midair:
                    self.land(self.cur_ladder_collides['bottom'])

        if self.currently_collides['top']:
            self.hit_head()

    def check_for_any_ladder_collisions(self):
        for obj in constants.game.objects:
            if obj.object_type == constants.ObjectType.LADDER:
                if pygame.sprite.collide_rect(self, obj):
                    return True

    def get_cur_ladder_collision_info(self):
        self.cur_ladder_collides['left'] = self.check_ladder_collision_left()
        self.cur_ladder_collides['right'] = self.check_ladder_collision_right()
        self.cur_ladder_collides['top'] = self.check_ladder_collision_top()
        self.cur_ladder_collides['bottom'] = self.check_ladder_collision_bottom()

    def check_ladder_collision_base(self, dx, dy):
        original_pos = self.position.copy()
        self.move(dx, dy)
        collide_obj = None
        for obj in constants.game.objects:
            if obj.object_type == constants.ObjectType.LADDER:
                if pygame.sprite.collide_rect(self, obj):
                    collide_obj = obj
                    break
        self.position = original_pos
        self.rect.center = self.position
        return collide_obj

    def check_ladder_collision_bottom(self):
        return self.check_ladder_collision_base(0, self.top_vertical_velocity + 1)

    def check_ladder_collision_top(self):
        return self.check_ladder_collision_base(0, -self.top_vertical_velocity)

    def check_ladder_collision_left(self):
        return self.check_ladder_collision_base(-self.top_horizontal_velocity, 0)

    def check_ladder_collision_right(self):
        return self.check_ladder_collision_base(self.top_horizontal_velocity, 0)

    def get_cur_collision_info(self):
        self.currently_collides['right'] = self.get_collision_right()
        self.currently_collides['left'] = self.get_collision_left()
        self.currently_collides['top'] = self.get_collision_top()
        self.currently_collides['bottom'] = self.get_collision_bottom()

    def get_collision_right(self):
        return self.get_collision_base(self.immediate_x_vel+1, 0)

    def get_collision_top(self):
        return self.get_collision_base(0, self.immediate_x_vel-1)

    def get_collision_bottom(self):
        return self.get_collision_base(0, self.immediate_y_vel + 1)

    def get_collision_left(self):
        return self.get_collision_base(-self.top_horizontal_velocity, 0)

    def print_collision_info(self):
        collisions = []
        for direction, obj in self.currently_collides.items():
            if obj is None:
                collisions.append(f"{direction}: None")
            else:
                collisions.append(f"{direction}: {obj.object_type}")
        print(" | ".join(collisions))

    def get_collision_base(self, dx, dy):
        original_pos = self.position.copy()
        self.move(dx, dy)
        collide_obj = None
        for obj in constants.game.objects:
            if obj == self or obj.object_type == constants.ObjectType.LADDER:
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
        # self.print_ladder_collisions()
        # self.print_collision_info()
        self.movement_update()
        self.sprite_update()
