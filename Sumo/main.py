import pygame #import pygame library
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.stamina = 100
        self.velocity = 5
        self.image = pygame.image.load('player1.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = 302
        self.rect.y = 300

pygame.init() #initialize pygame

window = pygame.display.set_mode((640, 480)) #creation et definition des paramètres de la fenetre

player1 = Player()


background = pygame.image.load("domo.background.png").convert() #on defini et colle le fond

slown = 1

while slown : #boucle qui sert à garder la fenetre ouverte

    window.blit(background, (0, 0))
    window.blit(player1.image, player1.rect)

    pygame.display.flip() #rafraichissement de l'image

    for event in pygame.event.get():
        if event.type == QUIT:
            slown=0
            pygame.quit()