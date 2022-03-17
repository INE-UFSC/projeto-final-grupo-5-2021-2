import pygame
from PlayableCharacter import PlayableCharacter
from Enemy import Enemy
from map import Map
#from map_test import tile_map
from Bullet import bullet_group
from Grenade import grenade_group
from CurrentPlayer import CurrentPlayer

screen_height = 600
screen_width = 800

class Mission():
    def __init__(self, level):
        self.level = level

    def iniciar_partida(self):
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
        '''
        def draw_map(current_map):
            screen.fill(BG)
            
            for y in range(len(current_map)):
                for x in range(len(current_map[y])):
                    if current_map[y][x] == 'X':
                        rect = pygame.Rect(x*50, y*50, 50, 50)
                        pygame.draw.rect(screen, BROWN, rect)
        '''   
        game_map = Map(self.level, 'background_1', screen_height, screen_width, 16, 150)
        #player = PlayableCharacter(200, 200, 5, 20, 5)
        #enemy = Enemy(400, 200, 5, 20)
        game_map.load_data()
        player, enemy_group, pickable_items_group = game_map.process_data()
        current_player = CurrentPlayer(player)

        def health_bar(self):
            self.health_bar = player.health
            pygame.draw.rect(screen, (255,0,0), (10, 10, 300//2, 25))
            pygame.draw.rect(screen, (0,255,0), (10, 10, (self.health//2)*3, 25))

        run = True
        while run:

            clock.tick(FPS)

        #   draw_map(tile_map)
            game_map.draw_bg(screen)
        #    game_map.draw(screen)
            health_bar(player)

            player.update()
            player.draw(screen)

            # controls if the current player is the slug or human
            if player.in_slug:
                player = current_player.enter_slug()
                current_player = CurrentPlayer(player)
            if player.is_human is False and player.alive is False:
                player = current_player.exit_slug()
                current_player = CurrentPlayer(player)
                player.update()

            # player.update_animation()

            for enemy in enemy_group:
                enemy.update()
                enemy.draw(screen)
                enemy.ai(player, game_map)

            #update and draw groups
            bullet_group.update(player, bullet_group, enemy_group)
            bullet_group.draw(screen)
            grenade_group.update(game_map, player, enemy_group)
            grenade_group.draw(screen)
            pickable_items_group.draw(screen)
            pickable_items_group.update(player)

            #update player actions
            if player.alive:
                if player.shooting:
                    player.update_action(1)
                    player.shoot(bullet_group)
                elif player.throwing:
                    player.throw_grenade(grenade_group)
                elif player.in_air:
                    player.update_action(0)#2: jump
#              elif player.moving_left or player.moving_right:
#                   player.update_action()#1: run
                else:
                    player.update_action(2)#0: idle
                player.move(game_map)
    
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
