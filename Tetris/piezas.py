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
    ],

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
        self.tipo = self.crear_pieza()
        self.forma = FORMAS[tipo]
        self.color = COLORES[tipo]
        self.pos = [0,4]

    def crear_pieza(self):
        tipo = random.choice(list(FORMAS.keys()))
        return tipo

    def draw(self, tablero):
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[self.pos[0] + i][self.pos[1] + j] = self.color

    def caída(self, tablero):
        if self.cai_posible(tablero):
            self.pos[0] += 1

    def rot_posible(self, tablero):
        forma = self.rotar_derecha(self.forma)

        for i in range(len(forma)):
            for j in range(len(forma[0])):
                if forma[i][j] == 1:
                    fila = self.pos[0] + i
                    columna = self.pos[1] + j

                    if fila < 0 or fila >= len(tablero):
                        return False

                    if columna < 0 or columna >= len(tablero[0]):
                        return False

                    if tablero[fila][columna] != "black":
                        return False

        return True


    def cai_posible(self, tablero):
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    fila = self.pos[0] + i + 1
                    columna = self.pos[1] + j

                    if fila >= len(tablero):
                        return False

                    if tablero[fila][columna] != "black":
                        return False

        return True


    def rotar_derecha(self, matriz):
        return [
            list(fila)
            for fila in zip(*matriz[::-1])
        ]



                        
                    





