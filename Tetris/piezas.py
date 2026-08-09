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
        self.forma = FORMAS[self.tipo]
        self.color = COLORES[self.tipo]
        self.pos = [0,4]

    def crear_pieza(self):
        tipo = random.choice(list(FORMAS.keys()))
        return tipo

    def draw(self, tablero):
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[self.pos[0] + i][self.pos[1] + j] = self.color

    def caida(self, tablero):
        self.borrar(tablero)

        self.pos[0] += 1

        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[self.pos[0] + i][self.pos[1] + j] = self.color

    def borrar(self, tablero):
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[self.pos[0] + i][self.pos[1] + j] = "black"

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
                    tablero[self.pos[0] + i][self.pos[1] + j] = "black"

        posible = True

        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:

                    fila = self.pos[0] + i + 1
                    columna = self.pos[1] + j

                    if fila >= len(tablero):
                        posible = False
                        break

                    if tablero[fila][columna] != "black":
                        posible = False
                        break

            if not posible:
                break

        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[self.pos[0] + i][self.pos[1] + j] = self.color

        return posible


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

    def der_posible(self,tablero):
        pos = self.pos
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[pos[0]+i][pos[1]+j] == "black"

        posible = True

        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:

                    fila = pos[0]+i
                    columna = pos[1]+j+1

                    if columna >= len(tablero[0]) or tablero[fila][columna] != "black":
                        posible = False
                        break

            if not posible: return False

        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[pos[0+1]][pos[1]+j] == self.color
        return True

    def izq_posible(self,tablero):
        pos = self.pos
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[pos[0]+i][pos[1]+j] == "black"
    
        posible = True
    
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
    
                    fila = pos[0]+i
                    columna = pos[1]+j-1
    
                    if columna >= len(tablero[0]) or tablero[fila][columna] != "black":
                        posible = False
                        break
    
            if not posible: 
                return False
                
    
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[pos[0+1]][pos[1]+j] == self.color
        return True

    def derecha(self,tablero):
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[self.pos[0] + i][self.pos[1] + j] = "black"
        
        self.pos[1] += 1
        
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[self.pos[0] + i][self.pos[1] + j] = self.color

    def izquierda(self,tablero):
        self.borrar(tablero)                
        self.pos[1] += 1
                
        for i in range(len(self.forma)):
            for j in range(len(self.forma[0])):
                if self.forma[i][j] == 1:
                    tablero[self.pos[0] + i][self.pos[1] + j] = self.color



                        
                    





