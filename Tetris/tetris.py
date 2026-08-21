import pygame
import sys
import Tablero
from piezas import Piezas

pygame.init()

screen = pygame.display.set_mode((400, 800))
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if pieza.rot_posible(tablero):
                    pieza.rotar(tablero)

            elif event.key == pygame.K_RIGHT and pieza.mover_posible(tablero, 0, 1):
                pieza.mover(tablero, 0, 1)

            elif event.key == pygame.K_LEFT and pieza.mover_posible(tablero, 0, -1):
                pieza.mover(tablero, 0, -1)

            elif event.key == pygame.K_DOWN and pieza.mover_posible(tablero, 1, 0):
                pieza.mover(tablero, 1, 0)


    if pieza_nueva:
        pieza = Piezas()
        pieza_nueva = False

    fcount += 1

    if fcount % 30 == 0:
        if pieza.mover_posible(tablero, 1, 0):
            pieza.caida(tablero)
            Tablero.clear_line(tablero)
        else:
            pieza_nueva = True

    pieza.draw(tablero)
    Tablero.draw(tablero, screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()