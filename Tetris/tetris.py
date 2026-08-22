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

        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_SPACE:
                    Tablero.reset(tablero)
                    game_over = False
                    pieza_nueva = True
                    fcount = 0
                    linecount = 0
                    speed = 30
            else:
                if event.key == pygame.K_UP and pieza:
                    pieza.rotar(tablero)
                elif event.key == pygame.K_RIGHT and pieza and pieza.mover_posible(tablero, 0, 1):
                    pieza.mover(tablero, 0, 1)
                elif event.key == pygame.K_LEFT and pieza and pieza.mover_posible(tablero, 0, -1):
                    pieza.mover(tablero, 0, -1)
                elif event.key == pygame.K_DOWN and pieza and pieza.mover_posible(tablero, 1, 0):
                    pieza.mover(tablero, 1, 0)



    if not game_over:
        if pieza_nueva:
            pieza = Piezas()
            pieza_nueva = False
            if not pieza.mover_posible(tablero, 0, 0):
                game_over = True

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
            pieza.draw(tablero)
        
        Tablero.draw(tablero, screen)


    if game_over:
        pygame.draw.rect(screen,(30,30,30),(50,300,300,200))
        texto = font.render("GAME OVER", True, (255,0,0))
        screen.blit(texto, (75, 350))
        texto2 = small_font.render(f"Lines: {linecount}  Press SPACE", True, (200,200,200))
        screen.blit(texto2, (75, 410))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()