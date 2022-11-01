from operator import attrgetter
import pygame
import sys
from modules.Globals import *
from pandas import Timestamp, to_datetime
from numpy import interp
from json import load
from modules.Planet import Planet


class Engine:

    button_list = []

    def __init__(self, width: int, height: int, simulated_planets: list):
        """The main class of the application, it has to be created once

        Args:
            width (int): screen width
            height (int): screen height
        Functions: 
            event_handler : Function to handel events in the main loop
            render_buttons : Display all of the buttons
            render_text : Updates all the text displayed on the screen and blits it
            render_planets : Update and display all the planets contained in planet_list
            main : This function has to be called after the creation of the class instance
        """
        # pygame init
        pygame.init()
        pygame.display.set_caption("Solar System Simulation")
        self.icon = pygame.image.load("assets/images/icon.png")
        pygame.display.set_icon(self.icon)

        # instance variables
        self.w = width
        self.h = height
        self.size = width, height
        self.center = (self.w/2, self.h / 2)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('freeserif', 22)
        self.planet_names = simulated_planets
        self.planet_list = []

        # class variables
        self.screen = pygame.display.set_mode(self.size)
        self.fps = 30
        self.time = Timestamp.today(tz="UTC").to_julian_date()
        self.speed = 30  # in [days/sec]

    def create_planet(self, data: dict, planet_name : str):
        """Reads the necesarry data from the data file and creates an instance
            of the Planet class
        """
        for x in data.get("Planets"):
            if x.get("name") == planet_name:
                dict = x
                break
        tmp = Planet(
            planet_name, dict.get("avg_dist"), dict.get("radius"),
            dict.get("color"), dict.get("a0"), dict.get("da"), dict.get("e0"),
            dict.get("de"), dict.get("I0"), dict.get("dI"), dict.get("L0"),
            dict.get("dL"), dict.get("w0"), dict.get("dw"), dict.get("Omega0"),
            dict.get("dOmega"), dict.get("b"), dict.get(
                "c"), dict.get("s"), dict.get("f")
        )
        self.planet_list.append(tmp)

    def load_planets(self):
        """A wrapper function for create_planet(), creates all the planets in self.planet_names """
        with open("assets/rawdata.json") as f:
            planets_data = load(f)

        self.planet_names.append("sun")
        for planet in self.planet_names:
            self.create_planet(planets_data, planet)

    def event_handler(self):
        """Function to handel events in the main loop"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def render_buttons(self):
        """Display all of the buttons"""
        pass

    def render_text(self):
        """Updates all the text displayed on the screen and blits it"""
        date = self.font.render(
            f"Date: {to_datetime(self.time, origin= 'julian', unit='D').date()}", True, WHITE)
        fps = self.font.render(str(int(self.clock.get_fps())), True, RED)
        self.screen.blit(date, (30, 30))
        self.screen.blit(fps, (self.w - 60, 30))

    def render_planets(self):
        """Update and display all the planets contained in self.planet_list"""
        dt = (self.time - 2451545.0) / 36525
        for planet in self.planet_list:
            planet.update(dt, self.center)
            pygame.draw.circle(self.screen, planet.color, planet.pos, planet.r)
        self.time = self.time + self.speed/self.fps

    def main(self):
        """Main loop of the application"""
        self.load_planets()

        while True:
            self.clock.tick(self.fps)
            self.screen.fill(BLACK)
            self.event_handler()
            # self.render_buttons()
            self.render_text()
            self.render_planets()
            pygame.display.flip()


    def render(self):
        self.clock.tick(self.fps)
        # converting the Julian Date back to human readable format
        date = self.font.render(
            f"Date: {to_datetime(self.time, origin= 'julian', unit='D').date()}", True, WHITE)
        fps = self.font.render(str(int(self.clock.get_fps())), True, RED)

        self.screen.fill(BLACK)
        self.screen.blit(date, (30, 30))
        self.screen.blit(fps, (self.w - 60, 30))
        # the number of centuries past J2000.0
        DT = (self.time - 2451545.0) / 36525
        for planet in self.planet_list:
            planet.update()
            planet.display()
        pygame.display.flip()
        self.time = self.time + self.speed/self.fps