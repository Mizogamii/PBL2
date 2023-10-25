import pygame
from pygame.locals import *

from sys import exit

pygame.init()

largura = 640
altura = 480
x = largura / 2
y = altura / 2

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Jogo 2048")
relogio = pygame.time.Clock()


while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))

    """if y >= altura:
        y = 0
    y = y + 5"""

    """pygame.draw.circle(tela, (0,0,120), (300,260), 40)
    pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5)"""
    pygame.display.update()
    
 

