import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  clock = pygame.time.Clock()
  dt = 0

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  AsteroidField()

  Player.containers = (updatable, drawable)
  
  Shot.containers = (shots, drawable, updatable)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    
    for structure in updatable:
      structure.update(dt)

    for asteroid in asteroids:
      for shot in shots:
        if asteroid.collides_with(shot):
          asteroid.split()
          shot.kill()

      if asteroid.collides_with(player):
        print("Game over!")
        sys.exit()

    screen.fill((0,0,0))

    for drawing in drawable:
      drawing.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()