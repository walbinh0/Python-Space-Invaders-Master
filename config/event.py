import pygame
from tiro import Tiro

class Event:

    config = None
    jogador = None

    def handleEvent(self, event):
        if event.type == pygame.QUIT:
            self.config.stopGame()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.jogador.goUp()
            if event.key == pygame.K_DOWN:
                self.jogador.goDown()
            if event.key == pygame.K_LEFT:
                self.jogador.goLeft()
            if event.key == pygame.K_RIGHT:
                self.jogador.goRight()
            if event.key == pygame.K_SPACE:
                self.config.addTiro(self.jogador.rect.x + 15, self.jogador.rect.y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.jogador.stopGoingUp()
            if event.key == pygame.K_DOWN:
                self.jogador.stopGoingUp()
            if event.key == pygame.K_LEFT:
                self.jogador.stopGoingSides()
            if event.key == pygame.K_RIGHT: 
                self.jogador.stopGoingSides()

    def __init__(self, config):
        self.config = config
        self.jogador = config.jogador