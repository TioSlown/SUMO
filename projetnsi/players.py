import pygame

class Players(pygame.sprite.Sprite):

    def __init__(self, cheminImage, x, y):
            super().__init__()
            self.stamina = 100
            self.image = pygame.image.load(cheminImage).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def barre_stamina(self, ecran, x):

        xpos =x

        couleur_fond = (255, 255, 255)
        position_fond = [xpos, 25, 200, 15]
        pygame.draw.rect(ecran, couleur_fond, position_fond)

        couleur_barre = (205, 92, 92)
        position_barre = [xpos, 25, self.stamina*2, 15]

        pygame.draw.rect(ecran, couleur_barre, position_barre)

    def avancer(self, dt):
        self.rect.x += 0.50 * dt

    def reculer(self, dt):
        self.rect.x -= 0.50 * dt
    
