import pygame
import os

class Inimigo(pygame.sprite.Sprite):

    sprite = pygame.image.load(os.path.join("assets","inimigo4130.png"))
    exploding_sprite = pygame.image.load(os.path.join("assets", "explosao4042.png"))
    vida = 1

    velocidade = {
        'x' : 0,
        'y' : 1
    }

    tamanho = {
        'x' : 40,
        'y' : 40
    }


    def __init__(self, x, y):
        super().__init__()
        self.image = self.sprite
        self.rect = pygame.Rect(x,y, self.tamanho['x'], self.tamanho['y'])

    def mover(self):
        self.rect.x += self.velocidade['x']
        self.rect.y += self.velocidade['y']
    
        if self.saiuDaTela():
            self.vida = 0

    def saiuDaTela(self):
        return self.rect.y > 920
    
    def perdeVida(self):
        self.vida -= 1
        if self.vida == 0:
            self.explode()

    def explode(self):
        self.image = self.exploding_sprite
