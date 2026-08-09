import pygame,sys
from tablero import Tablero
pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
running = True
tablero = Tablero()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tablero = tablero_init()
    tablero.draw(screen)
    clock.tick(60)
pygame.quit()
sys.exit()