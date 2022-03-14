import os
import pygame

animation_list = []

class Animations():
    def __init__(self, path):
        self.path = path
        self.files_number = 0
        self.img_list = []


    def count_files(self):
        for file in self.path:
            self.files_number += 1


    def create_sprites(self):
        for i in range(self.files_number):
            img = pygame.image.load(f'{self.path}/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * 2), int(img.get_height() * 2)))
            self.img_list.append(img)
