from tokenize import Triple
import pygame
from map import tile_map
import random
import os

class Enemy:
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades):
            pygame.sprite.Sprite.__init__(self)
            self.alive = True
            self.char_type = char_type
            self.speed = speed
            self.ammo = ammo
            self.start_ammo = ammo
            self.shoot_cooldown = 0
            self.grenades = grenades
            self.health = 100
            self.max_health = self.health
            self.direction = 1
            self.vel_y = 0
            self.jump = False
            self.in_air = True
            self.flip = False
            self.animation_list = []
            self.frame_index = 0
            self.action = 0
            self.update_time = pygame.time.get_ticks()
            #ai specific variables
            self.move_counter = 0
            self.vision = pygame.Rect(0, 0, 150, 20)
            self.idling = False
            self.idling_counter = 0
            
            img = pygame.image.load('assets/RebelSoldier.png').convert_alpha()
            self.image = pygame.transform.scale(img, (89, 77))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)


    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
    

    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
        #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)


    def update(self):
        self.check_alive()
        #update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
 

    def move(self, moving_left, moving_right):
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

        #check collision with floor
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy
