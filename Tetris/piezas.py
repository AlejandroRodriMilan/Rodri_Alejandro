FORMAS = {
    "I": [
        [1, 1, 1, 1]
    ],

    "O": [
        [1, 1],
        [1, 1]
    ],

    "T": [
        [0, 1, 0],
        [1, 1, 1]
    ],

    "L": [
        [1, 0],
        [1, 0],
        [1, 1]
    ],

    "J": [
        [0, 1],
        [0, 1],
        [1, 1]
    ],

    "S": [
        [0, 1, 1],
        [1, 1, 0]
    ],

    "Z": [
        [1, 1, 0],
        [0, 1, 1]
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

class piezas:
    def __init__(self, tipo):
        self.tipo = tipo
        self.formas = FORMAS[tipo]
        self.color = COLORES[tipo]

    def crear_pieza(self):


