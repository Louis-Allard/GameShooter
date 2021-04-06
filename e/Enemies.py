import pygame
from e.variables import *

'''
 _____   __   _   _____       ___   __   _   _____    _____
| ____| |  \ | | | ____|     /   |/   | | | | ____| /  ___/ 
| |__   |   \| | | |__      / /|   /| | | | | |__   | |___  
|  __|  | |\   | |  __|    / / |__/ | | | | |  __|  \___  \ 
| |___  | | \  | | |___   / /       | | | | | |___   ___| | 
|_____| |_|  \_| |_____| /_/        |_| |_| |_____| /_____/ 
'''

class Enemies(pygame.sprite.Sprite):
    enemie01 = pygame.image.load("./sprites/enemie01.png").convert_alpha()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Enemies.enemie01.subsurface(pygame.Rect(0,0,enemie01_w,enemie01_h))
        self.rect = pygame.Rect(0,0,enemie01_w,enemie01_h)
        self.rect.bottom = HEIGHT - 50             
        self.rect.right = WIDTH - 50 
        self.enemie_x = WIDTH
        self.enemie_y = 0
    
    def ene(self,enemie_x,enemie_y):
        surface.blit(self.enemie01,(enemie_x,enemie_y))
