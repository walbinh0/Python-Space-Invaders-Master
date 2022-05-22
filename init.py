import os
import sys
import pygame
sys.path.append("./config")
sys.path.append("./jogaveis")
sys.path.append("./constants")
sys.path.append("./assets")

from tiro import Tiro
from colors import BLACK
from general_config import General_Config
from event import Event

pygame.init()

config = General_Config()

screen = pygame.display.set_mode(
    [config.tamanho_tela['x'], config.tamanho_tela['y']])

jogador = config.jogador
mapa = config.mapa
eventHandler = Event(config)

contador = 0

while config.jogo_rodando:
    for event in pygame.event.get():
        eventHandler.handleEvent(event)

    
    
    config.deletaEntidadesMortas()
    config.checaColisao()

    jogador.mover()

    for inimigo in config.inimigos:
        inimigo.mover()

    for tiro in config.tiros:
        tiro.mover()

    contador += 1

    if contador > 100:
        config.doRandomIngameEvent()
        contador = 0

    # RENDERIZAÇÃO
    screen.fill(BLACK)
    config.inimigos.draw(screen)
   
    config.tiros.draw(screen)

    screen.blit(jogador.image, [jogador.rect.x, jogador.rect.y])

    pygame.display.update()



#TODO
# EXTRA -> Algum tipo de powerup
# Blocos de atrapalhar