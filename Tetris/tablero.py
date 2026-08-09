import pygame

def init():
    tablero = []
    for i in range(20):
        fila = []
        for j in range(10):
            file.append("black")
        tablero.append(fila)
    return tablero


def draw(tablero, screen):
    for fila in range(20):
        for columna in range(10):
            x = columna*40
            y = fila*40
            cuadrado = pygame.Rect(x, y, 40, 40)
            pygame.draw.rect(screen,tablero[fila][columna], cuadrado)

