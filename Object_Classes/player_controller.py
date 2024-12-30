import pygame
from pygame.math import Vector2

import constants
from Object_Classes.base_object import BaseObject


class Player(BaseObject):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    ANIMATION_DELAY = 3

    PLAYER_SPEED = 3
    JUMP_FORCE = 4
    CLIMBING_SPEED = 2
    LADDER_DRAG = 0.5

    def __init__(self, sprite, position, size=(32, 32), offset=(0, 0), idle_animation=None, walk_animation=None, jump_animation=None,
                 climb_animation=None, die_animation=None):
        super().__init__(sprite, position, constants.ObjectType.PLAYER, size, register=False, offset=offset)
        self.velocity = Vector2(0, 0)
        self.mask = None
        self.direction = "right"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.jumping = False
        self.can_climb = False
        self.hit_count = 0

        self.idle_animation = idle_animation
        self.walk_animation = walk_animation
        self.jump_animation = jump_animation
        self.climb_animation = climb_animation
        self.die_animation = die_animation

        self.play_animation(self.idle_animation)

    def jump(self):
        self.move(Vector2(0, -2))
        self.velocity.y = -self.JUMP_FORCE
        self.animation_count = 0
        self.jump_count += 1
        self.jumping = True
        self.on_animation_finish = self.animation_finished
        self.play_animation(self.jump_animation)
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, direction):
        self.position += direction
        self.rect.x += direction.x
        self.rect.y += direction.y

    def set_position(self, new_position):
        self.position = new_position
        self.rect.center = new_position

    def make_hit(self):
        self.hit = True

    def move_left(self, vel):
        self.velocity.x = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.velocity.x = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def update(self):
        if self.hit:
            self.update_sprite()
            return
        if not self.can_climb:
            self.velocity.y += min(1, (self.fall_count / constants.FPS) * self.GRAVITY)
        self.move(self.velocity)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > constants.FPS * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.handle_move(constants.game.objects)
        self.update_sprite()

        #if self.position.y > constants.HEIGHT:
        #    self.make_hit()

    def landed(self):
        self.fall_count = 0
        self.velocity.y = 0
        self.jump_count = 0
        self.jumping = False

    def hit_head(self):
        self.hit_count = 0
        self.velocity.y *= -1

    def update_sprite(self):
        animation = self.idle_animation
        if self.hit:
            animation = self.die_animation
            self.on_animation_finish = self.death
        else:
            if not self.can_climb:
                if self.velocity.y < 0:
                    animation = self.jump_animation
                # elif self.velocity.y > self.GRAVITY * 2:
                #     sprite_sheet = "fall"
                elif self.velocity.x != 0:
                    animation = self.walk_animation
            else:
                if self.velocity.y != 0:
                    animation = self.climb_animation
                else:
                    animation = None
        if self.animation != animation:
            self.play_animation(animation)

    def is_out_of_bounds_left(self, dx):
        check = False
        self.move(Vector2(-dx, 0))
        if self.position.x <= 5:
            check = True

        self.move(Vector2(dx, 0))
        return check

    def is_out_of_bounds_right(self, dx):
        check = False
        self.move(Vector2(dx, 0))
        if self.position.x >= constants.WIDTH - 5:
            check = True

        self.move(Vector2(-dx, 0))
        return check

    def collide_vertical(self, objects, dy):
        collided_objects = []
        for obj in objects:
            if obj.object_type in constants.climable:
                continue
            if pygame.sprite.collide_rect(self, obj):
                if dy > 0:
                    self.rect.bottom = obj.rect.top
                    self.landed()
                elif dy < 0:
                    if self.jumping:
                        if obj.rect.bottom < self.rect.bottom:
                            self.rect.top = obj.rect.bottom
                        self.hit_head()

                collided_objects.append(obj)

        return collided_objects

    def collide_horizontal(self, objects, dx):
        self.move(Vector2(dx, 0))
        # self.update()
        collided_object = None
        can_climb = False
        for obj in objects:
            if pygame.sprite.collide_rect(self, obj):
                if obj.object_type in constants.climable:
                    can_climb = True
                    continue
                elif obj.object_type in constants.deadly:
                    self.make_hit()
                elif obj.object_type == constants.ObjectType.NEXT_SCREEN_TRANSITION:
                    constants.game.level_manager.next_scene()
                elif obj.object_type == constants.ObjectType.PREVIOUS_SCREEN_TRANSITION:
                    constants.game.level_manager.previous_scene()
                collided_object = obj
                break

        # if can_climb and not self.can_climb:
        # self.velocity.y = 0
        self.can_climb = can_climb
        self.move(Vector2(-dx, 0))
        # self.update()
        return collided_object

    def get_ground(self):
        self.move(Vector2(0, 2))
        for obj in constants.game.objects:
            if pygame.sprite.collide_rect(self, obj):
                return obj
        self.move(Vector2(0, -2))
        return None


    def handle_move(self, objects):
        keys = pygame.key.get_pressed()

        self.velocity.x = 0
        collide_left = self.collide_horizontal(objects, -self.PLAYER_SPEED * 2)
        collide_right = self.collide_horizontal(objects, self.PLAYER_SPEED * 2)

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not collide_left and not self.is_out_of_bounds_left(self.PLAYER_SPEED):
            self.move_left(self.PLAYER_SPEED)
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not collide_right and not self.is_out_of_bounds_right(self.PLAYER_SPEED):
            self.move_right(self.PLAYER_SPEED)

        if self.can_climb:
            if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
                self.velocity.y = -self.CLIMBING_SPEED
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.velocity.y = self.CLIMBING_SPEED
            else:
                self.velocity *= self.LADDER_DRAG
                if abs(self.velocity.y) < 0.01:
                    self.velocity.y = 0
            self.collide_horizontal(objects, -self.PLAYER_SPEED * 2)
            self.collide_horizontal(objects, self.PLAYER_SPEED * 2)
        else:
            if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]):
                if self.jump_count < 2:
                    self.jump()
                else:
                    ground = self.get_ground()
                    if ground and ground.object_type in constants.climable:
                        self.jump_count = 0

        vertical_collide = self.collide_vertical(objects, self.velocity.y)
        # to_check = [collide_left, collide_right, *vertical_collide]

        # for obj in to_check:
        #     if obj and obj.name == "fire":
        #         self.make_hit()

    def play_animation(self, animation):
        if animation:
            if (self.direction == "left" and not animation.flipped) or (
                    self.direction == "right" and animation.flipped):
                animation.flip()
        self.animation = animation

    def animation_finished(self):
        self.play_animation(self.idle_animation)
        self.on_animation_finish = None

    def death(self):
        if self.hit:
            self.hit = False
            self.on_animation_finish = None
            self.play_animation(self.idle_animation)
            self.set_position(Vector2(0, 0))
            constants.game.level_manager.restart_scene()
