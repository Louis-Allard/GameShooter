import pygame
from e.variables import *

'''
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
        self.rect.bottom = HEIGHT + 10                