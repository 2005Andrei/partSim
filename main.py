import pygame
import random
import math


pygame.init()

W, H = 1000, 500
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

Running = True
while Running:
    screen.fill((0,0,0))
        
    pygame.display.flip()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()