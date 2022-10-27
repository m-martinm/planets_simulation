import pygame
from modules.Constants import *
from pandas import Timestamp

class Engine:

    planet_list = []
    
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.size = width, height
        self.clock = pygame.time.Clock()
        # global variables and start
        pygame.init()
        Engine.time = Timestamp.today(tz="UTC").to_julian_date()
        Engine.screen = pygame.display.set_mode(self.size)
        Engine.center = (self.w/2, self.h /2)

    def render(self):
        Engine.screen.fill(BLACK)
        self.clock.tick(30)
        for planet in Engine.planet_list:
            planet.update()
            planet.display()
        pygame.display.flip()