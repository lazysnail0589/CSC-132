import pygame
from settings import *


class character(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(r'C:\Users\Javen\PycharmProjects\pythonProject\venv\bulldogstill.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 5
        self.direction = pygame.math.Vector2()
        self.obstacle_sprites = obstacle_sprites
        self.is_jumping = False
        self.is_falling = False

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
        else:
            self.direction.y = 0
    def jump(self):
        if(self.is_jumping is False):
            self.is_falling = False
            self.is_jumping = True
    def gravity(self):
        if(self.is_jumping):
            self.direction.y +=1
    def move(self,speed):
        if self.direction.magnitude() !=0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        #self.rect.center += self.direction * speed

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
    def update(self):
        self.input()
        self.move(self.speed)
        #ground_hit_list = pygame.sprite.spritecollide(self)

        if (self.is_jumping and self.is_falling is False):
            self.is_falling = True
            self.direction.y -= .5