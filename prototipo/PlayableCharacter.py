import pygame
from RegularBullet import RegularBullet
from Grenade import Grenade
from abc import abstractmethod


class PlayableCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo, grenade):
        pygame.sprite.Sprite.__init__(self)
        self.__alive = True
        self.__speed = speed
        self.__ammo = ammo
        self.__start_ammo = ammo
        self.__grenade = grenade
        self.__start_grenade = grenade
        self.__shoot_cooldown = 0
        self.__grenade_thrown = False
        self.__health = 100
        self.__max_health = self.health
        self.__direction = 1
        self.__vel_y = 0
        self.__jump = False
        self.__in_air = True
        self.__flip = False
        self.__in_slug = False
        self.__is_human = True
        self.__lives = 3

        #player action variables
        self.__moving_left = False
        self.__moving_right = False
        self.__shooting = False
        self.__throwing = False


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
    def grenade(self):
        return self.__grenade
        
    @grenade.setter
    def grenade(self, new_grenade: int):
        if isinstance(new_grenade, int):
            self.__grenade = new_grenade
    

    @property
    def start_grenade(self):
        return self.__start_grenade
        
    
    @property
    def shoot_cooldown(self):
        return self.__shoot_cooldown
        
    @shoot_cooldown.setter
    def shoot_cooldown(self, new_shoot_cooldown: int):
        if isinstance(new_shoot_cooldown, int):
            self.__shoot_cooldown = new_shoot_cooldown

    @property
    def grenade_thrown(self):
        return self.__grenade_thrown
        
    @grenade_thrown.setter
    def grenade_thrown(self, new_grenade_thrown: bool):
        if isinstance(new_grenade_thrown, bool):
            self.__grenade_thrown = new_grenade_thrown
            
    @property
    def health(self):
        return self.__health
        
    @health.setter
    def health(self, new_health: int):
        if isinstance(new_health, int):
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
    def in_slug(self):
        return self.__in_slug
        
    @in_slug.setter
    def in_slug(self, new_in_slug: bool):
        if isinstance(new_in_slug, bool):
            self.__in_slug = new_in_slug


    @property
    def is_human(self):
        return self.__is_human
        
    @is_human.setter
    def is_human(self, new_is_human: bool):
        if isinstance(new_is_human, bool):
            self.__is_human = new_is_human


    @property
    def lives(self):
        return self.__lives
        
    @lives.setter
    def lives(self, new_lives: int):
        if isinstance(new_lives, int):
            self.__lives = new_lives


    @property
    def moving_left(self):
        return self.__moving_left
        
    @moving_left.setter
    def moving_left(self, new_moving_left: bool):
        if isinstance(new_moving_left, bool):
            self.__moving_left = new_moving_left


    @property
    def moving_right(self):
        return self.__moving_right
        
    @moving_right.setter
    def moving_right(self, new_moving_right: bool):
        if isinstance(new_moving_right, bool):
            self.__moving_right = new_moving_right
    

    @property
    def shooting(self):
        return self.__shooting
        
    @shooting.setter
    def shooting(self, new_shooting: bool):
        if isinstance(new_shooting, bool):
            self.__shooting = new_shooting
    

    @property
    def throwing(self):
        return self.__throwing
        
    @throwing.setter
    def throwing(self, new_throwing: bool):
        if isinstance(new_throwing, bool):
            self.__throwing = new_throwing

# End of getters and setters  

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
            dx = - self.__speed
            self.flip = True
            self.direction = -1
        if self.moving_right:
            dx = self.__speed
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
            bullet = RegularBullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery - 12, self.direction)
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

    # displays player's health bar
    def health_bar(self, screen):
        pygame.draw.rect(screen, (0,0,0), (8, 8, 154, 29))
        pygame.draw.rect(screen, (255,0,0), (10, 10, 300//2, 25))
        pygame.draw.rect(screen, (0,255,0), (10, 10, (self.health//2)*3, 25))
    
    # displays player's text hud
    def draw_hud(self, screen, text, font, text_col, x, y):
        hud = font.render(text, True, text_col)
        screen.blit(hud, (x, y))
    
    # displays player's ammo
    def draw_bullets(self, screen):
        bullet_img = pygame.image.load('assets/bullet.png').convert_alpha()
        for x in range(self.ammo):
            screen.blit(bullet_img, (110 + (x*10), 60))
    
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
