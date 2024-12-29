from Object_Classes.base_object import BaseObject
from pygame.math import Vector2
import pygame, constants

class Player(BaseObject):

    COLOR = (255, 0, 0)
    GRAVITY = 2
    ANIMATION_DELAY = 3

    PLAYER_SPEED = 5
    JUMP_FORCE = 6
    CLIMBING_SPEED = 5
    LADDER_DRAG = 0.5

    def __init__(self, sprite, position, size=(32, 32)):
        super().__init__(sprite, position, constants.ObjectType.PLAYER, size)
        self.velocity = Vector2(0, 0)
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.jumping = False
        self.can_climb = False
        self.hit_count = 0
        constants.game.objects.remove(self)

    def jump(self):
        self.move(Vector2(0, -2))
        self.velocity.y = -self.JUMP_FORCE
        self.animation_count = 0
        self.jump_count += 1
        self.jumping = True
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, direction):
        self.position += direction
        self.rect.x += direction.x
        self.rect.y += direction.y

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
        if not self.can_climb:
            self.velocity.y += min(1, (self.fall_count / constants.FPS) * self.GRAVITY)
        self.move(self.velocity)
        print(self.can_climb)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > constants.FPS * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.handle_move(constants.game.objects)
        self.update_sprite()
        #print(self.velocity)

    def landed(self):
        self.fall_count = 0
        self.velocity.y = 0
        self.jump_count = 0
        self.jumping = False

    def hit_head(self):
        self.hit_count = 0
        self.velocity.y *= -1

    def update_sprite(self):
        pass
        # sprite_sheet = "idle"
        # if self.hit:
        #     sprite_sheet = "hit"
        # elif self.velocity.y < 0:
        #     if self.jump_count == 1:
        #         sprite_sheet = "jump"
        #     elif self.jump_count == 2:
        #         sprite_sheet = "double_jump"
        # elif self.velocity.y > self.GRAVITY * 2:
        #     sprite_sheet = "fall"
        # elif self.velocity.y != 0:
        #     sprite_sheet = "run"
        #
        # sprite_sheet_name = sprite_sheet + "_" + self.direction
        # sprites = self.SPRITES[sprite_sheet_name]
        # sprite_index = (self.animation_count //
        #                 self.ANIMATION_DELAY) % len(sprites)
        # self.sprite = sprites[sprite_index]
        # self.animation_count += 1
        # self.update()

    def collide_vertical(self, objects, dy):
        collided_objects = []
        for obj in objects:
            if obj.object_type == constants.ObjectType.LADDER:
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
        #self.update()
        collided_object = None
        can_climb = False
        for obj in objects:
            if pygame.sprite.collide_rect(self, obj):
                if obj.object_type == constants.ObjectType.LADDER:
                    can_climb = True
                    continue
                collided_object = obj
                break

        #if can_climb and not self.can_climb:
            #self.velocity.y = 0
        self.can_climb = can_climb
        self.move(Vector2(-dx, 0))
        #self.update()
        return collided_object

    def handle_move(self, objects):
        keys = pygame.key.get_pressed()

        self.velocity.x = 0
        collide_left = self.collide_horizontal(objects, -self.PLAYER_SPEED * 2)
        collide_right = self.collide_horizontal(objects, self.PLAYER_SPEED * 2)

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not collide_left:
            self.move_left(self.PLAYER_SPEED)
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not collide_right:
            self.move_right(self.PLAYER_SPEED)


        if self.can_climb:
            if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
                self.velocity.y = -self.CLIMBING_SPEED
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.velocity.y = self.CLIMBING_SPEED
            else:
                self.velocity *= self.LADDER_DRAG
            self.collide_horizontal(objects, -self.PLAYER_SPEED * 2)
            self.collide_horizontal(objects, self.PLAYER_SPEED * 2)
        else:
            if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.jump_count < 2:
                self.jump()

        vertical_collide = self.collide_vertical(objects, self.velocity.y)
        #to_check = [collide_left, collide_right, *vertical_collide]

        # for obj in to_check:
        #     if obj and obj.name == "fire":
        #         self.make_hit()