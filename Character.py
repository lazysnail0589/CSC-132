import pygame
from settings import *
from support import import_folder
from entity import Entity
from tile import Tile

class character(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.import_character_assets()
        #character creation



        self.image = self.animations['still'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        #graphics
        self.import_character_assets()
        self.status = 'still'


        self.speed = 8
        self.direction = pygame.math.Vector2(0,0)
        self.obstacle_sprites = obstacle_sprites

        #jump
        self.gravity = 0.8
        self.jump_height = -1

        #champ stats
        self.stats ={'health': 100, 'damaghurte': 100,'speed': 8}
        self.health = self.stats['health'] * 0.5
        self.speed = self.stats['speed']

        self.vulnerable = True
        self.hurt_time = None




    def import_character_assets(self):
        character_path = '../pythonProject/venv/'
        self.animations = {'still': [],'run': [], 'jump': [],
                           'fall': []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
            print(self.animations)

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 2:
            self.status = 'fall'
            print(self.direction.y)

        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'still'

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            print("left")
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            print("right")
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
            print("space")
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_height




    #collisions
    def move(self,speed):
        if self.direction.magnitude() !=0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center


    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.get_status()
        self.animate()
        self.move(self.speed)
        self.apply_gravity()


