import pygame, sys

from settings import WIDTH, HEIGTH, FPS
from ingame import InGame
from interfaces.menuInterface import MenuInterface
from interfaces.gameoverInterface import GameOverInterface

class InterfaceController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.__actualInterface = MenuInterface()
        self.__pressed_time = 60
        self.__button_pressed = False
        self.__change_interface = False
        self.start()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            key = self.__actualInterface.run()
            
            if key != None:
                if key == 'mainmenu':
                    self.__actualInterface = MenuInterface()
                elif key == 'start' or key == 'continue' or key == 'restart':
                    self.__actualInterface = InGame()
                elif key == 'morreu':
                    self.__actualInterface = GameOverInterface()

            self.clock.tick(FPS)
            self.cooldownBottonPressed()
            pygame.display.flip()
    
    def cooldownBottonPressed(self):
        current_time = pygame.time.get_ticks()
        if self.__button_pressed:
            if current_time - self.__pressed_time > self.__pressed_time:
                self.__change_interface = True
        else:
            self.__change_interface = False
                
game = InterfaceController()

