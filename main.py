import sys
import pygame
from modules.Engine import *
from modules.Planet import *
from modules.Globals import *

engine = Engine(1800, 1000, ["mercury", "venus", "earth"])
# sun = Planet("sun", 1, 695508, YELLOW,  0, 0, 0, 0, 0, 0, 0,
#              0, 0, 0, 0, 0, 0, 0, 0, 0, sun=True)

# earth = Planet("earth", 149.6, 6378.137, BLUE, a0=1.00000018, da=-0.00000003, e0=0.01673163, de=-
#                0.00003661, I0=-0.00054346, dI=-0.01337178, L0=100.46691572, dL=35999.37306329, w0=102.93005885, dw=0.31795260, Omega0=-5.11260389, dOmega=49.71320984, b=1, c=1, s=1, f=1)

# mars = Planet("mars", 228.0, 3396.2, RED, a0=1.52371243, da=-0.00000097, e0=0.09336511, de=0.00009149, I0=1.85181869, dI=-0.00724757,
#               L0=-4.56813164, dL=19140.29934243, w0=-23.91744784, dw=0.45223625, Omega0=49.71320984, dOmega=-0.26852431, b=1, c=1, s=1, f=1)

engine.main()