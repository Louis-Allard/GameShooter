import pygame

WIDTH = 1020
HEIGHT = 600
grid_w = 195
grid_h = 195
el01_w = 10
el01_h = 9
el02_w = 12
el02_h = 11
el03_w = 12
el03_h = 8
el04_w = 10
el04_h = 11
enemie01_w = 50
enemie01_h = 80
elemts_vitesse = 10
enemie_vitesse = 2
pos_x = 0
pos_y = 0

surface = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("./sprites/background.png").convert()
rect = background.get_rect()
rectScreen = surface.get_rect()