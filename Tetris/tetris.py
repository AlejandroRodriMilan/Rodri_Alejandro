import pygame
import sys
import Tablero
from piezas import Piezas


pygame.init()


screen = pygame.display.set_mode((400,800))
pygame.display.set_caption("Tetris")


clock = pygame.time.Clock()
fcount = 0
tablero = Tablero.init()

running = True
pieza_nueva = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if pieza_nueva:
        pieza = Piezas()
        pieza_nueva = False


    fcount += 1

    if fcount % 30 == 0:
        if pieza.cai_posible(tablero):
            pieza.caida(tablero)
        else:
            pieza_nueva = True
    
    
    Tablero.draw(tablero, screen)
    pieza.draw(tablero)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()