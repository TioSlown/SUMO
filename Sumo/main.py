import pygame #import pygame library
from pygame.locals import *

pygame.init() #initialize pygame

window = pygame.display.set_mode((640, 480)) #creation et definition des paramètres de la fenetre


background = pygame.image.load("domo.background.png").convert() #on defini et colle le fond
window.blit(background, (0, 0))

pygame.display.flip() #rafraichissement de l'image


slown = 1

while slown : #boucle qui sert à garder la fenetre ouverte
    for event in pygame.event.get():
        if event.type == QUIT:
            slown=0