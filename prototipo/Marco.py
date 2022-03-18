import pygame
from createAnimations import animation_list
from PlayableCharacter import PlayableCharacter

revive_1 = pygame.transform.scale(pygame.image.load('assets/reviving_1.png'), (75, 75))
revive_2 = pygame.transform.scale(pygame.image.load('assets/reviving_2.png'), (75, 75))
revive_sprite_list = [revive_1, revive_2, revive_1, revive_2]


class Marco(PlayableCharacter, pygame.sprite.Sprite):
    def __init__(self, x, y, speed, ammo, grenade):
        super().__init__(x, y, speed, ammo, grenade)
        pygame.sprite.Sprite.__init__(self)

        # load all images for the players
        img = pygame.image.load('assets/marco_rossi.png').convert_alpha()
        self.image = pygame.transform.scale(img, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.__width = self.image.get_width()
        self.__height = self.image.get_height()

        # player action variables
        self.__sprite_index = 0
        self.__revive_index = 0
        self.__action = 2
        self.__animation_list = animation_list
        self.__update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.sprite_index]
    
    @property
    def width(self):
        return self.__width
        
    @property
    def height(self):
        return self.__height

    @property
    def sprite_index(self):
        return self.__sprite_index
        
    @sprite_index.setter
    def sprite_index(self, new_sprite_index: int):
        if isinstance(new_sprite_index, int):
            self.__sprite_index = new_sprite_index
    
    @property
    def revive_index(self):
        return self.__revive_index
        
    @revive_index.setter
    def revive_index(self, new_revive_index: int):
        self.__revive_index = new_revive_index
    
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
           
    @property
    def update_time(self):
        return self.__update_time
        
    @update_time.setter
    def update_time(self, new_update_time: int):
        self.__update_time = new_update_time

# End of getters and setters

    def revive(self):
        if self.lives > 0:
            self.image = revive_sprite_list[int(self.revive_index)]
            self.revive_index += 0.1
            if self.revive_index >= len(revive_sprite_list):
                self.revive_index = 0
                self.alive = True
                self.health = 100
                self.speed = 5
                self.lives -= 1
                img = pygame.image.load('assets/marco_rossi.png').convert_alpha()
                self.image = pygame.transform.scale(img, (75, 75))
        else:
            pygame.sprite.Sprite.kill(self)

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
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
