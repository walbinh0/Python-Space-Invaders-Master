import pygame
import os

class Navezinha(pygame.sprite.Sprite):
    sprite = pygame.image.load(os.path.join("assets","player4130.png"))
    vida = 3

    velocidade = {
        'x': 0,
        'y': 0
    }
    
    posicaoInicial = {
        'x': 630, 
        'y': 850
    }

    tamanho = {
        'x' : 40,
        'y' : 40
    }

    def __init__(self):
        super().__init__()
        self.image = self.sprite
        self.rect = pygame.Rect(self.posicaoInicial['x'], self.posicaoInicial['y'], self.tamanho['x'], self.tamanho['y'])    

    def mover(self):
        self.rect.x += self.velocidade['x']
        self.rect.y += self.velocidade['y']

    def perdeVida(self):
        self.vida -= 1

    def goUp(self):
        self.velocidade['y'] = -1
    def goDown(self):
        self.velocidade['y'] = 1
    def goLeft(self):
        self.velocidade['x'] = -1
    def goRight(self):
        self.velocidade['x'] = 1

    def stopGoingUp(self):
        self.velocidade['y'] = 0
    def stopGoingSides(self):
        self.velocidade['x'] = 0

