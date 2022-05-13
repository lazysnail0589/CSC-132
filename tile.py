import pygame
from settings import *
from entity import Entity
from support import *
#from Character import character
#from main import Game

class Tile(pygame.sprite.Sprite):
     def __init__(self,pos,groups,sprite_type, surface = pygame.Surface((TILESIZE,TILESIZE))):
         super().__init__(groups)
         self.sprite_type = sprite_type
         self.image = pygame.image.load(r'C:\Users\Javen\PycharmProjects\pythonProject\dirt2.png').convert_alpha()

         self.rect = self.image.get_rect(topleft = pos)
         self.hitbox = self.rect.inflate(0,20)

class Coin(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
         super().__init__(groups)
         self.image = pygame.image.load(r'C:\Users\Javen\PycharmProjects\pythonProject\venv\coinandpeach\coin1.png').convert_alpha()

         self.rect = self.image.get_rect(topleft = pos)
         self.hitbox = self.rect.inflate(0,20)



    #def coin_collision(self):
        #if character.player.hitbox.colliderect(self.hitbox):
            #del self.image
            #Game.score += 1

