import pygame
import pickle
from e.Personnage import *
from e.variables import *
from e.Enemies import *

pygame.display.set_caption("GameShooter")

stateFile = "flipState"

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,5))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

    def update(self,enemie_pos):
        print("enemie position: " + str(Enemies.rect))
        if stateFile:
            file = open(stateFile, "rb")
            flip = pickle.load(file)
            file.close()
            f = flip[0]
            if f:
                self.rect.x -= 5
                if self.rect.x <= -10:
                    self.kill()
            else:
                self.rect.x += 5
                if self.rect.x >= WIDTH + 10:
                    self.kill()
        else:
            print("No flipState file")