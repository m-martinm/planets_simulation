from datetime import tzinfo
import pygame
from modules.Constants import *
from pandas import *


class Engine:

    planet_list = []
    pygame.init()

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.size = width, height
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('freeserif', 22)

        # global variables and start
        Engine.fps = 30
        Engine.time = Timestamp.today(tz="UTC").to_julian_date()
        Engine.screen = pygame.display.set_mode(self.size)
        Engine.center = (self.w/2, self.h / 2)

    def render(self):
        date = self.font.render(
            f"Date: {to_datetime(Engine.time, origin= 'julian', unit='D').date()}", False, WHITE)
        dateRect = date.get_rect()
        dateRect.topleft = (30, 30)
        Engine.screen.fill(BLACK)
        Engine.screen.blit(date, dateRect)
        self.clock.tick(Engine.fps)
        for planet in Engine.planet_list:
            planet.update()
            planet.display()
        pygame.display.flip()
