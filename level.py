import pygame
from settings import *
from tile import Tile
from Character import character
from Grass import *
from debug import debug
from enemy import Enemy
from support import *

class Level:

     def __init__(self):
         self.display_surface = pygame.display.get_surface()
         # sprite group setups
         self.visible_sprites = YSortCameraGroup()
         self.obstacle_sprites = pygame.sprite.Group()

         self.current_attack = None
         self.attack_sprites = pygame.sprite.Group()
         self.attackable_sprites = pygame.sprite.Group()

         self.create_map()

     def kill(self):
         pygame.sprite.Sprite.kill(self.player)


     def create_map(self):
         for row_index,row in enumerate(PLAIN):
             for col_index, col in enumerate(row):
                 x = col_index * TILESIZE
                 y = row_index * TILESIZE

                 if col == 'x':
                     Tile((x,y), [self.visible_sprites,self.obstacle_sprites], 'object')
                 if col == 'p':
                     self.player = character((x,y),[self.visible_sprites],self.obstacle_sprites)
                 if col == 'g':
                     grass((x,y), [self.visible_sprites,self.obstacle_sprites])
                 if col == 'w':
                     water((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 'b':
                     bridge((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 'bb':
                     break_bridge((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 't':
                     bottom((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 'bl':
                     bottomleft((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 'l':
                     left((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 'r':
                     right((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 'gblt':
                     gbottomlefttop((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 'glt':
                     glefttop((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 'gt':
                     gtop((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 'gtr':
                    gtopright((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if col == 'c':
                    Coin((x, y), [self.visible_sprites, self.obstacle_sprites])
                 if(col == 'e'):
                     pass
                 #self.hit = pygame.sprite.spritecollide(self.player,water((x, y), [self.visible_sprites, self.obstacle_sprites]), True, True)

                 #if self.hit:
                 #    self.kill()

     def damage_player(self,amount,attack_type):
         if self.player.vulnerable:
             self.player.health -=amount
             self.player.vulnerable = False
             self.player.hurt_time = pygame.time.get_ticks()





     def run(self):
         self.visible_sprites.custom_draw(self.player)
         self.visible_sprites.update()
         debug(self.player.get_status())


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.floor_surf = pygame.image.load(r'C:\Users\Javen\PycharmProjects\pythonProject\venv\background(2).png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self,player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)


