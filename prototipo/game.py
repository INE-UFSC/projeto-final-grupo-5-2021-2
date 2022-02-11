import pygame
import os
from pygame.constants import K_ESCAPE
from PlayableCharacter import PlayableCharacter
from Enemy import Enemy
from map import tile_map
from Bullet import bullet_group

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Metal Slug')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#game variables
gravity = 0.75

#define colors
BG = (144, 201, 120)
RED = (255, 0, 0)
BROWN = (110, 38, 14)

def draw_map(current_map):
    screen.fill(BG)
    
    for y in range(len(current_map)):
        for x in range(len(current_map[y])):
            if current_map[y][x] == 'X':
                rect = pygame.Rect(x*50, y*50, 50, 50)
                pygame.draw.rect(screen, BROWN, rect)
    

player = PlayableCharacter('player', 200, 200, 3, 5, 20)
enemy = Enemy('enemy', 400, 200, 3, 5, 20, 20)

run = True
while run:

    clock.tick(FPS)

    draw_map(tile_map)

    player.update()
    player.draw(screen)

    enemy.update()
    enemy.draw(screen)
    enemy.ai(player)

    #update and draw groups
    bullet_group.update(player, bullet_group, enemy)
    bullet_group.draw(screen)

    #update player actions
    if player.alive:
        if player.shooting:
            player.shoot(bullet_group)
        if player.in_air:
            player.update_action(2)#2: jump
        elif player.moving_left or player.moving_right:
            player.update_action(1)#1: run
        else:
            player.update_action(0)#0: idle
        player.move()

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.moving_left = True
            if event.key == pygame.K_d:
                player.moving_right = True
            if event.key == pygame.K_SPACE:
                player.shooting = True
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_w and player.alive:
                player.jump = True

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.moving_left = False
            if event.key == pygame.K_d:
                player.moving_right = False
            if event.key == pygame.K_SPACE:
                player.shooting = False

    pygame.display.update()

pygame.quit()
