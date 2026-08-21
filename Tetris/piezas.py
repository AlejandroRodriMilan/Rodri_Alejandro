import pygame, random, Tablero

FORMAS = {
    "I": [
        [1],
        [1],
        [1],
        [1]
    ],
    "O": [
        [1, 1],
        [1, 1],
    ],
    "T": [
        [0, 1, 0],
        [1, 1, 1],
    ],
    "L": [
        [0, 0, 1],
        [1, 1, 1],
    ],
    "J": [
        [1, 0, 0],
        [1, 1, 1],
    ],
    "S": [
        [0, 1, 1],
        [1, 1, 0],
    ],
    "Z": [
        [1, 1, 0],
        [0, 1, 1],
    ],
}
COLORES = {
    "I": (0, 255, 255),
    "O": (255, 255, 0),
    "T": (128, 0, 128),
    "L": (255, 165, 0),
    "J": (0, 0, 255),
    "S": (0, 255, 0),
    "Z": (255, 0, 0)
}


class Piezas:
    def __init__(self):
        self.tipo = random.choice(list(FORMAS))
        self.forma = FORMAS[self.tipo]
        self.color = COLORES[self.tipo]
        self.pos = [0, 4]

    def draw(self, tablero):
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[self.pos[0] + i][self.pos[1] + j] = self.color

    def caida(self, tablero):
        self.borrar(tablero)
        self.pos[0] += 1

    def borrar(self, tablero):
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[self.pos[0] + i][self.pos[1] + j] = "black"

    def mover_posible(self, tablero, check_fila, check_columna):
        self.borrar(tablero)
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    fila = self.pos[0] + i + check_fila
                    columna = self.pos[1] + j + check_columna
                    if fila >= len(tablero) or columna >= len(tablero[0]) or columna < 0 or tablero[fila][columna] != "black":
                        return False
        return True


    def mover(self, tablero, cambio_fila, cambio_columna):
        self.borrar(tablero)
        self.pos[0] += cambio_fila
        self.pos[1] += cambio_columna
        
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

    def rotar(self, tablero):
        self.borrar(tablero)

        forma_rotada = self.rotar_derecha(self.forma)

        if self.rot_posible(tablero):
            self.forma = forma_rotada

        self.draw(tablero)

    def rotar_derecha(self, matriz):
        return [
            list(fila)
            for fila in zip(*matriz[::-1])
        ]
