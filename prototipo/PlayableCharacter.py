import pygame
from RegularBullet import RegularBullet
from Grenade import Grenade
from abc import abstractmethod


class PlayableCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo, grenade):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.grenade = grenade
        self.start_grenade = grenade
        self.shoot_cooldown = 0
        self.grenade_thrown = False
        self.health = 100
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.in_slug = False
        self.is_human = True
        self.lives = 3

        #player action variables
        self.moving_left = False
        self.moving_right = False
        self.shooting = False
        self.throwing = False

        #load all images for the players
        self.width = None
        self.height = None

    def update(self):
        self.update_animation()
        self.check_alive()
        #update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, game_map):
        #reset movement variables
        dx = 0
        dy = 0

        #assign movement variables if moving left or right
        if self.moving_left:
            dx = - self.speed
            self.flip = True
            self.direction = -1
        if self.moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        #jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        #apply gravity
        self.vel_y += 0.75
        dy += self.vel_y

        for tile in game_map.tile_list:
            #check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            #check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if below the ground, i.e, jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                #check if above the ground, i.e, falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom
                    
        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def shoot(self, bullet_group):
        if self.shoot_cooldown == 0 and self.ammo > 0:
#           self.update_action(1)
            self.shoot_cooldown = 20
            bullet = RegularBullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            #reduce ammo
            self.ammo -= 1

    def throw_grenade(self, grenade_group):
        if self.grenade_thrown is False and self.grenade > 0:
            self.grenade_thrown = True
            grenade = Grenade(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction),
                                self.rect.top, self.direction)
            grenade_group.add(grenade)
            #reduce grenade
            self.grenade -= 1

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.image = None

    @abstractmethod
    def update_animation(self):
        pass
    
    @abstractmethod
    def update_action(self, new_action):
        pass
        

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
