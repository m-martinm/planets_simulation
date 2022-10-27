import sys
import ctypes
from modules.Engine import *
from modules.Planet import *
from modules.Constants import *

engine = Engine(1200, 1200)
sun = Planet(30, YELLOW, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, sun=True)
earth = Planet(15, BLUE, a0=1.00000018, da=-0.00000003,
              e0=0.01673163, de=-0.00003661, I0=-0.00054346, dI=-0.01337178,
              L0=100.46691572, dL=35999.37306329, w0=102.93005885, dw=0.31795260,
              W0=-5.11260389, dW=-0.24123856, b=1, c=1, s=1, f=1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    engine.render()
