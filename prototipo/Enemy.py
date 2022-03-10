import pygame
import random
from Bullet import Bullet, bullet_group

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo):
            pygame.sprite.Sprite.__init__(self)
            self.alive = True
            self.speed = speed
            self.ammo = ammo
            self.start_ammo = ammo
            self.shoot_cooldown = 0
            self.health = 100
            self.max_health = self.health
            self.direction = 1
            self.vel_y = 0
            self.jump = False
            self.in_air = True
            self.flip = False
            #ai specific variables
            self.move_counter = 0
            self.vision = pygame.Rect(0, 0, 150, 20)
            self.idling = False
            self.idling_counter = 0
            
            img = pygame.image.load('assets/RebelSoldier.png').convert_alpha()
            self.image = pygame.transform.scale(img, (89, 77))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.width = self.image.get_width()
            self.height = self.image.get_height()


    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            img = pygame.image.load('assets/RebelSoldier_dead.png').convert_alpha()
            self.image = pygame.transform.scale(img, (89, 77))


    def update(self):
        self.check_alive()
        #update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def shoot(self, bullet_group):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            #reduce ammo
            self.ammo -= 1


    def move(self, moving_left, moving_right, game_map):
        #reset movement variables
        dx = 0
        dy = 0

        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
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
        if self.vel_y > 10:
            self.vel_y
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

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy


    def ai(self, player, game_map):
        if self.alive and player.alive:
            if self.idling == False and random.randint(1, 200) == 1:
                self.idling = True
                self.idling_counter = 50
            #check if the ai in near the player
            if self.vision.colliderect(player.rect):
                #stop running and face the player
                #shoot
                self.shoot(bullet_group)
            else:
                if self.idling == False:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right, game_map)
                    self.move_counter += 1
                    #update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > 600 // 16:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

