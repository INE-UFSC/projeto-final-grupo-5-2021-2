from turtle import speed
import pygame
import time
from createAnimations import animation_list
from PlayableCharacter import PlayableCharacter


class Marco(PlayableCharacter, pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo, grenade):
        super().__init__(x, y, speed, ammo, grenade)
        pygame.sprite.Sprite.__init__(self)

        # load all images for the players
        img = pygame.image.load('assets/marco_rossi.png').convert_alpha()
        self.image = pygame.transform.scale(img, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        #player action variables
        self.sprite_index = 0
        self.action = 2
        self.animation_list = animation_list
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.sprite_index]

    def revive(self):
        if self.lives > 0:
            self.alive = True
            self.health = 100
            self.speed = 5
            img = pygame.image.load('assets/marco_rossi.png').convert_alpha()
            self.image = pygame.transform.scale(img, (75, 75))
        else:
            pygame.sprite.Sprite.kill(self)


    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.lives -= 1
            img = pygame.image.load('assets/marco_rossi_dead.png').convert_alpha()
            self.image = pygame.transform.scale(img, (75, 75))
            self.revive()
        else:
            pass


    def update_animation(self):
        # update animation
        animation_cooldown = 100

        # update image depending on current frame
        self.image = self.animation_list[self.action][self.sprite_index]

        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.sprite_index += 1

        # if the animation has run out then reset back to start
        if self.sprite_index >= len(self.animation_list[self.action]):
            self.sprite_index = 0


    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action

            # update the animation settings
            self.sprite_index = 0
            self.update_time = pygame.time.get_ticks()
