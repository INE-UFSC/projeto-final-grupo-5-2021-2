from Marco import Marco
from Rebel import Rebel
from Tank import Tank
from Badass import Badass
import pygame
import csv
from PickableItem import PickableItem


class Map:
    def __init__(self, level, background, screen_height, screen_width, rows, cols, sprite_list=[], tile_list=[], map_data=[]):
        self.__level = level
        self.__background = pygame.image.load('assets/background_3.jpg')
        self.__bg_rect = self.background.get_rect(topleft=(0, 0))
        self.__tile_list = tile_list
        self.__map_data = map_data
        self.__screen_height = screen_height
        self.__screen_width = screen_width
        self.__rows = rows
        self.__cols = cols
        self.__tile_size = screen_height//rows
        self.__sprite_list = sprite_list
        img = pygame.image.load(f'assets/tiles/0.png').convert_alpha()
        sprite_list.append(img)
    
    @property
    def level(self):
        return self.__level
        
    @level.setter
    def level(self, new_level):
        self.__level = new_level
    
    @property
    def background(self):
        return self.__background
        
    @background.setter
    def background(self, new_background):
        self.__background = new_background
    
    @property
    def bg_rect(self):
        return self.__bg_rect
        
    @bg_rect.setter
    def bg_rect(self, new_bg_rect):
            self.__bg_rect = new_bg_rect
    
    @property
    def tile_list(self):
        return self.__tile_list
        
    @tile_list.setter
    def tile_list(self, new_tile_list: list):
        if isinstance(new_tile_list, list):
            self.__tile_list = new_tile_list
    
    @property
    def map_data(self):
        return self.__map_data
        
    @map_data.setter
    def map_data(self, new_map_data: list):
        if isinstance(new_map_data, list):
            self.__map_data = new_map_data
    
    @property
    def screen_height(self):
        return self.__screen_height
        
    @screen_height.setter
    def screen_height(self, new_screen_height: float):
        self.__screen_height = new_screen_height

    @property
    def screen_width(self):
        return self.__screen_width
        
    @screen_width.setter
    def screen_width(self, new_screen_width: int):
        if isinstance(new_screen_width, int):
            self.__screen_width = new_screen_width
    
    @property
    def rows(self):
        return self.__rows
    
    @rows.setter
    def rows(self, new_rows: int):
        if isinstance(new_rows, int):
            self.__rows = new_rows
    
    @property
    def cols(self):
        return self.__cols
    
    @cols.setter
    def cols(self, new_cols: int):
        if isinstance(new_cols, int):
            self.__cols = new_cols
    
    @property
    def tile_size(self):
        return self.__tile_size
    
    @tile_size.setter
    def tile_size(self, new_tile_size: int):
        if isinstance(new_tile_size, int):
            self.__tile_size = new_tile_size
    
    @property
    def sprite_list(self):
        return self.__sprite_list
        
    @sprite_list.setter
    def sprite_list(self, new_sprite_list: list):
        if isinstance(new_sprite_list, list):
            self.__sprite_list = new_sprite_list

# End of getters and setters  

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
                    enemy = Rebel(x * self.tile_size, y * self.tile_size, 2, 50)
                    enemy_group.add(enemy)
                elif tile == 3:  # create ammo box
                    pickable_item = PickableItem('Ammo', x * self.tile_size, y * self.tile_size, self.tile_size)
                    pickable_items_group.add(pickable_item)
                elif tile == 4:  # create grenade box
                    pickable_item = PickableItem('Grenade', x * self.tile_size, y * self.tile_size, self.tile_size)
                    pickable_items_group.add(pickable_item)
                elif tile == 5: #create slug
                    pickable_item = PickableItem('Slug', x * self.tile_size, y * self.tile_size, self.tile_size)
                    pickable_items_group.add(pickable_item)
                elif tile == 6:  # create tank enemies
                    enemy = Tank(x * self.tile_size, y * self.tile_size, 2, 50)
                    enemy_group.add(enemy)
                elif tile == 7:  # create badass enemies
                    enemyB = Badass(x * self.tile_size, y * self.tile_size, 2, 50)
                    enemy_group.add(enemyB)

        return player, enemy_group, pickable_items_group

    # method for tile scroll
    def update_map(self, speed_x):
        for tile in self.tile_list:
            tile[1][0] += speed_x

    def draw_bg(self, screen):
        screen.blit(self.background, self.bg_rect)

    # method for background scroll
    def bg_update(self, speed_x):
        self.bg_rect.x += speed_x
