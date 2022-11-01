from modules.Engine import *


class Button:
    
    def __init__(self, name : str, path_to_img : str, pos : tuple):
        """Button class

        Args:
            name (str): An identifier for the button
            path_to_img (str): Path to an image to be loaded as the button
            pos (tuple): Position of the button
        """
        self.name = name
        self.path = path_to_img
        self.pos = pos
        
        Engine.button_list.append(self)
    
    def action(self):
        """This function (containing a "switch statement") is called if the button is clicked"""
        pass
    
    def display(self):
        """Display the button"""
        pass
    
    