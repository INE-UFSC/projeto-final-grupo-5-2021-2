import pygame

class PickableItem(pygame.sprite.Sprite):
    def __init__(self, type, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size = tile_size
        self.type = type
        self.image = pygame.image.load(f'assets/pickableitems/{type}.gif').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + tile_size//2, y + (tile_size - self.image.get_height()))

    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            if self.type == 'Ammo':
                player.ammo += 15
            elif self.type == 'Grenade':
                player.grenades += 10
            self.kill()