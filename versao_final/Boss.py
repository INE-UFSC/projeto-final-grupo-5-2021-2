import pygame
from Enemy import Enemy
from SlugBullet import SlugBullet


class Boss(Enemy, pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo):
        super().__init__(x, y, speed, ammo)
        pygame.sprite.Sprite.__init__(self)
        self.__vision = pygame.Rect(0, 0, 600, 600)

        # sprites
        img = pygame.image.load('assets/Boss.png').convert_alpha()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.__width = self.image.get_width()
        self.__height = self.image.get_height()
        self.health = 300

    @property
    def vision(self):
        return self.__vision

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # End of getters and setters

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.image = pygame.image.load('assets/Boss-dead.png')
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

    def shoot(self, bullet_group):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = SlugBullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery + 60,
                                self.direction)
            bullet.enemy = True
            bullet_group.add(bullet)
            # reduce ammo
            self.ammo -= 1
