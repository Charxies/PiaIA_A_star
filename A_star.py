from Nodo import Nodo
import time

start = time.process_time()
def encontrarCamino(terreno, principio, fin):
    nodo_principio = Nodo(None, principio)
    nodo_principio.peso = nodo_principio.heuristico = nodo_principio.final = 0
    nodo_final = Nodo(None, fin)
    nodo_final.peso = nodo_final.heuristico = nodo_final.final = 0
    lista_nodos = []
    lista_nodos_cerrados = []

    # nodo principio
    lista_nodos.append(nodo_principio)
    # Loop hasta terminar
    while len(lista_nodos) > 0:
        # obtener nodo
        nodo_actual = lista_nodos[0]
        indice_actual = 0
        for indice, nod in enumerate(lista_nodos):
            if nod.final < nodo_actual.final:
                nodo_actual = nod
                indice_actual = indice
        # quitar nodo de lista abierta a nodo cerrado
        lista_nodos.pop(indice_actual)
        lista_nodos_cerrados.append(nodo_actual)
        # encontro fin
        if nodo_actual == nodo_final:
            camino = []
            actual = nodo_actual
            while actual is not None:
                camino.append(actual.posicion)
                actual = actual.padre
            return camino[::-1]  # Return camino invertido
        # Generar hijos
        hijos = []
        for nueva_pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # nodos adjacentes
            # obtener posicion
            posicion_nodo = (nodo_actual.posicion[0] + nueva_pos[0], nodo_actual.posicion[1] + nueva_pos[1])
            # nodo en rango?
            if posicion_nodo[0] > (len(terreno) - 1) or posicion_nodo[0] < 0 or posicion_nodo[1] > (
                    len(terreno[len(terreno) - 1]) - 1) or posicion_nodo[1] < 0:
                continue
            # terreno estorba
            if terreno[posicion_nodo[0]][posicion_nodo[1]] != 0:
                continue

            # Crear nuevo nodo
            nuevo_nodo = Nodo(nodo_actual, posicion_nodo)
            # Append el nodo a la lista hijos
            hijos.append(nuevo_nodo)
        # Loop por hijos
        for hijo in hijos:
            # hijo en lista_nodos_cerrados
            for hijo_cerrado in lista_nodos_cerrados:
                if hijo == hijo_cerrado:
                    continue
            # Crear valores para meter en nodo
            hijo.peso = nodo_actual.peso + 1
            #teoream pitagoras para encontrar distancia final al nodo actual heuristico
            hijo.heuristico = ((hijo.posicion[0] - nodo_final.posicion[0]) ** 2) + (
                    (hijo.posicion[1] - nodo_final.posicion[1]) ** 2)
            #distancia total recorrida
            hijo.final = hijo.peso + hijo.heuristico
            # hijo en la lista de nodos buenos
            for nodo_abierto in lista_nodos:
                if hijo == nodo_abierto and hijo.peso > nodo_abierto.peso:
                    continue
            # Anadir hijo a la lista
            lista_nodos.append(hijo)


def main():
    #    1  2  3  4  5  6  7  8  9  10
    terreno = [
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
    # inicializamos las variables

    principio = (0, 0)
    fin = (6,0)
    camino = encontrarCamino(terreno, principio, fin)
    print(camino)
    print(time.process_time() )

if __name__ == '__main__':
    main()
