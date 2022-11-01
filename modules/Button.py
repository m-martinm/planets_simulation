from modules.Engine import *
import pygame

class Button:
    
    def __init__(self, name : str, path_to_img : str, pos : tuple, window):
        """Button class

        Args:
            name (str): An identifier for the button
            path_to_img (str): Path to an image to be loaded as the button
            pos (tuple): Position of the button relative to the window
            window (pygame.Rect) : Rect of the window
        """
        self.name = name
        self.img = pygame.image.load(path_to_img).convert()
        self.window = window
        self.pos = (self.window.rect.left + pos[0], self.window.rect.top + pos[1])
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 40, 40)
        
    def action(self):
        """This function (containing a "switch statement") is called if the button is clicked"""
        if self.name == "p_speed":
            self.window.engine.speed += 1
        elif self.name == "m_speed":
            self.window.engine.speed -=1
    
    def display(self):
        """Display the button"""
        self.window.engine.screen.blit(self.img, self.pos)
    
    