import pygame
from Enemy import Enemy


class Rebel(Enemy, pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo):
        super().__init__(x, y, speed, ammo)
        pygame.sprite.Sprite.__init__(self)

        # sprites
        img = pygame.image.load('assets/RebelSoldier.png').convert_alpha()
        self.image = pygame.transform.scale(img, (89, 77))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            img = pygame.image.load('assets/RebelSoldier_dead.png').convert_alpha()
            self.image = pygame.transform.scale(img, (89, 77))
