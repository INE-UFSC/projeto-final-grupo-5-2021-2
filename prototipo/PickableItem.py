import pygame
from Slug import Slug


class PickableItem(pygame.sprite.Sprite):
    def __init__(self, type, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.__tile_size = tile_size
        self.__type = type
        self.image = pygame.image.load(f'assets/pickableitems/{type}.gif').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + tile_size//2, y + (tile_size - self.image.get_height()))
    
    @property
    def tile_size(self):
        return self.__tile_size
    
    @tile_size.setter
    def tile_size(self, new_tile_size: int):
        if isinstance(new_tile_size, int):
            self.__tile_size = new_tile_size
    
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, new_type):
        self.__type = new_type

# End of getters and setters

    def update(self, player, screen_scroll):
        #scroll
        self.rect.x += screen_scroll
        if pygame.sprite.collide_rect(self, player):
            if self.type == 'Ammo':
                player.ammo += 15
            elif self.type == 'Grenade':
                player.grenade += 10
            elif self.type == 'Slug':
                player.in_slug = True
            self.kill()
