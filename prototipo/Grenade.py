import pygame

#load images
#grenade
grenade_img = pygame.image.load('assets/grenade.png')
#explosion
explosion_fr_1 = pygame.image.load('assets/explosion/exp1.png')
explosion_fr_2 = pygame.image.load('assets/explosion/exp2.png')
explosion_fr_3 = pygame.image.load('assets/explosion/exp3.png')
explosion_fr_4 = pygame.image.load('assets/explosion/exp4.png')
explosion_fr_5 = pygame.image.load('assets/explosion/exp5.png')
explosion_animation = [explosion_fr_1, explosion_fr_2, explosion_fr_3, explosion_fr_4, explosion_fr_5]
#create sprite groups

grenade_group = pygame.sprite.Group()


class Grenade(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 75
        self.speed_y = -10
        self.speed_x = 7
        self.image = grenade_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.dx = 0
        self.dy = 0
        self.dmg_player = False
        self.in_air = True
        self.animation_index = 0

    def update(self, game_map, player, enemy_group):
        #move grenade
        if self.in_air:
            gravity = 0.75
            self.speed_y += gravity
            self.dy = self.speed_y  # vertical change
            self.dx = (self.direction * self.speed_x)  # horizontal change

        # check collision with map
        for tile in game_map.tile_list:
            if self.rect.colliderect(tile[1]):
                self.dx = 0
                self.dy = 0
                self.in_air = False
                self.explode(player, enemy_group)

        # update grenade position

        self.rect.x += self.dx
        self.rect.y += self.dy

        # check if grenade has gone off screen
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()

    def explode(self, player, enemy_group):

        self.image = explosion_animation[int(self.animation_index)]
        self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

        if self.rect.colliderect(player.rect) and self.dmg_player is False:
            player.health -= 50
            self.dmg_player = True

        for enemy in enemy_group:
            if self.rect.colliderect(enemy.rect):
                enemy.health -= 100

        self.animation_index += 0.04

        if self.animation_index >= len(explosion_animation):
            self.animation_index = 0
            self.kill()
