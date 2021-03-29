import pygame
import time

pygame.init()

WIDTH = 1020
HEIGHT = 600
sprite_w = 303
sprite_h = 363

surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GameShooter")
background = pygame.image.load("./sprites/background.png").convert()
rect = background.get_rect()
rectScreen = surface.get_rect()

class Personnage(pygame.sprite.Sprite):
	spriteSheet = pygame.image.load("./sprites/player.png").convert_alpha()
	#[(stand),(down),(run),(fight),(die),(jump)]
	sequences = [(0,1,False),(1,3,True),(4,7,True),(10,4,True),(14,8,True),(23,6,True)]
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = Personnage.spriteSheet.subsurface(pygame.Rect(0,0,sprite_w,sprite_h))
		self.rect = pygame.Rect(0,0,sprite_w,sprite_h)
		self.rect.bottom = HEIGHT

		self.numeroSequence = 0
		self.numeroImage = 0
		self.flip = False

		self.deltaTime = 0
		self.vitesse = int(30)
			
	def update(self,time):
		self.deltaTime = self.deltaTime + time
		if self.deltaTime>=150:
			self.deltaTime = 0
			n = Personnage.sequences[self.numeroSequence][0]+self.numeroImage
			self.image = Personnage.spriteSheet.subsurface(pygame.Rect(n%10*100,n//10*125,sprite_w,sprite_h)) 
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
	
	def goRight(self):
		self.rect = self.rect.move(self.vitesse,0).clamp(rectScreen)
		self.flip = True
		self.setSequence(2)

	def goLeft(self):
		self.rect = self.rect.move(-self.vitesse,0).clamp(rectScreen)
		self.flip = True
		self.setSequence(2)

def main():
	clock = pygame.time.Clock()
	time = clock.tick(60)
	game_over = False
	perso = Personnage()
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					perso.goRight()
				if event.key == pygame.K_DOWN:
					perso.setSequence(1)
		perso.update(time)			
		surface.blit(background,(0,0))
		surface.blit(background,rect)
		surface.blit(perso.image,perso.rect)
		pygame.display.update()

main()
pygame.quit()
quit()
