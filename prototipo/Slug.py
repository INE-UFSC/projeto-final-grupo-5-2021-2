import pygame
from Grenade import Grenade
from Bullet import Bullet
from PlayableCharacter import PlayableCharacter
from createAnimations import slug_animation_list

# slug sprite
slug_img = pygame.image.load('assets/actions/slug_standing/0.png')


class Slug(PlayableCharacter, pygame.sprite.Sprite):
    def __init__(self, x, y, player_health, player_ammo, player_grenade, player_speed, lives):
        super().__init__(x, y, 5, 200, 5)
        self.image = pygame.transform.scale(slug_img, (100, 75))
        self.rect = self.image.get_rect(center=(x, y))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # player stats before entering the slug
        self.player_health = player_health
        self.player_ammo = player_ammo
        self.player_grenade = player_grenade
        self.player_speed = player_speed
        self.lives = lives

        # slug stats
        self.alive = True
        self.health = 100
        self.in_slug = False
        self.is_human = False

        # slug action variables
        self.sprite_index = 0
        self.action = 2
        self.animation_list = slug_animation_list
        self.update_time = pygame.time.get_ticks()
        self.image = pygame.transform.scale(self.animation_list[self.action][self.sprite_index], (100, 75))


    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            img = pygame.image.load('assets/explosion1.png').convert_alpha()
            self.image = pygame.transform.scale(img, (100, 150))

    def shoot(self, bullet_group):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 15
            bullet = Bullet(self.rect.centerx + (0.8 * self.rect.size[0] * self.direction), (self.rect.centery - 11), self.direction, 'slug')
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

    def update_animation(self):
        # update animation
        animation_cooldown = 100

        # update image depending on current frame
        self.image = pygame.transform.scale(self.animation_list[self.action][self.sprite_index], (100, 75))

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
