import pygame
import sys

class Game:
  def __init__(self):
    pygame.init()

    # Sets name of display window
    pygame.display.set_caption("Fair Fight 1")

    # Create window and set resolution
    self.screen = pygame.display.set_mode((640, 480))

    # A lot of times you don't want to run games at the max frame rate
    self.clock = pygame.time.Clock()

    self.img = pygame.image.load('data/images/clouds/cloud_1.png')

    # Replaces designated color with transparency
    self.img.set_colorkey((0,0,0))

    self.img_pos = [160, 260]
    self.movement = [False, False]

    # First two - top left parameter
    # Right two - width and height
    self.collision_area = pygame.Rect(50, 50, 500, 50)

  def run(self):
    while True:
      self.screen.fill((14,219,248))
      

      img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
      if img_r.colliderect(self.collision_area):
        pygame.draw.rect(self.screen, (0, 255, 100), self.collision_area)
      else:
        pygame.draw.rect(self.screen, (0, 255, 50), self.collision_area)

      # Moves the cloud up and down
      self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
      self.screen.blit(self.img, self.img_pos)


      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            self.movement[0] = True
          if event.key == pygame.K_DOWN:
            self.movement[1] = True

        if event.type == pygame.KEYUP:
          if event.key == pygame.K_UP:
            self.movement[0] = False
          if event.key == pygame.K_DOWN:
            self.movement[1] = False
          

      pygame.display.update()
      # Force loop to run at 60 fps
      self.clock.tick(60)


Game().run()