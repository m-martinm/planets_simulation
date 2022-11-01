from operator import attrgetter
import pygame
from modules.Constants import *
from pandas import Timestamp, to_datetime
from numpy import interp


class Engine:

    planet_list = []

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.size = width, height
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('freeserif', 22)

        Engine.fps = 30
        # current time in Julian Dates
        Engine.time = Timestamp.today(tz="UTC").to_julian_date()
        Engine.dt = None
        Engine.screen = pygame.display.set_mode(self.size)
        Engine.center = (self.w/2, self.h / 2)
        Engine.speed = 30  # in [days/sec]

    def render(self):
        self.clock.tick(Engine.fps)
        # converting the Julian Date back to human readable format
        date = self.font.render(
            f"Date: {to_datetime(Engine.time, origin= 'julian', unit='D').date()}", True, WHITE)
        fps = self.font.render(str(int(self.clock.get_fps())), True, RED)

        Engine.screen.fill(BLACK)
        Engine.screen.blit(date, (30, 30))
        Engine.screen.blit(fps, (self.w - 60, 30))
        # the number of centuries past J2000.0
        Engine.dt = (Engine.time - 2451545.0) / 36525
        for planet in Engine.planet_list:
            planet.update()
            planet.display()
        pygame.display.flip()
        Engine.time = Engine.time + Engine.speed/Engine.fps

    def interpolate(self):
        sorted_x = sorted(Engine.planet_list, key=attrgetter('avg_dist'))
        min = sorted_x[1].avg_dist  # sun's value 1
        max = sorted_x[-1].avg_dist
        for planet in Engine.planet_list:
            if not planet.sun:
                planet.multiplier = interp(
                    planet.avg_dist, [min, max], [120, 30])
