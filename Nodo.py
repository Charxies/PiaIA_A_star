class Nodo():
    def __init__(self, padre=None, posicion=None):
        self.padre = padre
        self.posicion = posicion
        #distancia del nodo inicial al actual
        self.peso = 0
        #heuristica
        self.heuristico = 0
        #costo total
        self.final = 0
    def __eq__(self, other):
        return self.posicion == other.posicion
