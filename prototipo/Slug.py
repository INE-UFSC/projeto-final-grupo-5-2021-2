import pygame
from Grenade import Grenade
from Bullet import Bullet

# slug sprite
slug_img = pygame.image.load('assets/slug_1.png')


class Slug(pygame.sprite.Sprite):
    def __init__(self, x, y, player_health, player_ammo, player_grenade, player_speed):
        super().__init__()
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
        self.speed = 5
        self.ammo = 200
        self.grenade = 5
        self.shoot_cooldown = 0
        self.grenade_thrown = False
        self.direction = 1
        self.vel_y = 0
        self.in_air = True
        self.flip = False
        self.in_slug = False
        self.is_human = False

        # slug action variables
        self.jump = False
        self.moving_left = False
        self.moving_right = False
        self.shooting = False
        self.throwing = False

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            img = pygame.image.load('assets/explosion1.png').convert_alpha()
            self.image = pygame.transform.scale(img, (100, 150))

    def update(self):
        self.check_alive()
        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, game_map):
        # reset movement variables
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if self.moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if self.moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # apply gravity
        if self.in_air:
            self.vel_y += 0.75
            dy += self.vel_y

        for tile in game_map.tile_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground, i.e, jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e, falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

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

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def update_animation(self):
        pass

    def update_action(self, new_action):
        pass
