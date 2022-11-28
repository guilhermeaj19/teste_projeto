import pygame, sys

from settings import WIDTH, HEIGTH, FPS
from interfaceController import InterfaceController

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.__interfaceController = InterfaceController()
        self.__actualInterface = self.__interfaceController.firstInterface()
        self.__nextInterface = None
        self.__key = None
        self.start()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                        
            key = self.__actualInterface.run()
                
            if key != None:
                self.__nextInterface = self.__interfaceController.nextInterface(key)

            if (not pygame.mouse.get_pressed()[0]) and (self.__nextInterface != None):
                self.__actualInterface = self.__nextInterface
            
            
            self.clock.tick(FPS)             
            pygame.display.flip()
                
game = Game()

