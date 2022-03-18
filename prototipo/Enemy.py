import pygame
import random
from Bullet import bullet_group
from RegularBullet import RegularBullet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo):
        pygame.sprite.Sprite.__init__(self)
        self.__alive = True
        self.__speed = speed
        self.__ammo = ammo
        self.__start_ammo = ammo
        self.__shoot_cooldown = 0
        self.__health = 100
        self.__max_health = self.health
        self.__direction = 1
        self.__vel_y = 0
        self.__jump = False
        self.__in_air = True
        self.__flip = False

        # ai specific variables
        self.__move_counter = 0
        self.__vision = pygame.Rect(0, 0, 150, 20)
        self.__idling = False
        self.__idling_counter = 0
        self.__animation_index = 0
        self.__death_counter = 0

        self.__width = None
        self.__height = None


    @property
    def alive(self):
        return self.__alive
        
    @alive.setter
    def alive(self, new_alive: bool):
        if isinstance(new_alive, bool):
            self.__alive = new_alive


    @property
    def speed(self):
        return self.__speed
        
    @speed.setter
    def speed(self, new_speed: int):
        if isinstance(new_speed, int):
            self.__speed = new_speed


    @property
    def ammo(self):
        return self.__ammo
        
    @ammo.setter
    def ammo(self, new_ammo: int):
        if isinstance(new_ammo, int):
            self.__ammo = new_ammo


    @property
    def start_ammo(self):
        return self.__start_ammo


    @property
    def shoot_cooldown(self):
        return self.__shoot_cooldown
        
    @shoot_cooldown.setter
    def shoot_cooldown(self, new_shoot_cooldown: int):
        if isinstance(new_shoot_cooldown, int):
            self.__shoot_cooldown = new_shoot_cooldown


    @property
    def health(self):
        return self.__health
        
    @health.setter
    def health(self, new_health: int):
        self.__health = new_health


    @property
    def max_health(self):
        return self.__max_health


    @property
    def direction(self):
        return self.__direction
        
    @direction.setter
    def direction(self, new_direction: int):
        if isinstance(new_direction, int):
            self.__direction = new_direction
    

    @property
    def vel_y(self):
        return self.__vel_y
        
    @vel_y.setter
    def vel_y(self, new_vel_y: float):
        self.__vel_y = new_vel_y


    @property
    def jump(self):
        return self.__jump
        
    @jump.setter
    def jump(self, new_jump: bool):
        if isinstance(new_jump, bool):
            self.__jump = new_jump


    @property
    def in_air(self):
        return self.__in_air
        
    @in_air.setter
    def in_air(self, new_in_air: bool):
        if isinstance(new_in_air, bool):
            self.__in_air = new_in_air


    @property
    def flip(self):
        return self.__flip
        
    @flip.setter
    def flip(self, new_flip: bool):
        if isinstance(new_flip, bool):
            self.__flip = new_flip
    

    @property
    def move_counter(self):
        return self.__move_counter
        
    @move_counter.setter
    def move_counter(self, new_move_counter: int):
        if isinstance(new_move_counter, int):
            self.__move_counter = new_move_counter
    

    @property
    def vision(self):
        return self.__vision
        
    @vision.setter
    def vision(self, new_vision):
        self.__vision = new_vision
        

    @property
    def idling(self):
        return self.__idling
        
    @idling.setter
    def idling(self, new_idling: bool):
        self.__idling = new_idling


    @property
    def idling_counter(self):
        return self.__idling_counter
        
    @idling_counter.setter
    def idling_counter(self, new_idling_counter: int):
        if isinstance(new_idling_counter, int):
            self.__idling_counter = new_idling_counter
    

    @property
    def animation_index(self):
        return self.__animation_index
        
    @animation_index.setter
    def animation_index(self, new_animation_index: int):
        self.__animation_index = new_animation_index
    

    @property
    def death_counter(self):
        return self.__death_counter
        
    @death_counter.setter
    def death_counter(self, new_death_counter: int):
        if isinstance(new_death_counter, int):
            self.__death_counter = new_death_counter
    

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, new_width):
        self.__width = new_width
        

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new_height):
        self.__height = new_height

# End of getters and setters

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def check_alive(self):
        pass

    def update(self):
        self.check_alive()
        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        self.update_dead()

    def shoot(self, bullet_group):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = RegularBullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
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
                if self.idling is False:
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
