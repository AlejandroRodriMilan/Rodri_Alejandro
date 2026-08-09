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
        for i in range(20):
            for j in range(10):
                pygame.draw.rect(screen,self.tablero[i][j], 40*i, 40*j, 40, 40)

