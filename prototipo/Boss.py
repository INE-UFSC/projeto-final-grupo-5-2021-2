import pygame
from Enemy import Enemy


class Boss(Enemy, pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo):
        super().__init__(x, y, speed, ammo)
        pygame.sprite.Sprite.__init__(self)

        # sprites
        #img = pygame.image.load('assets/EnemyBadAss.png').convert_alpha()
        #self.image = pygame.transform.scale(img, (89, 77))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.__width = self.image.get_width()
        self.__height = self.image.get_height()
    
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            # img = pygame.image.load('assets/').convert_alpha()
            #self.image = pygame.transform.scale(img, (89, 77))
