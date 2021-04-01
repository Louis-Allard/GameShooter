import pygame
from e.variables import *
'''
_____   __   _       _  
|  _  \ |  \ | |     | | 
| |_| | |   \| |     | | 
|  ___/ | |\   |  _  | | 
| |     | | \  | | |_| | 
|_|     |_|  \_| \_____/ 

'''

class Elements(pygame.sprite.Sprite):
    el01 = pygame.image.load("./sprites/el01.png").convert_alpha()
    el02 = pygame.image.load("./sprites/el02.png").convert_alpha()
    el03 = pygame.image.load("./sprites/el03.png").convert_alpha()
    el04 = pygame.image.load("./sprites/el04.png").convert_alpha()

    def elmnts(self,elmnts_x,elmnts_y,espace_elemnts):
        surface.blit(self.el01,(elmnts_x,elmnts_y + espace_elemnts))
        surface.blit(self.el02,(elmnts_x,elmnts_y + el01_h + espace_elemnts - 105))
        surface.blit(self.el03,(elmnts_x,elmnts_y + el02_h + espace_elemnts - 300))
        surface.blit(self.el04,(elmnts_x,elmnts_y + el03_h + espace_elemnts - 90))
