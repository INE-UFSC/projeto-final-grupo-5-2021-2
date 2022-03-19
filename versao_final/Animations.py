import os
import pygame

animation_list = []


class Animations():
    def __init__(self, path):
        self.__path = path
        self.__files_number = 0
        self.__img_list = []
    
    @property
    def path(self):
        return self.__path
    
    @path.setter
    def path(self, new_path):
        self.__path = new_path
    
    @property
    def files_number(self):
        return self.__files_number
    
    @files_number.setter
    def files_number(self, new_files_number: int):
        if isinstance(new_files_number, int):
            self.__files_number = new_files_number
    
    @property
    def img_list(self):
        return self.__img_list
    
    @img_list.setter
    def img_list(self, new_img_list: list):
        if isinstance(new_img_list, list):
            self.__img_list = new_img_list

# End of getters and setters

    def count_files(self):
        for file in os.listdir(self.path):
            self.files_number += 1


    def create_sprites(self):
        for i in range(self.files_number):
            img = pygame.image.load(f'{self.path}/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * 2), int(img.get_height() * 2)))
            self.img_list.append(img)
