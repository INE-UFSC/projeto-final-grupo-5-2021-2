import pygame

#load images
#grenade
grenade_img = pygame.image.load('assets/grenade.png')
#explosion
explosion_fr_1 = pygame.image.load('assets/explosion/exp1.png')
explosion_fr_2 = pygame.image.load('assets/explosion/exp2.png')
explosion_fr_3 = pygame.image.load('assets/explosion/exp3.png')
explosion_fr_4 = pygame.image.load('assets/explosion/exp4.png')
explosion_fr_5 = pygame.image.load('assets/explosion/exp5.png')
explosion_animation = [explosion_fr_1, explosion_fr_2, explosion_fr_3, explosion_fr_4, explosion_fr_5]
#create sprite groups

grenade_group = pygame.sprite.Group()


class Grenade(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.__speed_y = -10
        self.__speed_x = 7
        self.image = grenade_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.__direction = direction
        self.__width = self.image.get_width()
        self.__height = self.image.get_height()
        self.__dx = 0
        self.__dy = 0
        self.__dmg_player = False
        self.__in_air = True
        self.__animation_index = 0

    # getters and setters
    @property
    def speed_y(self):
        return self.__speed_y

    @speed_y.setter
    def speed_y(self, new_speed_y):
        self.__speed_y = new_speed_y

    @property
    def speed_x(self):
        return self.__speed_x

    @speed_x.setter
    def speed_x(self, new_speed_x):
        self.__speed_x = new_speed_x

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, new_direction):
        self.__direction = new_direction

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

    @property
    def dx(self):
        return self.__dx

    @dx.setter
    def dx(self, new_dx):
        self.__dx = new_dx

    @property
    def dy(self):
        return self.__dy

    @dy.setter
    def dy(self, new_dy):
        self.__dy = new_dy

    @property
    def dmg_player(self):
        return self.__dmg_player

    @dmg_player.setter
    def dmg_player(self, new_dmg_player):
        self.__dmg_player = new_dmg_player

    @property
    def in_air(self):
        return self.__in_air

    @in_air.setter
    def in_air(self, new_in_air):
        self.__in_air = new_in_air

    @property
    def animation_index(self):
        return self.__animation_index

    @animation_index.setter
    def animation_index(self, new_animation_index):
        self.__animation_index = new_animation_index

    # end of getters and setters

    def update(self, game_map, player, enemy_group, volume):
        #move grenade
        if self.in_air:
            gravity = 0.75
            self.speed_y += gravity
            self.dy = self.speed_y  # vertical change
            self.dx = (self.direction * self.speed_x)  # horizontal change

        # check collision with map
        for tile in game_map.tile_list:
            if self.rect.colliderect(tile[1]):
                self.dx = 0
                self.dy = 0
                self.in_air = False
                self.explode(player, enemy_group, volume)

        # update grenade position

        self.rect.x += self.dx
        self.rect.y += self.dy

        # check if grenade has gone off screen
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()

    def explode(self, player, enemy_group, volume):

        self.image = explosion_animation[int(self.animation_index)]
        self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

        if self.animation_index == 0:
            explosion = pygame.mixer.Sound('assets/sounds/explosion.mp3')
            explosion.set_volume(volume)
            explosion.play()

        if self.rect.colliderect(player.rect) and self.dmg_player is False:
            player.health -= 50
            self.dmg_player = True

        for enemy in enemy_group:
            if self.rect.colliderect(enemy.rect):
                enemy.health -= 0.5

        self.animation_index += 0.04

        if self.animation_index >= len(explosion_animation):
            self.animation_index = 0
            self.kill()
