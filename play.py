import pygame
import time

pygame.init()

WIDTH = 1020
HEIGHT = 600
perso_standW = 75
perso_standH = 100
perso_stit01W = 75
perso_sit01H = 89
perso_sit02W = 75
perso_sit02H = 75

surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GameShooter")
background = pygame.image.load("./sprites/background.png").convert()
rect = background.get_rect()
perso_stand = pygame.image.load("./sprites/perso_stand.png")
perso_sit01 = pygame.image.load("./sprites/perso_sit01.png")
perso_sit02 = pygame.image.load("./sprites/perso_sit02.png")

########### Ex #######
class Personnage(pygame.sprite.Sprite):
	spriteSheet = pygame.image.load("./sprites/persoUpDown.png").convert_alpha()
	sequences = [(0,1,False),(1,3,True)]
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = Personnage.spriteSheet.subsurface(pygame.Rect(0,0,99,125))
		self.rect = pygame.Rect(0,0,99,125)
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
			self.image = Personnage.spriteSheet.subsurface(pygame.Rect(n%10*100,n//10*125,99,125)) 
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
	
	def down(self):
    		#flip => indique si l'image doit être retournée
		#self.rect = self.rect.move(self.vitesse,0).clamp(rect)
		self.flip = False 
		self.setSequence(1)

	def goLeft(self):
		self.rect = self.rect.move(-self.vitesse,0).clamp(rect)
		self.flip = True
		self.setSequence(1)

#########

def perso_change(perso_x,perso_y,image):
    surface.blit(background,rect)
    #surface.blit(image,(perso_x,perso_y))

def perso(perso_x,perso_y,image):
        surface.blit(image,(perso_x,perso_y))

def main():
    clock = pygame.time.Clock()
    game_over = False
    perso_x = 30
    perso_y = 500
    move_x = 0
    perso = Personnage()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 5
                if event.key == pygame.K_DOWN:
                    perso.down()
        surface.blit(background,(0,0))
        surface.blit(background,rect)
        surface.blit(perso.image,perso.rect)
        #surface.blit(perso_stand, (perso_x,perso_y))
        #perso(perso_x,perso_y,perso_stand)
        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()
