import pygame
from settings import *
from tile import Tile
from Character import character
from debug import debug


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # sprite group setups
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(PLAIN):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = character((x,y),[self.visible_sprites],self.obstacle_sprites)

    def run(self):
        self.visible_sprites.custom_draw()
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        #self.half_width = self.display_surface.get_surface()[0]//2
        #self.half_height = self.display_surface.get_surface()[0] // 2
        self.offset = pygame.math.Vector2(-10,10)

    def custom_draw(self):
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image,offset_pos)