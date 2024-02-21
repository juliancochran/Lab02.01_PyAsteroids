'''
Bullet class for drawing/animating in PyAsteroids
'''
__author__ = "Add your name here"
__version__ = "Add version date here"

import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, spaceship):
        super().__init__()
        self.image = pygame.Surface((5, 5))  # You can adjust the size of the bullet
        self.image.fill((255, 255, 0))  # yellow color for the bullet
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center  # Start at the center of the spaceship
        self.angle = spaceship.angle
        self.speed = 8  # Adjust the speed of the bullet as needed

     # update method for the sprite
    def update(self):
        # Update position based on speed and angle
        angle_radians = math.radians(self.angle)
        self.rect.x += self.speed * math.cos(angle_radians)
        self.rect.y -= self.speed * math.sin(angle_radians)  # Subtract because y-axis is inverted in Pygame

        # Check if the bullet is out of the screen, and remove it if so
        # Instead of using the boundary variables, this just checks at any level of leaving
        # the screen and deletes the sprite if it's off the screen
        if (
            self.rect.x < 0
            or self.rect.y < 0
            or self.rect.x > pygame.display.get_surface().get_width()
            or self.rect.y > pygame.display.get_surface().get_height()
        ):
            self.kill()
