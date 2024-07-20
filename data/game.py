import pygame
import sys

pygame.init()

# Create window and set resolution
screen = pygame.display.set_mode((640, 480))

# A lot of times you don't want to run games at the max frame rate
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  pygame.display.update()
  # Force loop to run at 60 fps
  clock.tick(60)