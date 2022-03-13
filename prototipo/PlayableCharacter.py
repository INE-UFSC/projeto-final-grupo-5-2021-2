import pygame
from Bullet import Bullet
from Grenade import Grenade
from Animations import animation_list

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

        #player action variables
        self.moving_left = False
        self.moving_right = False
        self.shooting = False
        self.throwing = False
        self.sprite_index = 0
        self.action = 2
        self.animation_list = animation_list
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.sprite_index]

        #load all images for the players
        img = pygame.image.load('assets/marco_rossi.png').convert_alpha()
        self.image = pygame.transform.scale(img, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

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
            dx =- self.speed
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
#            self.update_action(0)

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

    def shoot(self, bullet_group):
        if self.shoot_cooldown == 0 and self.ammo > 0:
#            self.update_action(1)
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction, 'human')
            bullet_group.add(bullet)
            #reduce ammo
            self.ammo -= 1

    def throw_grenade(self, grenade_group):
        if self.grenade_thrown is False and self.grenade > 0:
            self.grenade_thrown = True
            grenade = Grenade(  self.rect.centerx + (0.6 * self.rect.size[0] * self.direction),
                                self.rect.top, self.direction)
            grenade_group.add(grenade)
            #reduce grenade
            self.grenade -= 1

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            img = pygame.image.load('assets/marco_rossi_dead.png').convert_alpha()
            self.image = pygame.transform.scale(img, (75, 75))

    
    def update_animation(self):
        # update animation
        animation_cooldown = 100

        # upadete image depending on current frame
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
        

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
