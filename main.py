import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  asteroid_field = AsteroidField()

  Player.containers = (updatable, drawable)
  Shot.containers = (shots, updatable, drawable)

  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

  dt = 0


  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
      
      updatable.update(dt)
      for object in asteroids:
        if object.collision(player):
          print('Game Over!')
          sys.exit()

      for asteroid in asteroids:
        for bullet in shots:
          has_collided = asteroid.collision(bullet)
          if has_collided:
            bullet.kill()
            asteroid.split()
  
      screen.fill('black')
      for object in drawable:
        object.draw(screen)
      pygame.display.flip()
      
      dt = clock.tick(60) / 1000

          

if __name__ == "__main__":
  main()