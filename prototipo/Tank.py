import pygame
from Enemy import Enemy
from Bullet import Bullet

exp_fr_1 = pygame.image.load('assets/tank_exp/exp_fr1.png')
exp_fr_2 = pygame.image.load('assets/tank_exp/exp_fr2.png')
exp_fr_3 = pygame.image.load('assets/tank_exp/exp_fr3.png')
exp_fr_4 = pygame.image.load('assets/tank_exp/exp_fr4.png')
exp_fr_5 = pygame.image.load('assets/tank_exp/exp_fr5.png')
exp_fr_6 = pygame.image.load('assets/tank_exp/exp_fr6.png')
exp_fr_7 = pygame.image.load('assets/tank_exp/exp_fr7.png')

explosion_animation = [exp_fr_1, exp_fr_2, exp_fr_3, exp_fr_4, exp_fr_5, exp_fr_6, exp_fr_7]


class Tank(Enemy, pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo):
        super().__init__(x, y, speed, ammo)
        pygame.sprite.Sprite.__init__(self)
        self.vision = pygame.Rect(0, 0, 300, 20)

        # sprites
        img = pygame.image.load('assets/enemy_tank.png').convert_alpha()
        self.image = pygame.transform.scale(img, (75, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.image = explosion_animation[int(self.animation_index)]
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
            self.animation_index += 0.2
            if self.animation_index >= len(explosion_animation):
                self.animation_index = 0
                self.kill()

    def shoot(self, bullet_group):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.9 * self.rect.size[0] * self.direction), self.rect.centery - 20, self.direction, 'slug')
            bullet.enemy = True
            bullet_group.add(bullet)
            # reduce ammo
            self.ammo -= 1
