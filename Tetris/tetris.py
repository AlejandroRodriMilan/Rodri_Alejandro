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
nueva_pieza = Piezas()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fcount += 1
    if fcount % 30 == 0:
        #caida pieza
    
    
    if nueva_pieza.cai_posible(tablero):
        tablero = caída(tablero)
    else:
        nueva_pieza = crear_pieza()
        nueva_pieza = draw(tablero)
        nueva_pieza = Piezas()
    
    
    Tablero.draw(tablero, screen)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()