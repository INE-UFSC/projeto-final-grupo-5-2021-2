import pygame
from Bullet import Bullet

# bullet image
bullet_img = pygame.image.load('assets/bullet.png')


class RegularBullet(Bullet, pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        if self.direction < 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.center = (x, y)