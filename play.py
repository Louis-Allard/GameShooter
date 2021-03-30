import pygame
import time
from random import *
from e.Personnage import Personnage
from e.variables import *

pygame.init()

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

def main():
	clock = pygame.time.Clock()
	time = clock.tick(500)
	game_over = False
	pos_x = 0
	pos_y = 0	
	perso = Personnage()
	elmts = Elements()
	elemts_vitesse = 10
	elmnts_x = WIDTH
	elmnts_y = randint(-20,610)
	espace_elemnts = el04_h * randint(2,10)
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					perso.walk(1)
				if event.key == pygame.K_LEFT:
					perso.walk(2)	
				if event.key == pygame.K_DOWN:
					perso.goDown()
				if event.key == pygame.K_SPACE:
					perso.goJump(1)	
			if event.type == pygame.KEYUP:	
				if event.key == pygame.K_SPACE:
					perso.goJump(0)			
				perso.setSequence(0)		

		perso.update(time)			
		surface.blit(background,(0,0))
		surface.blit(background,rect)
		elmts.elmnts(elmnts_x,elmnts_y,espace_elemnts)
		surface.blit(perso.image,perso.rect)
		elmnts_x -= elemts_vitesse
		if elmnts_x < 20:
			elmnts_x = WIDTH
			elmnts_y = randint(-0,HEIGHT)

		pygame.display.update()
main()
pygame.quit()
quit()
