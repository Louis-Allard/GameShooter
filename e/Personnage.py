import pygame
from e.Bullet import *
from e.variables import *

pygame.display.set_caption("GameShooter")

game_over = False

class Personnage(pygame.sprite.Sprite):
	player = pygame.image.load("./sprites/player.png").convert_alpha()
	#[(stand),(down),(run),(fight),(die),(jump)]
	sequences = [(0,1,False),(1,3,False),(4,7,True),(10,4,True),(14,9,True),(23,6,False)]
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = Personnage.player.subsurface(pygame.Rect(0,0,grid_w,grid_h))
		self.rect = pygame.Rect(0,0,grid_w,grid_h)
		self.rect.bottom = HEIGHT
		self.numeroSequence = 0
		self.numeroImage = 0
		self.flip = False
		self.deltaTime = 0
		self.vitesse = 6
		self.jump = 50	
		pos_x = self.rect[0]
		pos_y = self.rect[1]
	
	def update(self,time):
		self.deltaTime = self.deltaTime + time
		if self.deltaTime>=150:
			self.deltaTime = 0
			n = Personnage.sequences[self.numeroSequence][0]+self.numeroImage
			self.image = Personnage.player.subsurface(pygame.Rect(n%10*grid_w,n//10*grid_h,grid_w,grid_h)) 
			if self.flip:
				self.image = pygame.transform.flip(self.image,True,False)
			
			self.numeroImage = self.numeroImage+1
			
			if self.numeroImage == Personnage.sequences[self.numeroSequence][1]:
				if Personnage.sequences[self.numeroSequence][2]:
					self.numeroImage = 0
				else:
					self.numeroImage = self.numeroImage-1

	def create_bullet(self):
		bullet_x = self.rect[0]
		bullet_y = self.rect[1] + 100
		return Bullet(bullet_x,bullet_y)

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
		print("goDown")
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
			print("perso_x = " + str(self.rect[0]))