import pygame,sys
import Tablero
from piezas import Piezas

pygame.init()

pygame.mixer.music.load("Tetris/tetris-gameboy.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Tetris")

font = pygame.font.Font("Tetris/PressStart2P-Regular.ttf", 40)
small_font = pygame.font.Font("Tetris/PressStart2P-Regular.ttf", 16)

clock = pygame.time.Clock()
fcount = 0
tablero = Tablero.init()
possible_restart = False

state = "home"

speed = 30
linecount = 0
running = True
pieza_nueva = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if state == "over" or state == "home":
                if event.key == pygame.K_SPACE:
                    Tablero.reset(tablero)
                    state = "game"
                    pieza_nueva = True
                    fcount = 0
                    linecount = 0
                    speed = 30
            elif state == "game":
                if event.key == pygame.K_UP and pieza:
                    pieza.rotar(tablero)
                elif event.key == pygame.K_RIGHT and pieza and pieza.mover_posible(tablero, 0, 1):
                    pieza.mover(tablero, 0, 1)
                elif event.key == pygame.K_LEFT and pieza and pieza.mover_posible(tablero, 0, -1):
                    pieza.mover(tablero, 0, -1)
                elif event.key == pygame.K_DOWN and pieza and pieza.mover_posible(tablero, 1, 0):
                    pieza.mover(tablero, 1, 0)

    if state == "home":
        texto = font.render("TETRIS", True, (255,0,0))
        screen.blit(texto, (80, 350))
        texto2 = small_font.render("Press SPACE to Start",True,(100,100,100))
        screen.blit(texto2,(45,450))


    if state == "game":
        if pieza_nueva:
            pieza = Piezas()
            pieza_nueva = False
            if not pieza.mover_posible(tablero, 0, 0):
                state = "over"

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


    if state == "over":
        pygame.draw.rect(screen,(30,30,30),(10,300,380,200))
        texto = font.render("GAME OVER", True, (255,0,0))
        screen.blit(texto, (25, 350))
        texto2 = small_font.render(f"Lines: {linecount}", True, (200,200,200))
        screen.blit(texto2, (30, 410))
        texto3 = small_font.render(f"Press SPACE", True, (200,200,200))
        screen.blit(texto3, (100, 450))


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()