import pygame
from abc import ABC, abstractmethod

#Deve ser uma classe Abstrata
class Item(ABC, pygame.sprite.Sprite):
    def  __init__(self, x, y, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.sprite = sprite
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.hitbox = self.rect.inflate(0,0)
        self.posicao = [self.x, self.y]
    
    @abstractmethod
    def use(self, jogador):
        pass
        
    def exclui(self):
        self.kill()

    def draw(self, x, y, valor, pos, surface):
        surface.blit(self.image, (valor*pos+x, y-4))