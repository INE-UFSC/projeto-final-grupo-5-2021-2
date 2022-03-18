import pygame
from Bullet import Bullet

slug_bullet_img = pygame.image.load('assets/slug_bullet.png')


class SlugBullet(Bullet, pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        pygame.sprite.Sprite.__init__(self)
        self.image = slug_bullet_img
        self.rect = self.image.get_rect()
        if self.direction < 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.center = (x, y)
