import pygame #importando bibliotecas
import os
import random

LARGURA = 500
ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load("Imagens/pipe.png"))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load("Imagens/base.png"))
IMAGEM_FUNDO = pygame.transform.scale2x(pygame.image.load("Imagens/bg.png"))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load("Imagens/bird1.png")),
    pygame.transform.scale2x(pygame.image.load("Imagens/bird2.png")),
    pygame.transform.scale2x(pygame.image.load("Imagens/bird3.png"))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont("Arial", 30, False,False)

class Passaro:
    IMAGENS = IMAGENS_PASSARO
    #animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 1
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMAGENS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        #calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo
        #restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento
        #angulo do passaro
        if deslocamento < 0 or self.y - (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
            else:
                if self.angulo > -90:
                    self.angulo -= self.VELOCIDADE_ROTACAO




class Cano:
    pass

class Chao:
    pass
