import pygame
from settings import *
from entity import Entity
from support import *


class Enemy(Entity):
    def __init__(self, groups):
        super().__init__(groups)
        self.can_attack = None

    def __int__(self, enemy_name, pos, groups, obstacle_sprites, damage_player):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics
        self.import_graphics(enemy_name)
        self.status = 'still'
        self.image = self.animations[self.status][self.frame_index]

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # stats
        self.enemy_name = enemy_name
        enemy_info = enemy_data[self.enemy_name]
        self.health = enemy_info['health']
        self.speed = enemy_info['speed']
        self.attack_radius = enemy_info['attack_radius']
        self.notice_radius = enemy_info['notice_radius']
        self.attack_type = enemy_info['attack_type']
        self.attack_damage = enemy_info['damage']
        self.resistance = enemy_info['resistance']

        self.damage_player = damage_player
        #self.can_attack = True
        #self.attack_time = None

        #self.vulnerable = True
        #self.hit_time = None

    def import_graphics(self):
        self.animations = {'still': [], 'flap': [], 'attack': []}
        main_path = f'../venv/monsters/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'flap'
        else:
            self.status = 'still'

    # def actions(self, player):
    #     if self.status == 'attack':
    #         self.attack_time = pygame.time.get_ticks()
    #         self.damage_player(self.attack_damage, self.attack_type)
    #     elif self.status == 'flap':
    #         self.direction = self.get_player_distance_direction(player)[1]
    #     else:
    #         self.direction = pygame.math.Vector2()

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    # def get_damage(self, player, attack_type):
    #     if self.vulnerable:
    #         self.direction = self.get_player_distance_direction(player)[1]
    #         if attack_type == 'rush':
    #             self.health -= player.get_full_weapon_damage()
    #         else:
    #             pass
    #
    #         self.hit_time = pygame.time.get_ticks()
    #         self.vulnerable = False

    def check_death(self):
        if self.health <= 0:
            self.kill()

    # def hit_reaction(self):
    #     if not self.vunerable:
    #         self.direction *= -self.resistance

    def update(self):
       # self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.check_death()

    def enemy_update(self, player):
        self.get_status(player)
        #self.actions(player)
