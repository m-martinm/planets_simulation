import sys
import pygame
from modules.Engine import *
from modules.Planet import *
from modules.Constants import *

pygame.init()
pygame.display.set_caption("Solar System Simulation")
icon = pygame.image.load("files/icon.png")
pygame.display.set_icon(icon)

engine = Engine(1800, 1000)
sun = Planet("sun",1, 695508, YELLOW, 0, 0, 0, 0, 0, 0, 0, 0, 
             0, 0, 0, 0, sun=True)
earth = Planet("earth",149.6, 6378.137,BLUE, a0=1.00000018, da=-0.00000003,
               e0=0.01673163, de=-0.00003661, L0=100.46691572, dL=35999.37306329, w0=102.93005885, dw=0.31795260, 
               b=1, c=1, s=1, f=1)
mars = Planet("mars", 228.0, 3396.2, RED, a0=1.52371243, da=-0.00000097,
              e0=0.09336511, de=0.00009149, L0=-4.56813164, dL=19140.29934243, w0=-23.91744784, dw=0.45223625, 
              b=1, c=1, s=1, f=1)
saturn = Planet("saturn", 1432.0, 58232, BEIGE, a0=9.54149883, da=-0.00003065, # radius/5
                e0=0.05550825, de=-0.00032044, L0=50.07571329, dL=1222.11494724, w0=92.86136063, dw=0.54179478,
                b=0.00025899, c=-0.13434469, s=0.87320147, f=38.351250)
venus = Planet("venus",108.2, 6051.8, RED, a0=0.72332102, da=-0.00000026,
              e0=0.00676399, de=-0.00005107, L0=-181.97970850, dL=58517.81560260, w0=0.05679648, dw=102.93005885,
              b=1, c=1, s=1, f=1)
engine.interpolate()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    engine.render()
