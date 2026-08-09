import pygame
import sys
import Tablero
from piezas import Piezas


pygame.init()


screen = pygame.display.set_mode((400,800))
clock = pygame.time.Clock()
fcount = 0
nueva_pieza = Piezas()

running = True
while running:
    tablero = Tablero.init()
    Tablero.draw(tablero, screen)

    
    if nueva_pieza.cai_posible(tablero):
        tablero = caída(tablero)
    else:
        nueva_pieza = crear_pieza()
        nueva_pieza = draw(tablero)
    
    
    fcount += 1
    if fcount % 30 == 0:
        caida pieza
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
sys.exit()