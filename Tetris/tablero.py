import pygame

def tablero_init():
    tablero = []
    for fila in range(20):
        for columna in range(10):
            tablero[fila][columna] = "black"
    return tablero


def draw(tablero, screen):
    for fila in range(20):
        for columna in range(10):
            x = columnas*40
            y = fila*40
            cuadrado = pygame.Rect(x, y, 40, 40)
            pygame.draw.rect(screen,tablero[fila][columna], cuadrado)

