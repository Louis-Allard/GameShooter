import pygame

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
background = pygame.image.load("./sprites/background.png").convert()
rect = background.get_rect()
rectScreen = surface.get_rect()