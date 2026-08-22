import pygame
import sys
import Tablero
from piezas import Piezas

pygame.init()

pygame.mixer.music.load("Tetris/tetris-gameboy.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Tetris")

font = pygame.font.SysFont("consolas", 48)
small_font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
fcount = 0
tablero = Tablero.init()
possible_restart = False

game_over = False

speed = 30
linecount = 0
running = True
pieza_nueva = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and pieza:
                pieza.rotar(tablero)

            elif event.key == pygame.K_RIGHT and pieza.mover_posible(tablero, 0, 1) and pieza:
                pieza.mover(tablero, 0, 1)

            elif event.key == pygame.K_LEFT and pieza.mover_posible(tablero, 0, -1) and pieza:
                pieza.mover(tablero, 0, -1)

            elif event.key == pygame.K_DOWN and pieza.mover_posible(tablero, 1, 0) and pieza:
                pieza.mover(tablero, 1, 0)
            elif event.key == pygame.K_r and possible_restart:
                Tablero.reset(tablero)


    if not game_over:
        if pieza_nueva:
            pieza = Piezas()
            pieza_nueva = False
            if not pieza.mover_posible(tablero, 0, 0):
                running = False

        fcount += 1

        if fcount % speed == 0:
            if pieza.mover_posible(tablero, 1, 0):
                pieza.caida(tablero)
            else:
                pieza.draw(tablero)
                speed, linecount = Tablero.clear_line(tablero, speed, linecount)
                pieza_nueva = True
                fcount = 0

        if not pieza_nueva:
            pieza.draw(tablero)   # <-- always redraw current state before rendering

        Tablero.draw(tablero, screen)


    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()