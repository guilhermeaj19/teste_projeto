import pygame, sys
from abc import ABC, abstractmethod

class AbstractInterface(ABC):
    def __init__(self, screen, file_background_image, buttons):
        self.__screen = screen
        self.__background = pygame.image.load(file_background_image)
        self.__buttons = buttons
        self.__pressed_time = 60
        self.__button_pressed = False
        self.__change_interface = False

    def setButtonPressed(self):
        self.__button_pressed = not self.__button_pressed
    
    def getScreen(self):
        return self.__screen
    
    def getBackground(self):
        return self.__background
    
    def getChangeInterface(self):
        return self.__change_interface

    def getKey(self):
        return self.__key
    
    def setKey(self, key):
        self.__key = key
    
    def getButtons(self):
        return self.__buttons
    
    @abstractmethod
    def run(self):
        pass
    """        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            for button in self.__buttons:
                if button.colliding():
                    self.__key = button.key
                    self.setButtonPressed()
            
        key = self.update()
        if key != None:
            self.__key = None
            return key
        
        self.draw()
        self.cooldownBottonPressed()"""
    
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    def cooldownBottonPressed(self):
        current_time = pygame.time.get_ticks()
        if self.__button_pressed:
            if current_time - self.__pressed_time > self.__pressed_time:
                self.__change_interface = True
        else:
            self.__change_interface = False
    
    
    
    
    