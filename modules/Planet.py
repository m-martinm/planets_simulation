import pygame
import modules.compute
import numpy as np
import modules.Engine


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

    def __init__(self, name, avg_dist, radius, color, a0, da, e0, de, I0, dI, L0, dL, w0, dw, Omega0, dOmega, b, c, s, f, sun=False):
        self.r = np.log(radius)  # scale down for the animation
        self.name = name
        self.avg_dist = avg_dist
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
        self.Omega0 = Omega0
        self.dOmega = dOmega

        # additional terms for some bodies
        self.b = b
        self.c = c
        self.s = s
        self.f = f
        self.sun = sun

        self.pos = [0,0]

    def update(self, dt : float, center : tuple):

        if self.sun == True:
            pass

        else:

            # cpdef Point compute_coordinates(double dt, double a0, double da, double e0,
            #                                 double de, double L0, double dL, double w0,
            #                                 double dw, double b, double c, double s,
            #                                 double f):
            coordinates = modules.compute.compute_coordinates(
                dt, self.a0, self.da, self.e0, self.de, self.I0, self.dI, self.L0, self.dL, self.w0, self.dw, self.Omega0,self.dOmega,self.b, self.c, self.s, self.f)

            self.pos[0] = center[0] + coordinates['x']*150
            self.pos[1] = center[1] + coordinates['y']*150
            
