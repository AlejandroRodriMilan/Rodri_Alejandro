import pygame,sys,Tablero, piezas
from piezas import Piezas

pygame.init()
screen = pygame.display.set_mode((400,800))
clock = pygame.time.Clock()
running = True

fcount = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tablero = Tablero.init()
    Tablero.draw(tablero, screen)

    nueva_pieza = Piezas()
    
    if nueva_pieza.cai_posible(tablero):
        tablero = caída(tablero)
    else:
        nueva_pieza = crear_pieza()
        nueva_pieza = draw(tablero)
    


    if fcount % 60 == 0:
        caida pieza

    

    





    fcount += 1
    clock.tick(60)
pygame.quit()
sys.exit()