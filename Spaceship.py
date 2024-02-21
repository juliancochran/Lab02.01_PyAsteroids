'''
Spaceship class for drawing/animating in PyAsteroids
'''
__author__ = "Add your name here"
__version__ = "Add version date here"

import pygame
import math

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.original_image = pygame.image.load("spaceship.png").convert()
        self.original_image.set_colorkey((0, 0, 0))  # Set black as the transparent color
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        # screen boundaries
        self.left_boundary = -self.rect.width
        self.right_boundary = screen.get_width()
        self.top_boundary = -self.rect.height
        self.bottom_boundary = screen.get_height()
        # movement of the spaceship
        self.angle = 0
        self.speed = 0
        self.acceleration = 0
        self.max_speed = 5      # This can be adjusted to make the ship move faster or slower
        self.friction = 0.02    # Adjust this value for desired friction effect

    # Draw the spaceship object to the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # update the UI of the spaceship based on its position and angle of rotation
    def update(self):
        # move to the other side of the screen -- x-axis
        if self.rect.x < self.left_boundary:
            self.rect.x = self.right_boundary - 1
        elif self.rect.x > self.right_boundary:
            self.rect.x = self.left_boundary + 1
        # move to the other side of the screen -- y-axis
        if self.rect.y < self.top_boundary:
            self.rect.y = self.bottom_boundary - 1
        elif self.rect.y > self.bottom_boundary:
            self.rect.y = self.top_boundary + 1

        # Apply friction or drag force
        self.speed *= (1 - self.friction)
        # Update position based on speed and angle; computers work in radians, not degrees
        angle_radians = math.radians(self.angle)
        self.rect.x += self.speed * math.cos(angle_radians)
        self.rect.y -= self.speed * math.sin(angle_radians)  # Subtract because y-axis is inverted in Pygame

    # Rotate the spaceship image and image rect. To do this, the system must remember the former
    # position of the rect/image before it can reset the angle of the rect/image
    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    # Move/accelerate the spaceship, which can be capped
    def move(self, acceleration):
        self.acceleration = acceleration
        # Apply acceleration to speed
        self.speed += self.acceleration
        # Cap the speed to prevent excessive acceleration
        self.speed = min(max(self.speed, 0), self.max_speed)  # Adjust the maximum speed as needed
