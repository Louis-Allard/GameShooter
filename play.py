import pygame
import time
from random import *

pygame.init()

WHITE = (255,255,255)
WIDTH = 1020
HEIGHT = 600
grid_w = 195
grid_h = 195
el01_w = 10
el01_h = 9
el02_w = 15
el02_h = 14
el03_w = 12
el03_h = 8
el04_w = 10
el04_h = 11

surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GameShooter")
background = pygame.image.load("./sprites/background.png").convert()
rect = background.get_rect()
rectScreen = surface.get_rect()

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

class Personnage(pygame.sprite.Sprite):
	spriteSheet = pygame.image.load("./sprites/player.png").convert_alpha()
	#[(stand),(down),(run),(fight),(die),(jump)]
	sequences = [(0,1,False),(1,3,False),(4,7,True),(10,4,True),(14,9,True),(23,6,False)]
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = Personnage.spriteSheet.subsurface(pygame.Rect(0,0,grid_w,grid_h))
		self.rect = pygame.Rect(0,0,grid_w,grid_h)
		self.rect.bottom = HEIGHT
		self.numeroSequence = 0
		self.numeroImage = 0
		self.flip = False
		self.deltaTime = 0
		self.vitesse = 6
		self.jump = 50
			
	def update(self,time):
		self.deltaTime = self.deltaTime + time
		if self.deltaTime>=150:
			self.deltaTime = 0
			n = Personnage.sequences[self.numeroSequence][0]+self.numeroImage
			self.image = Personnage.spriteSheet.subsurface(pygame.Rect(n%10*grid_w,n//10*grid_h,grid_w,grid_h)) 
			if self.flip:
				self.image = pygame.transform.flip(self.image,True,False)
			
			self.numeroImage = self.numeroImage+1
			
			if self.numeroImage == Personnage.sequences[self.numeroSequence][1]:
				if Personnage.sequences[self.numeroSequence][2]:
					self.numeroImage = 0
				else:
					self.numeroImage = self.numeroImage-1
	
	def setSequence(self,n):
		if self.numeroSequence != n:
			self.numeroImage = 0
			self.numeroSequence = n

	def goJump(self,j):
		if j == 1:
			upDown = -self.jump
		elif j== 0:
			upDown = self.jump	
		else:
			upDown = 0
			print("WARNING j is invalid")		
		self.rect = self.rect.move(0,upDown).clamp(rectScreen)   
		self.flip = False			
		self.setSequence(0)
	def goDown(self):
		self.flip = False
		self.setSequence(1)
	def walk(self,k):
		if k == 1:
			v = self.vitesse
			f = False
		elif k == 2:
			v = -self.vitesse
			f = True
		else:
			v = 0
			set.flip = False
			print("WARNING k is invalid")	
		for i in range(0,5):
			self.setSequence(2)	
			self.rect = self.rect.move(v,0).clamp(rectScreen)
			self.flip = f

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
