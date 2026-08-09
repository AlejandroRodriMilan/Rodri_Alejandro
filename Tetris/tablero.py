import pygame

class Tablero:
    def __init__ (self)
    self.filas = 20
    self.columnas = 10
    
    self.tablero = []
    for fila in range(self.filas):
        for columna in range(self.columnas):
            self.tablero[fila][columna] = "black"
    def update ()

    def draw(self, screen):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                x = columnas*40
                y = fila*40
                cuadrado = pygame.Rect(x, y, 40, 40)
                pygame.draw.rect(screen,self.tablero[fila][columna], cuadrado)

