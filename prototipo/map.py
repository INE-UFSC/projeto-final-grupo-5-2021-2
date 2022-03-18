from Marco import Marco
from Rebel import Rebel
from Tank import Tank
from Badass import Badass
import pygame
import csv
from PickableItem import PickableItem


class Map:
    def __init__(self, level, background, screen_height, screen_width, rows, cols, sprite_list=[], tile_list=[], map_data=[]):
        self.level = level
        self.background = pygame.image.load('assets/background_1.png')
        self.bg_rect = self.background.get_rect(topleft=(0, 0))
        self.tile_list = tile_list
        self.map_data = map_data
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.rows = rows
        self.cols = cols
        self.tile_size = screen_height//rows
        self.sprite_list = sprite_list
        img = pygame.image.load(f'assets/tiles/0.png').convert_alpha()
        sprite_list.append(img)


    def load_data(self):
        for row in range(self.rows):
            r = [-1] * self.cols
            self.map_data.append(r)

        with open(f'assets/level{self.level}_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.map_data[x][y] = int(tile)


    def process_data(self):
        enemy_group = pygame.sprite.Group()
        pickable_items_group = pygame.sprite.Group()
        player = None
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 0:
                    img = self.sprite_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * self.tile_size
                    img_rect.y = y * self.tile_size
                    tile_data = (img, img_rect)
                    self.tile_list.append(tile_data)
                elif tile == 1:  # create player
                    player = Marco(200, 200, 5, 20, 5)
                elif tile == 2:  # create enemies
                    enemy = Rebel(400, 200, 2, 50)
                    enemy_group.add(enemy)
                elif tile == 3:  # create ammo box
                    pickable_item = PickableItem('Ammo', x * self.tile_size, y * self.tile_size, self.tile_size)
                    pickable_items_group.add(pickable_item)
                elif tile == 4:  # create grenade box
                    pickable_item = PickableItem('Grenade', x * self.tile_size, y * self.tile_size, self.tile_size)
                    pickable_items_group.add(pickable_item)
                elif tile == 5: #create slug
                    pickable_item = PickableItem('Slug', (self.screen_width - self.screen_width / 4), y * self.tile_size, self.tile_size)
                    pickable_items_group.add(pickable_item)
                elif tile == 6:  # create tank enemies
                    enemy = Tank(600, 200, 2, 50)
                    enemy_group.add(enemy)
                elif tile == 7:  # create badass enemies
                    enemyB = Badass(500, 200, 2, 50)
                    enemy_group.add(enemyB)

        return player, enemy_group, pickable_items_group
    
    def update_map(self, speed_x):
        for tile in self.tile_list:
            tile[1].x += speed_x

    def draw_bg(self, screen):
        screen.blit(self.background, self.bg_rect)

    def bg_update(self, speed_x):
        self.bg_rect.x += speed_x
