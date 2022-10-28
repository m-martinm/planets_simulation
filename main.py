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
sun = Planet(False, 6955*3,YELLOW, 0, 0, 0, 0, 0, 0, 0, 0, # radius/33
             0, 0, 0, 0, 0, 0, 0, 0, sun=True)
earth = Planet(False, 6378.137,BLUE, a0=1.00000018, da=-0.00000003,
               e0=0.01673163, de=-0.00003661, I0=-0.00054346, dI=-0.01337178,
               L0=100.46691572, dL=35999.37306329, w0=102.93005885, dw=0.31795260,
               W0=-5.11260389, dW=-0.24123856, b=1, c=1, s=1, f=1)
mars = Planet(False, 3396.2, RED, a0=1.52371243, da=-0.00000097,
              e0=0.09336511, de=0.00009149, I0=1.85181869, dI=-0.00724757,
              L0=-4.56813164, dL=19140.29934243, w0=-23.91744784, dw=0.45223625,
              W0=49.71320984, dW=-0.26852431, b=1, c=1, s=1, f=1)
saturn = Planet(True, 6026*2, BEIGE, a0=9.54149883, da=-0.00003065, # radius/5
                e0=0.05550825, de=-0.00032044, I0=2.49424102, dI=0.00451969,
                L0=50.07571329, dL=1222.11494724, w0=92.86136063, dw=0.54179478,
                W0=113.63998702, dW=-0.25015002, b=0.00025899, c=-0.13434469, s=0.87320147, f=38.351250)
venus = Planet(False, 6051.8, RED, a0=0.72332102, da=-0.00000026,
              e0=0.00676399, de=-0.00005107, I0=3.39777545, dI=0.00043494,
              L0=-181.97970850, dL=58517.81560260, w0=0.05679648, dw=102.93005885,
              W0=-0.27274174, dW=-5.11260389, b=1, c=1, s=1, f=1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    engine.render()
