import pygame

pygame.init()

# Create window and set resolution
screen = pygame.display.set_mode(640, 480)

# A lot of times you don't want to run games at the max frame rate
clock = pygame.time.Clock()