import os
import pygame

dir = 'assets/actions'

animation_list = []

def animations(animations_path):
    global animation_list
    files_number = 0
    img_list = []

    for file in os.listdir(animations_path):
        files_number += 1

    for i in range(files_number):
        img = pygame.image.load(f'{animations_path}/{i}.png')
        img = pygame.transform.scale(img, (int(img.get_width() * 75), int(img.get_height() * 75)))
        img_list.append(img)

    animation_list.append(img_list)


for path in os.listdir(dir):
    animations(f'{dir}/{path}')
