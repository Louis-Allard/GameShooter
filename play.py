import pygame
import time
from random import *
from e.Personnage import Personnage
from e.Elements import Elements
from e.Enemies import Enemies
from e.variables import *

pygame.init()

def main():
	game_over = False
	perso = Personnage()
	perso_group = pygame.sprite.Group()
	perso_group.add(perso)
	bullet_group = pygame.sprite.Group()
	enemies = Enemies()
	enemies_group = pygame.sprite.Group()
	enemies_group.add(enemies)
	elmts = Elements()  	
	clock = pygame.time.Clock()
	time = clock.tick(5)
	elmnts_x = WIDTH
	elmnts_y = randint(-20,610)
	espace_elemnts = el04_h * randint(2,10)
	enable = 0 

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
				if event.key == pygame.K_UP:
					perso.goJump(1)	
				if event.key == pygame.K_SPACE:
					bullet_group.add(perso.create_bullet())
			if event.type == pygame.KEYUP:	
				if event.key == pygame.K_UP:
					perso.goJump(0)			
				if event.key == pygame.K_SPACE:
					enable = 0
				perso.setSequence(0)		
		
		perso.update(time)		
		surface.blit(background,(0,0))
		surface.blit(background,rect)
		elmts.elmnts(elmnts_x,elmnts_y,espace_elemnts)
		surface.blit(perso.image,perso.rect)    
		perso_group.draw(surface)
		perso_group.update(time)
		enemies_group.draw(surface)
		enemies_group.update(time)
		bullet_group.draw(surface)
		bullet_group.update()

		elmnts_x -= elemts_vitesse
		if elmnts_x < 20:
			elmnts_x = WIDTH
			elmnts_y = randint(-0,HEIGHT)
	
		pygame.display.flip()
main()
pygame.quit()
quit()
