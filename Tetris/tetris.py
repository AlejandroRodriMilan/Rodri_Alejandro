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
        pieza.draw(tablero)
        Tablero.draw(tablero,screen)
        pieza_nueva = False


    fcount += 1
    if fcount % 30 == 0:
        pieza.caida(tablero)
    
    Tablero.draw(tablero, screen)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()