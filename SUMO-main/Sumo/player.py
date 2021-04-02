import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.stamina = 100
        self.image = pygame.image.load('player1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 302
        self.rect.y = 300

    def avancer(self, dt):
        print(dt, "trololo")
        self.rect.y -= 0.09 * dt
