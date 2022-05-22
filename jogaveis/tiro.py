import pygame
import os

class Tiro(pygame.sprite.Sprite):

    sprite = pygame.image.load(os.path.join("assets", "tirinho-laser.png"))
    
    na_tela = True

    velocidade = {
        'x': 0,
        'y': -0.2
    }

    tamanho = {
        'x': 5,
        'y': 10
    }

    def __init__(self, x, y):
        super().__init__()
        self.image = self.sprite
        self.rect = pygame.Rect(x, y, self.tamanho['x'], self.tamanho['y'])

    def mover(self):
        self.rect.y += self.velocidade['y']

        if self.saiuDaTela():
            self.na_tela = False

    def saiuDaTela(self):
        return self.rect.y == 0



