'''
This is a utility class for creating different hues of gray or random colors for an arcade game
'''
__author__ = "Julian Cochran"
__version__ = "02.20.2024"

import random

class ColorGen:
    @staticmethod
    def make_gray():
        grays = [105, 119, 126, 128, 129, 136, 140, 144, 151, 153, 169, 170, 174, 179]
        hue = random.choice(grays)
        color = (hue, hue, hue)
        return color

    @staticmethod
    def make_rgb():
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        return color