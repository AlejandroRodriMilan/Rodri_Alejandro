import pygame

class Tablero:
    tablero = []
    for i in range(20):
        for j in range(10):
            tablero[i][j] = "black"
    def update ()

    def draw(screen):
        for i in range(20):
            for j in range(10):
                pygame.draw.rect(screen,tablero[i][j], 40*i, 40*j, 40, 40)

