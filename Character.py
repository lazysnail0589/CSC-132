import pygame
from settings import *
from support import import_folder


class character(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        #character creation
        self.animation_steps = 7
        self.animation_cooldown = 500

        self.image = pygame.image.load(r'C:\Users\Javen\PycharmProjects\pythonProject\venv\1dog\1dog.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        #graphics
        self.import_character_assets()
        self.status = '1dog'
        self.frame_index = 0
        self.animation_speed = 0.15

        self.speed = 5
        self.direction = pygame.math.Vector2()
        self.obstacle_sprites = obstacle_sprites

        #jump
        self.gravity = 0.5
        self.jump_height = -1

    def import_character_assets(self):
        character_path = '../pythonProject/venv/'
        self.animations = {'1dog': [],'2dog': [], '3dog': [],
                           '4dog': [],'5dog': [],
                           '6dog': [],'7dog': []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
            print(self.animations)

    def get_status(self):
        if self.direction.x == 0 and self.direction.y ==0:
            #if not '1dog' in self.status:
            self.status = '1dog'

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = '6dog'

            print("left")
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            print("right")
            self.status = '3dog'
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
            self.status = '4dog'
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
    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)
        self.apply_gravity()
