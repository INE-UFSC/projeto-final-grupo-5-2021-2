import pygame
from PlayableCharacter import PlayableCharacter
from Enemy import Enemy
from map import tile_map
from Bullet import bullet_group
from Grenade import grenade_group, explosion_group

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Metal Slug')

#set FPSd
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
    

player = PlayableCharacter(200, 200, 5, 20, 5)
enemy = Enemy(400, 200, 5, 20)

def health_bar(self):
    self.health_bar = player.health
    pygame.draw.rect(screen, (255,0,0), (10, 10, 300//2, 25))
    pygame.draw.rect(screen, (0,255,0), (10, 10, (self.health//2)*3, 25))

run = True
while run:

    clock.tick(FPS)

    draw_map(tile_map)

    health_bar(player)

    player.update()
    player.draw(screen)

    enemy.update()
    enemy.draw(screen)
    enemy.ai(player)

    

    #update and draw groups
    bullet_group.update(player, bullet_group, enemy)
    bullet_group.draw(screen)
    grenade_group.update(player, grenade_group, enemy)
    grenade_group.draw(screen)
    explosion_group.update(player, explosion_group, enemy)
    explosion_group.draw(screen)

    #update player actions
    if player.alive:
        if player.shooting:
            player.shoot(bullet_group)
        elif player.throwing:
            player.throw_grenade(grenade_group)
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
            if event.key == pygame.K_q:
                player.throwing = True
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
            if event.key == pygame.K_q:
                player.throwing = False
                player.grenade_thrown = False

    pygame.display.update()

pygame.quit()
