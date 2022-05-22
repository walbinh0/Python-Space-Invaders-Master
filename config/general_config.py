from navezinha import Navezinha
from inimigo import Inimigo
from tiro import Tiro
from mapa import Mapa
from colisao import Colisao
import pygame
import random

class General_Config():
    mapa = Mapa()
    jogador = Navezinha()
    inimigos =  pygame.sprite.Group()
    tiros = pygame.sprite.Group()
    colisoes = []
    tamanho_tela = {
        'x': 1260,
        'y': 920
    }
    jogo_rodando = True
    seed = random.random()

    def __init__(self):
        print(self.seed)
        pass

    def stopGame(self):
        self.jogo_rodando = False

    def addEnemy(self, x, y):
        self.inimigos.add(Inimigo(x, y))

    def addTiro(self, x, y):
        self.tiros.add(Tiro(x, y))

    def checaColisao(self):
        self.checaColisaoNaveInimigo()
        self.checaColisaoNaveTiro()

    def checaColisaoNaveInimigo(self):
        for inimigo in self.inimigos:
            if Colisao.checa_colisao(self.jogador, inimigo):
                self.jogador.perdeVida()
                inimigo.perdeVida()
    
    def checaColisaoNaveTiro(self):
        for inimigo in self.inimigos:
            for tiro in self.tiros:
                if Colisao.checa_colisao(tiro, inimigo):
                    inimigo.perdeVida()
                    tiro.na_tela = False

    def doRandomIngameEvent(self):
        escolheEventos = random.randint(0, 3)
        if escolheEventos == 1 :
            self.geraInimigo()

    def geraInimigo(self):
        x = random.randint(50, 1200)
        y = random.randint(20, 200)
        inimigo = Inimigo(x ,y)
        self.inimigos.add(inimigo)

    def deletaEntidadesMortas(self):
        self.deletaInimigosMortos()
        self.deletaTirosForaDaTela()
        
    def deletaInimigosMortos(self):
        inimigos_com_vida = [inimigo for inimigo in self.inimigos if inimigo.vida > 0]
        self.inimigos.empty()
        for inimigo in inimigos_com_vida:
            self.inimigos.add(inimigo)

    def deletaTirosForaDaTela(self):
        lista_tiros = [tiro for tiro in self.tiros if tiro.na_tela]
        self.tiros.empty()
        for tiro in lista_tiros:
            self.tiros.add(tiro)

    
