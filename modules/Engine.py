import pygame
import sys
import os
from pandas import Timestamp, to_datetime
from json import load
from modules.Planet import Planet
from modules.Settings import *


class Engine:

    colors = {"BLACK": (0, 0, 0), "WHITE": (255, 255, 255), "BLUE": (21, 5, 255),
              "YELLOW": (255, 225, 5), "RED": (153, 82, 7), "BEIGE": (224, 195, 107),
              "L_BLUE": (88, 195, 221), "GRAY": (85, 85, 85)}

    def __init__(self, width: int, height: int, simulated_planets: list):
        """The main class of the application, it has to be created once

        Args:
            width (int): screen width
            height (int): screen height
            simulated_planets (list): list of all the planets which have to be drawn
        Functions: 
            event_handler : Function to handel events in the main loop
            render_text : Updates all the text displayed on the screen and blits it
            render_planets : Update and display all the planets contained in planet_list
            main : This function has to be called after the creation of the class instance
        """
        # pygame init
        os.system("cls")
        print("Loading engine...")
        pygame.init()
        pygame.display.set_caption("Solar System Simulation")
        self.icon = pygame.image.load("assets/images/icon.png")
        pygame.display.set_icon(self.icon)

        # variables
        self.w = width
        self.h = height
        self.size = width, height
        self.center = (self.w/2, self.h / 2)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('consolas', 16)
        self.screen = pygame.display.set_mode(self.size)
        self.planet_names = simulated_planets
        self.planet_list = []
        self.fps = 30
        self.time = Timestamp.today(tz="UTC").to_julian_date()
        self.speed = 10  # in [days/sec]
        self.settings = Settings(self)

    def create_planet(self, data: dict, planet_name: str):
        """Reads the necesarry data from the data file and creates an instance
            of the Planet class
        """
        print(f"Loading {planet_name}...")
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.settings.settings_loop()
                elif event.key == pygame.K_SPACE:
                    if self.speed > 0:
                        self.speed = 0
                    else:
                        self.speed = 10

    def render_text(self):
        """Updates all the text displayed on the screen and blits it"""

        # texts
        date = self.font.render(
            f"Date: {to_datetime(self.time, origin= 'julian', unit='D').date()}", True, self.colors.get("WHITE"))
        fps = self.font.render(
            "FPS  " + str(int(self.clock.get_fps())), True, self.colors.get("RED"))
        Engine_data = self.font.render(
            f"Speed  {self.speed} [days/sec]", True, self.colors.get("WHITE"))
        settings = self.font.render(
            "Press [ESC] to open settings", True, self.colors.get("WHITE"))
        pause = self.font.render(
            "Press [SPACE] to pause", True, self.colors.get("WHITE"))

        # blit
        self.screen.blit(
            pause, (self.w/2 - self.font.size("Press [SPACE] to pause")[0]/2, 60))
        self.screen.blit(
            settings, (self.w/2 - self.font.size("Press [ESC] to open settings")[0]/2, 30))
        self.screen.blit(Engine_data, (30, 60))
        self.screen.blit(date, (30, 30))
        self.screen.blit(fps, (self.w - 80, 30))

    def render_planets(self):
        """Update and display all the planets contained in self.planet_list"""
        dt = (self.time - 2451545.0) / 36525
        for planet in self.planet_list:
            planet.update(dt, self.center)
            pygame.draw.circle(self.screen, self.colors.get(
                str(planet.color)), planet.pos, planet.r)
        self.time = self.time + self.speed/self.fps

    def main(self):
        """Main loop of the application"""

        print("starting the simulation")
        self.load_planets()

        while True:
            self.clock.tick(self.fps)
            self.screen.fill(self.colors.get("BLACK"))
            self.event_handler()
            self.render_text()
            self.render_planets()
            pygame.display.flip()
