import pygame
import sys
from modules.Button import Button

class Settings:

    def __init__(self, engine):
        self.w = 500
        self.h = 500
        self.engine = engine
        self.rect = pygame.Rect(
            engine.center[0] - self.w/2, engine.center[1] - self.h/2, self.w, self.h)
        self.run = True
        self.button_list = []
        self.load_buttons()
        
    def load_buttons(self):
        p_speed = Button("p_speed", "assets/images/plus_button.png", (40,40), self)
        m_speed = Button("m_speed", "assets/images/minus_button.png", (2*40, 40), self)
        
        self.button_list.append(m_speed)
        self.button_list.append(p_speed)

    def event_handler_settings(self):
        mouse_state = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.run = False
            elif mouse_state[0]:
                for button in self.button_list:
                    if button.rect.collidepoint(mouse_pos):
                        button.action()
                    
    def render_text(self):
        settings = self.engine.font.render("Press [ENTER] to close settings", True, self.engine.colors.get("WHITE"))
        self.engine.screen.blit(settings, (self.engine.w/2 - self.engine.font.size("Press [ENTER] to close settings")[0]/2, 30))
        speed =  self.engine.font.render(f"Current speed: {self.engine.speed}", True, self.engine.colors.get("BLACK"))
        self.engine.screen.blit(speed, (self.rect.left + 4*40, self.rect.top + 60))

    def render_settings(self):
        
        pygame.draw.rect(self.engine.screen,
                         self.engine.colors.get("WHITE"), self.rect)
        for button in self.button_list:
            button.display()

    def settings_loop(self):
        """A while loop which exits if [ENTER] is pressed and settings are saved"""
        self.run = True
        self.engine.screen.fill(self.engine.colors.get("GRAY"))
        while self.run:
            self.event_handler_settings()
            self.render_settings()
            self.render_text()
            pygame.display.flip()
