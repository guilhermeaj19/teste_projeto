import pygame
import pygame_widgets

from pygame_widgets.slider import Slider
from interfaces.internalInterface import InternalInterface
from interfaces.button import Button

class OptionsInterface(InternalInterface):
    def __init__(self):
        buttons = pygame.sprite.Group([Button(150, 50, 'interfaces\Botoes\\botao_mainmenu_hover.png', 
                                                       'interfaces\Botoes\\botao_mainmenu.png',
                                                       'interfaces\Botoes\\botao_mainmenu_pressed.png', 'voltar')])
        super().__init__(pygame.display.get_surface(), 'interfaces\\telaOptions.png', buttons)
        
        self.__slider = Slider(self.getScreen(), 175, 300, 400, 30, colour = (225, 215, 208), handleColour = (132, 116, 110))

    def update(self):
        if self.getChangeInterface():
            return self.getKey()

    def draw(self):
        self.getButtons().update()
        pygame_widgets.update(pygame.event.get())
        self.getScreen().fill((0,0,0))
        self.getScreen().blit(self.getBackground(), ((1280-self.getBackground().get_rect()[2])//2,0))
        self.getButtons().draw(self.getScreen())
        self.__slider.draw()
