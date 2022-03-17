import pygame
import random
from Bullet import Bullet, bullet_group

exp_fr_1 = pygame.image.load('assets/tank_exp/exp_fr1.png')
exp_fr_2 = pygame.image.load('assets/tank_exp/exp_fr2.png')
exp_fr_3 = pygame.image.load('assets/tank_exp/exp_fr3.png')
exp_fr_4 = pygame.image.load('assets/tank_exp/exp_fr4.png')
exp_fr_5 = pygame.image.load('assets/tank_exp/exp_fr5.png')
exp_fr_6 = pygame.image.load('assets/tank_exp/exp_fr6.png')
exp_fr_7 = pygame.image.load('assets/tank_exp/exp_fr7.png')

explosion_animation = [exp_fr_1, exp_fr_2, exp_fr_3, exp_fr_4, exp_fr_5, exp_fr_6, exp_fr_7]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo, type):
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
        self.type = type
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.idling = False
        self.idling_counter = 0
        self.animation_index = 0
        self.death_counter = 0

        if self.type == 'rebel':
            img = pygame.image.load('assets/RebelSoldier.png').convert_alpha()
            self.image = pygame.transform.scale(img, (89, 77))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.width = self.image.get_width()
            self.height = self.image.get_height()

        elif self.type == 'badass':
            img = pygame.image.load('assets/EnemyBadAss.png').convert_alpha()
            self.image = pygame.transform.scale(img, (89, 77))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.width = self.image.get_width()
            self.height = self.image.get_height()

        elif self.type == 'tank':
            self.vision = pygame.Rect(0, 0, 300, 20)
            img = pygame.image.load('assets/enemy_tank.png').convert_alpha()
            self.image = pygame.transform.scale(img, (75, 100))
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
            if self.type == "rebel":
                img = pygame.image.load('assets/RebelSoldier_dead.png').convert_alpha()
                self.image = pygame.transform.scale(img, (89, 77))
            elif self.type == "badass":
                img = pygame.image.load('assets/EnemyBadAss_dead.png').convert_alpha()
                self.image = pygame.transform.scale(img, (89, 77))
            elif self.type == "tank":
                self.image = explosion_animation[int(self.animation_index)]
                self.rect = self.image.get_rect(midbottom=(self.rect.midbottom))
                self.animation_index += 0.2
                if self.animation_index >= len(explosion_animation):
                    self.animation_index = 0
                    self.kill()

    def update(self):
        self.check_alive()
        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        self.update_dead()

    def shoot(self, bullet_group):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            if self.type == 'rebel':
                bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction, 'human')
                bullet.enemy = True
                bullet_group.add(bullet)
            elif self.type == 'tank':
                bullet = Bullet(self.rect.centerx + (0.9 * self.rect.size[0] * self.direction), self.rect.centery - 20, self.direction, 'slug')
                bullet.enemy = True
                bullet_group.add(bullet)
            elif self.type == 'badass':
                bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction, 'human')
                bullet.enemy = True
                bullet_group.add(bullet)
            # reduce ammo
            self.ammo -= 1

    def move(self, moving_left, moving_right, game_map):
        # reset movement variables
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # apply gravity
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
                #  if above the ground, i.e, falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom
        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def ai(self, player, game_map):
        if self.alive and player.alive:
            if self.idling == False and random.randint(1, 200) == 1:
                self.idling = True
                self.idling_counter = 50
            # check if the ai in near the player
            if self.vision.colliderect(player.rect):
                # stop running and face the player
                # shoot
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
                    # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > 600 // 16:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

    def update_dead(self):
        if self.alive is False:
            self.death_counter += 1
        if self.death_counter >= 45:
            self.kill()

