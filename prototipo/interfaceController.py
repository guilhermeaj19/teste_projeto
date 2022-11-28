from ingame import InGame
from interfaces.menuInterface import MenuInterface
from interfaces.gameoverInterface import GameOverInterface

class InterfaceController:
    def firstInterface(self):
        return MenuInterface()
    
    def nextInterface(self, key):
        if key == 'mainmenu':
            return MenuInterface()
        elif key == 'start' or key == 'continue' or key == 'restart':
            return InGame()
        elif key == 'morreu':
            return GameOverInterface()