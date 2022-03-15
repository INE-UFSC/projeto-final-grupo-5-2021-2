import pygame
from Grenade import Grenade
from Bullet import Bullet
from PlayableCharacter import PlayableCharacter

# slug sprite
slug_img = pygame.image.load('assets/slug_1.png')


class Slug(PlayableCharacter, pygame.sprite.Sprite):
    def __init__(self, x, y, player_health, player_ammo, player_grenade, player_speed):
        super().__init__(x, y, 5, 200, 5)
        self.image = pygame.transform.scale(slug_img, (100, 75))
        self.rect = self.image.get_rect(center=(x, y))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # player stats before entering the slug
        self.player_health = player_health
        self.player_ammo = player_ammo
        self.player_grenade = player_grenade
        self.player_speed = player_speed

        # slug stats
        self.alive = True
        self.health = 100
        self.in_slug = False
        self.is_human = False


    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            img = pygame.image.load('assets/explosion1.png').convert_alpha()
            self.image = pygame.transform.scale(img, (100, 150))

    def shoot(self, bullet_group):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 15
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), (self.rect.centery - 12), self.direction, 'slug')
            bullet_group.add(bullet)
            #reduce ammo
            self.ammo -= 1

    def throw_grenade(self, grenade_group):
        if self.grenade_thrown is False and self.grenade > 0:
            self.grenade_thrown = True
            grenade = Grenade(self.rect.centerx + (0.7 * self.rect.size[0] * self.direction),
                                self.rect.top, self.direction)
            grenade_group.add(grenade)
            #reduce grenade
            self.grenade -= 1

    def update_animation(self):
        pass

    def update_action(self, new_action):
        pass
