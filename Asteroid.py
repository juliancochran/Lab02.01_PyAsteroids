'''
Asteroid class for drawing/animating in PyAsteroids
'''
__author__ = "Add your name here"
__version__ = "Add version date here"

import random
import pygame
from ColorGen import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        width = random.randint(10, 70)
        height = random.randint(10, 70)
        self.image = pygame.Surface([width, height])
        self.image.fill(ColorGen.make_gray())
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(1, screen.get_width() - width), random.randint(1, screen.get_height() - height))
        # screen boundaries for moving the Asteroid around the screen
        self.left_boundary = -width
        self.right_boundary = screen.get_width()
        self.top_boundary = -height
        self.bottom_boundary = screen.get_height()
        # random movement of this sprite is here; prevents the sprite from having movement speed set to 0
        self.x_change = self.y_change = 0
        while self.x_change == 0 or self.y_change == 0:
            self.x_change = random.randint(-2, 2)
            self.y_change = random.randint(-2, 2)
        self.hit_points = 3     # an asteroid must be hit 3 times by bullets before it is deleted
        self.delete_me = False  # when this is set to true, the sprite group deletes this object

    # draw the item to the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    # move the item around the screen, appearing on oppposite edge when needed
    def update(self):
        self.rect.x += self.x_change
        self.rect.y += self.y_change
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

    # when hit by a bullet, this object either shrinks or is marked for deletion
    def shrink(self, screen):
        if self.hit_points > 1:
            new_width = max(10, self.rect.width - 10)
            new_height = max(10, self.rect.height - 10)
            self.image = pygame.Surface([new_width, new_height])
            color = ColorGen.make_gray()
            self.image.fill(color)
            self.rect.size = (new_width, new_height)
            self.hit_points -= 1
        else:
            self.delete_me = True
