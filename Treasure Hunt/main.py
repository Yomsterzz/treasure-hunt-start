import pygame
pygame.init()
import random
import time
import sys

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Hunt")

clock = pygame.time.Clock()
grid_size = 20
cell_size = WIDTH//grid_size
fps = 30
obstacle_num = 10

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (76, 210, 90)
RED = (186, 45, 11)
BLUE = (5, 142, 217)

treasure_pos = []
obstacle_pos = []
player_pos = [grid_size//2, grid_size//2]
score = 0

def draw_grid():t
    for x in range(0,WIDTH, cell_size):
        pygame.draw.line(screen, BLUE, (x,0), (x,HEIGHT), 2)
    
    for y in range(0,HEIGHT, cell_size):
        pygame.draw.line(screen, BLUE, (0,y), (WIDTH,y), 2)
        
def draw_player():
    pygame.draw.rect(screen, BLUE, (player_pos[0]*cell_size, player_pos[1]*cell_size, cell_size, cell_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(WHITE)
    draw_grid()
    draw_player()
    clock.tick(fps)
