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
        self.rect = pygame.Rect(WIDTH - 100,0,enemie01_w,enemie01_h)
        self.rect.bottom = HEIGHT - 50             
        self.enemie_x = self.rect.right
        self.enemie_y = 0

    def update(self,time):
        self.rect.x -= enemie_vitesse
        if self.rect.x <= 0:
            self.rect.x = WIDTH - 50
