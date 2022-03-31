import time
import pygame
from pygame.locals import *

game_title = "Pacman Multiplayer"
flag_game_running = True
fps_limit = 120

player_pos_x, player_pos_y = 50, 50
player_velocity_x, player_velocity_y = 0,0
player_max_velocity = 50

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption(game_title)

pygame.init()
clock = pygame.time.Clock()

window.fill((0, 0, 0))
circle = pygame.draw.circle(window, (255,255,0), (player_pos_x, player_pos_y), 50)

pygame.display.update()

while flag_game_running:
    print((player_pos_x, player_pos_y), (player_velocity_x, player_velocity_y))
    clock.tick(fps_limit)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_A and player_velocity_x >= 0:
                player_velocity_x = -player_max_velocity
                player_velocity_y = 0
            if event.key == pygame.K_RIGHT and player_velocity_x <= 0:
                player_velocity_x = player_max_velocity
                player_velocity_y = 0
            if event.key == pygame.K_UP and player_velocity_y >= 0:
                player_velocity_y = -player_max_velocity
                player_velocity_x = 0
            if event.key == pygame.K_DOWN and player_velocity_y <= 0:
                player_velocity_y = player_max_velocity
                player_velocity_x = 0

    player_pos_x = player_velocity_x/fps_limit + player_pos_x
    player_pos_y = player_velocity_y/fps_limit + player_pos_y

    window.fill((0, 0, 0))
    circle = pygame.draw.circle(window, (255,255,0), (player_pos_x, player_pos_y), 50)

    pygame.display.flip()
    
## Quit the pygame window after 5 seconds
pygame.quit()