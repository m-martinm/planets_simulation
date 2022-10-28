import pygame
from modules.Engine import *
from modules.Constants import *
import modules.compute 

class Planet:

    """
    a0, da : semi-major axis [au, au/century]
    e0, de : eccentricity
    I0, dI : inclination [degrees, degrees/century]
    L0, dL : mean longitude [degrees, degrees/century]
    w0, dw (omega): longitude of perihelion [degrees, degrees/century]
    W0, dW (capital omega) : longitude of the ascending node [degrees, degrees/century]
    b, c, s, f additional terms for Jupiter through Neptune
    """

    def __init__(self, name,radius, color, a0, da, e0, de, I0, dI, L0, dL, w0, dw, W0, dW, b, c, s, f, sun=False):
        self.r = radius   # scale down for the animation
        self.name = name
        self.color = color
        self.a0 = a0
        self.da = da
        self.e0 = e0
        self.de = de
        self.I0 = I0
        self.dI = dI
        self.L0 = L0
        self.dL = dL
        self.w0 = w0
        self.dw = dw
        self. W0 = W0
        self.dW = dW

        # additional terms for some bodies
        self.b = b
        self.c = c
        self.s = s
        self.f = f
        self.sun = sun

        self.pos = [Engine.center[0], Engine.center[1]]

        Engine.planet_list.append(self)

    def display(self):
        pygame.draw.circle(Engine.screen, self.color, self.pos, self.r)

    def update(self):
        if self.sun == True:
            pass

        else:
            # double eccentric_anomaly(double period, double dt, double eccentricity) {...} where dt is the time elapsed since perihelion
            coordinates = modules.compute.compute_coordinates(Engine.dt, self.a0, self.da, self.e0, self.de, self.I0, self.dI,
                                                             self.L0, self.dL, self.w0, self.dw, self.W0, self.dW, self.b, self.c, self.s, self.f)
            self.pos[0] = Engine.center[0] + round(coordinates['x']*50, 5)
            self.pos[1] = Engine.center[1] + round(coordinates['y']*50, 5)
