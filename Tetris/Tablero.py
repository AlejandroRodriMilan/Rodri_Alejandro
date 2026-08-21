import pygame

def init():
    tablero = []
    for i in range(20):
        fila = []
        for j in range(10):
            fila.append("black")
        tablero.append(fila)
    return tablero


def draw(tablero, screen):
    for fila in range(20):
        for columna in range(10):
            x = columna*40
            y = fila*40
            cuadrado = pygame.Rect(x, y, 40, 40)
            pygame.draw.rect(screen,tablero[fila][columna], cuadrado)
            pygame.draw.rect(screen,(30,30,30),cuadrado,1)  

def clear_line(tablero):
    for i in range(len(tablero)-1,-1,-1):
        if "black" not in tablero[i]:
            tablero.pop(i)
            tablero.insert(0,["black"] *10)
