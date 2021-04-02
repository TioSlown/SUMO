import pygame #import pygame library
from pygame.locals import *
from game import *

pygame.init() #initialize pygame

window = pygame.display.set_mode((640, 480)) #creation et definition des paramètres de la fenetre

background = pygame.image.load("domo.background.png").convert() #on defini et colle le fond

game =  Game()

slown = 1

timer = pygame.time.Clock()

while slown : #boucle qui sert à garder la fenetre ouverte

    window.blit(background, (0, 0))
    window.blit(game.player1.image, game.player1.rect)

    if game.touche.get(pygame.K_UP):
        print(dt, 'k')
        game.player1.avancer(dt)

    pygame.display.flip() #rafraichissement de l'image

    for event in pygame.event.get():

        if event.type == QUIT:
            slown=0
            pygame.quit()

        elif event.type == pygame.KEYDOWN :
            game.touche[event.key] = True
        elif event.type == pygame.KEYUP :
            game.touche[event.key] = False

    dt = timer.tick(60) #en ms, "40" -> bloque les fps à 40
    print(dt)