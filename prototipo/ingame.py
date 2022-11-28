import pygame, sys
from settings import *
from level import Level
from interfaces.pauseInterface import PauseInterface

class InGame:
    def __init__(self):
        # Configuração inicial
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.pause = PauseInterface()
        self.level = Level()

    def run(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            key = self.pause.run()
                    
            if key == 'restart':
                self.level = Level()
                    
            if key == 'mainmenu':
                return key
            
        if self.level.getPlayerDead():
            return 'morreu'

        self.screen.fill((0, 0, 0))
        self.level.run()

