import pygame
from e.Personnage import *
from e.variables import *

pygame.display.set_caption("GameShooter")

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,5))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        print("k = " + str(Personnage.walk))

    def update(self):
        self.rect.x  += 5
