import pygame

#load images
#grenade
grenade_img = pygame.image.load('assets/grenade.png')
#explosion
explosion_img = pygame.image.load('assets/explosion.png')
#create sprite groups
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()




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

    def update(self, game_map, player, enemy_group):
        #move grenade
        gravity = 0.75
        self.speed_y += gravity
        dy = self.speed_y #vertical change
        dx = (self.direction * self.speed_x) #horizontal change

        # check collision with floor
        for tile in game_map.tile_list:
            #check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            #check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if below the ground, i.e, jumping
                if self.speed_y < 0:
                    self.speed_y = 0
                    dy = tile[1].bottom - self.rect.top
                #check if above the ground, i.e, falling
                elif self.speed_y >= 0:
                    self.speed_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        #update grenade position
        self.rect.x += dx
        self.rect.y += dy

        #check if grenade has gone off screen
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()

        #countdown timer
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explode = Explosion(self.rect.x, self.rect.y)
            explosion_group.add(explode)
            #do daamge to anyone that is nearby
            if abs(self.rect.centerx - player.rect.centerx) < game_map.tile_size * 2 and \
                abs(self.rect.centery - player.rect.centery) < game_map.tile_size * 2:
                player.health -= 50
            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < game_map.tile_size * 2 and \
                    abs(self.rect.centery - enemy.rect.centery) < game_map.tile_size * 2:
                    enemy.health -= 50


class Explosion(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.duration = 2
        self.counter = 0
        self.done = False

    def update(self, player, explosion_group, enemy_group):

        self.counter += 1
        if self.counter >= self.duration:
            self.counter = 0
            self.kill()
            self.done = True

        if self.done is False:
            #check if player take dmg
            if abs(self.rect.centerx - player.rect.centerx) < 30 and abs(self.rect.centery - player.rect.centery) < 30:
                if player.alive:
                    player.health -= 50
                    print(player.health)

            #check if enemy take dmg
            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < 30 and abs(self.rect.centery - enemy.rect.centery) < 30:
                    if enemy.alive:
                        enemy.health -= 50
                        print(enemy.health)





