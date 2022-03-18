import pygame

#load images
#bullet
bullet_img = pygame.image.load('assets/bullet.png')
slug_bullet_img = pygame.image.load('assets/slug_bullet.png')

#create sprite groups
bullet_group = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, type):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.direction = direction
        self.enemy = False
        self.type = type

        #check who is shooting
        if self.type == 'human':
            self.image = bullet_img
        if self.type == 'slug':
            self.image = slug_bullet_img
            if self.direction < 0:
                self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, player, bullet_group, enemy_group):
        #move bullet
        self.rect.x += (self.direction * self.speed)

        #check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()

        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive and self.enemy:
                player.health -= 5
                self.kill()

        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive and self.enemy is False:
                    enemy.health -= 25
                    print(enemy.health)
                    self.kill()
