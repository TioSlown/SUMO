import pygame #on importe la pygame
from players import *
from pygame.locals import *
import time

pygame.init() #on initialise pygame

window = pygame.display.set_mode((1280, 720))

background = pygame.image.load("background.png").convert()

touche = {} #dictionnaire qui les touches préssées et les enregistres pour permettre des déplacements fluides

continuer = 1

player1 = Players('macron.png', 100, 310)
player2 = Players('mlp.png', 865, 300)

timer = pygame.time.Clock()

while continuer:

    print(touche)

    window.blit(background, (0,0))   #on applique les images nécéssaires (background, les joueurs)
    window.blit(player1.image, player1.rect)
    window.blit(player2.image, player2.rect)

    if pygame.sprite.collide_rect(player1, player2) == True:

        if touche.get(pygame.K_z):
            if player1.stamina > 0 :
                player2.rect.x += 10 * dt
                player1.stamina -= 10
                print(player1.stamina)

        if touche.get(pygame.K_DOWN):
            if player2.stamina > 0 :
                player1.rect.x -= 10 * dt
                player2.stamina -= 10

    if pygame.sprite.collide_rect(player1, player2) == False:

        if touche.get(pygame.K_LEFT):
            player2.reculer(dt)

        if touche.get(pygame.K_e):
            player1.avancer(dt)

    if touche.get(pygame.K_RIGHT):
        player2.avancer(dt)

    if touche.get(pygame.K_a):
        player1.reculer(dt)

    player1.barre_stamina(window, 25)
    player2.barre_stamina(window, 1055)

    pygame.display.flip() #on rafraichit l'écran

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            continuer = 0
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            touche[event.key] = True
        elif event.type == pygame.KEYUP:
            touche[event.key] = False

    dt = timer.tick(60) #en ms, bloque les fps
    print(dt)

