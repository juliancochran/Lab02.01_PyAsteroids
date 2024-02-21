'''
Asteroid class for drawing in Pygame
'''
__author__ = "Julian C"
__version__ = "2.13.2024"

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
        self.rect.center = (
        random.randint(1, screen.get_width() - width), random.randint(1, screen.get_height() - height))
        # screen boundaries
        self.left_boundary = -width
        self.right_boundary = screen.get_width()
        self.top_boundary = -height
        self.bottom_boundary = screen.get_height()
        # random movement of this sprite is here
        self.x_change = self.y_change = 0
        while self.x_change == 0 or self.y_change == 0:
            self.x_change = random.randint(-2, 2)
            self.y_change = random.randint(-2, 2)
        self.hit_points = 3
        self.delete_me = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

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
