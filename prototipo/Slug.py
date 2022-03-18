import pygame
from Grenade import Grenade
from SlugBullet import SlugBullet
from PlayableCharacter import PlayableCharacter
from createAnimations import slug_animation_list

# slug sprite
slug_img = pygame.image.load('assets/actions/slug_standing/0.png')


class Slug(PlayableCharacter, pygame.sprite.Sprite):
    def __init__(self, x, y, player_health, player_ammo, player_grenade, player_speed, lives):
        super().__init__(x, y, 5, 200, 5)
        self.image = pygame.transform.scale(slug_img, (100, 75))
        self.rect = self.image.get_rect(center=(x, y))
        self.__width = self.image.get_width()
        self.__height = self.image.get_height()

        # player stats before entering the slug
        self.__player_health = player_health
        self.__player_ammo = player_ammo
        self.__player_grenade = player_grenade
        self.__player_speed = player_speed
        self.__lives = lives

        # slug stats
        self.__alive = True
        self.__health = 100
        self.__in_slug = False
        self.__is_human = False

        # slug action variables
        self.__sprite_index = 0
        self.__action = 2
        self.__animation_list = slug_animation_list
        self.__update_time = pygame.time.get_ticks()
        self.image = pygame.transform.scale(self.animation_list[self.action][self.sprite_index], (100, 75))

    @property
    def width(self):
        return self.__width
        
    @property
    def height(self):
        return self.__height
   
    @property
    def player_health(self):
        return self.__player_health
    
    @player_health.setter
    def player_health(self, new_player_health: int):
        if isinstance(new_player_health, int):
            self.__player_health = new_player_health  

    @property
    def player_ammo(self):
        return self.__player_ammo
        
    @player_ammo.setter
    def player_ammo(self, new_player_ammo: int):
        if isinstance(new_player_ammo, int):
            self.__player_ammo = new_player_ammo
    
    @property
    def player_grenade(self):
        return self.__player_grenade
    
    @player_grenade.setter
    def player_grenade(self, new_player_grenade: int):
        if isinstance(new_player_grenade, int):
            self.__player_grenade = new_player_grenade 

    @property
    def player_speed(self):
        return self.__player_speed
    
    @player_speed.setter
    def player_speed(self, new_player_speed: float):
        self.__player_speed = new_player_speed
    
    @property
    def lives(self):
        return self.__lives
    
    @lives.setter
    def lives(self, new_lives: int):
        if isinstance(new_lives, int):
            self.__lives = new_lives
    
    @property
    def alive(self):
        return self.__alive
        
    @alive.setter
    def alive(self, new_alive: bool):
        if isinstance(new_alive, bool):
            self.__alive = new_alive
     
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
    def sprite_index(self):
        return self.__sprite_index
        
    @sprite_index.setter
    def sprite_index(self, new_sprite_index: int):
        if isinstance(new_sprite_index, int):
            self.__sprite_index = new_sprite_index
    
    @property
    def action(self):
        return self.__action
        
    @action.setter
    def action(self, new_action: int):
        if isinstance(new_action, int):
            self.__action = new_action
    
    @property
    def animation_list(self):
        return self.__animation_list
        
    @animation_list.setter
    def animation_list(self, new_animation_list: int):
        if isinstance(new_animation_list, int):
            self.__animation_list = new_animation_list
    
    @property
    def update_time(self):
        return self.__update_time
        
    @update_time.setter
    def update_time(self, new_update_time: int):
        if isinstance(new_update_time, int):
            self.__update_time = new_update_time

# End of getters and setters

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
            bullet = SlugBullet(self.rect.centerx + (0.8 * self.rect.size[0] * self.direction), (self.rect.centery - 11), self.direction)
            bullet_group.add(bullet)
            # reduce ammo
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
