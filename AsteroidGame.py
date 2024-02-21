'''
Using Pygame to learn about classes/objects
OOD and OOP
'''
__author__ = "Julian C"
__version__ = "02.13.2024"

import pygame
from Asteroid import *
from Spaceship import *
from Bullet import *

pygame.init()
screen = pygame.display.set_mode((1000,700))
BLACK = (0,0,0)

# create asteroids sprite group
asteroids = pygame.sprite.Group()
players = pygame.sprite.Group()
bullets = pygame.sprite.Group()

spaceship = Spaceship(screen)
players.add(spaceship)
for i in range(10):
    asteroids.add(Asteroid(screen))
clock = pygame.time.Clock()
running = True
safety_time = 0

while running:
    # EVENT PROCESSING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # KEYBOARD PROCESSING
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a new bullet instance and add it to the bullets group
                bullet = Bullet(spaceship)
                bullets.add(bullet)
    keys = pygame.key.get_pressed()  # Checking pressed keys
    if keys[pygame.K_LEFT]:
        spaceship.rotate(1)
    if keys[pygame.K_RIGHT]:
        spaceship.rotate(-1)
    if keys[pygame.K_UP]:
        spaceship.move(1)
    # DETECT COLLISION between bullets and Asteroids
    # Check for collisions between bullets and asteroids
    for bullet in bullets:
        for asteroid in asteroids:
            if bullet.rect.colliderect(asteroid.rect):
                # Perform actions when collision is detected (e.g., remove bullet, shrink asteroid)
                bullet.kill()
                asteroid.shrink(screen)
                if asteroid.delete_me:
                    asteroids.remove(asteroid)
    # DETECT COLLISION but give the user 2 seconds at the start
    if safety_time == 120:
        for asteroid in asteroids:
            if asteroid.rect.colliderect(spaceship):
                running = False
    else:
        safety_time += 1
    # DRAW TO SCREEN
    screen.fill(BLACK)
    asteroids.draw(screen)
    asteroids.update()
    players.draw(screen)
    players.update()
    bullets.draw(screen)
    bullets.update()
    pygame.display.flip()
    clock.tick(60)

print('game over')
