import pygame

#load images
#bullet
bullet_img = pygame.image.load('assets/bullet.png')
slug_bullet_img = pygame.image.load('assets/slug_bullet.png')

#create sprite groups
bullet_group = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.__speed = 10
        self.__direction = direction
        self.__enemy = False
    
    @property
    def speed(self):
        return self.__speed
        
    @speed.setter
    def speed(self, new_speed: int):
        if isinstance(new_speed, int):
            self.__speed = new_speed
    
    @property
    def direction(self):
        return self.__direction
        
    @direction.setter
    def direction(self, new_direction: int):
        if isinstance(new_direction, int):
            self.__direction = new_direction
    
    @property
    def enemy(self):
        return self.__enemy
        
    @enemy.setter
    def enemy(self, new_enemy: bool):
        if isinstance(new_enemy, bool):
            self.__enemy = new_enemy

# End of getters and setters

    def update(self, player, bullet_group, enemy_group, screen_scroll, level):
        # move bullet
        self.rect.x += (self.direction * self.speed) + screen_scroll

        # check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()

        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive and self.enemy:
                player.health -= 5 * level
                self.kill()

        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive and self.enemy is False:
                    enemy.health -= 25
                    print(enemy.health)
                    self.kill()
