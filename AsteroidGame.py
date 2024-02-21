'''
Using Pygame to learn about classes/objects OOD and OOP for PyAsteroids game
'''
__author__ = "Add your name here"
__version__ = "Add version date here"

import sys
import pygame
import time
from Asteroid import *
from Spaceship import *
from Bullet import *

pygame.init()
screen = pygame.display.set_mode((1000,700))
BLACK = (0,0,0)

# TODO: create a method that displays the score to the screen
def show_score(score):
    print('delete this statement, show the score')

# TODO: create a method that displays end of game information
def endgame_display(score):
    print('delete this statement, show the score at the end of the game, display stats')

### LOADING AND CREATING PROGRAM VARIABLES HERE ###
# create asteroids, player, and bullets sprite groups
asteroids = pygame.sprite.Group()
players = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# create the spaceship -- see the constructor for the class
spaceship = Spaceship(screen)
players.add(spaceship)
# create the asteroids -- make this harder by adding more
for i in range(10):
    asteroids.add(Asteroid(screen))
clock = pygame.time.Clock()
# running controls the animation/while loop
running = True
# safety time gives the player 2 seconds to move before asteroid collision becomes active
safety_time = 0

# main game loop
while running:
    # EVENT PROCESSING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # KEYBOARD PROCESSING, this lets the players shoot a bullet at an asteroid
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a new bullet instance and add it to the bullets group; see the constructor
                bullet = Bullet(spaceship)
                bullets.add(bullet)

    # PROCESS KEYS PRESSED FOR MOVEMENT/ROTATION
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

    # DETECT COLLISION between Asteroids and Spaceship, but give the user 2 seconds at the start
    if safety_time == 120:
        for asteroid in asteroids:
            if asteroid.rect.colliderect(spaceship):
                running = False
    else:
        safety_time += 1

    # DRAW TO SCREEN. ANIMATE, FLIP, TIME CLOCK, UPDATE SCREEN
    screen.fill(BLACK)
    asteroids.draw(screen)
    asteroids.update()
    players.draw(screen)
    players.update()
    bullets.draw(screen)
    bullets.update()
    pygame.display.flip()
    clock.tick(60)

# CALL ENDGAME DISPLAY HERE

time.sleep(2)   # pause the game from closing for display
pygame.quit()
sys.exit()
