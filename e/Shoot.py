import pygame
from e.variables import *

class Shoot(pygame.sprite.Sprite):  
    bullet = pygame.image.load("./sprites/bullet.png").convert_alpha()

    def goBullet(self,bullet_x,bullet_y,pos_x,enable):
        if enable == 1:
            self.bullet.set_alpha(200)
        elif enable == 0:
            self.bullet.set_alpha(0)
        else:
            print("WARNING BULLET ALPHA")    
        surface.blit(self.bullet,(bullet_x,bullet_y))