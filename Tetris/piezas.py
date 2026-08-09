import pygame, random, Tablero


FORMAS = {
    "I": [
        [1, 0], 
        [1, 0], 
        [1, 0], 
        [1, 0]
    ],

    "O": [
        [1, 1],
        [1, 1],
        [0, 0],
        [0, 0]
    ],

    "T": [
        [1, 0],
        [1, 1],
        [1, 0],
        [0, 0]
    ]

    "L": [
        [1, 0],
        [1, 0],
        [1, 1],
        [0, 0]
    ],

    "J": [
        [0, 1],
        [0, 1],
        [1, 1],
        [0, 0]
    ],

    "S": [
        [1, 0],
        [1, 1],
        [0, 1],
        [0, 0]
    ],

    "Z": [
        [0, 1],
        [1, 1],
        [1, 0],
        [0, 0]
    ]
}

COLORES = {
    "I": "cyan",
    "O": "yellow",
    "T": "purple",
    "L": "orange",
    "J": "blue",
    "S": "green",
    "Z": "red"
}

class Piezas:
    def __init__(self):
        tipo = crear_pieza
        self.forma = FORMA[tipo]
        self.color = COLORES[tipo]

    def crear_pieza(self):
        tipo = random_choice(list.(FORMAS.keys()))
        return Pieza(tipo)

    def draw(self,tablero):
        for i in range(4):
            for j in range(10):
                if j==4 or j==5:
                    if FORMAS[self.tipo][i][j-4] == 1:
                        talero[i][j] = COLORES[self.tipo]

    def caída(self, tablero, pos):

    def rotar_derecha(matriz):
    return [
        list(fila)
        for fila in zip(*matriz[::-1])
    ]



                        
                    





