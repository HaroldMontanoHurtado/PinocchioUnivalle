from queue import Queue

class Nodo:
    def __init__(self, x, y, costo, padre=None):
        self.x = x
        self.y = y
        self.costo = costo
        self.padre = padre

def buscar_camino(matriz, inicio, fin):
    # Inicializar la cola con el nodo inicial
    cola = Queue()
    nodo_inicial = Nodo(inicio[0], inicio[1], matriz[inicio[0]][inicio[1]])
    cola.put(nodo_inicial)
    
    # Inicializar el diccionario de nodos visitados
    visitados = {}
    visitados[inicio] = nodo_inicial
    
    while not cola.empty():
        # Obtener el siguiente nodo de la cola
        nodo_actual = cola.get()
        
        # Comprobar si es el nodo final
        if (nodo_actual.x, nodo_actual.y) == fin:
            # Reconstruir el camino desde el nodo final hasta el inicio
            camino = []
            while nodo_actual:
                camino.append((nodo_actual.x, nodo_actual.y))
                nodo_actual = nodo_actual.padre
            camino.reverse()
            return camino
        
        # Obtener los vecinos del nodo actual
        vecinos = obtener_vecinos(matriz, nodo_actual)
        
        # Añadir los vecinos a la cola y al diccionario de nodos visitados
        for vecino in vecinos:
            if (vecino.x, vecino.y) not in visitados:
                cola.put(vecino)
                visitados[(vecino.x, vecino.y)] = vecino
    
    # No se encontró un camino
    return None

def obtener_vecinos(matriz, nodo):
    vecinos = []

    # Comprobar los vecinos a la izquierda, derecha, arriba y abajo del nodo
    if nodo.x > 0:
        vecino_izq = Nodo(nodo.x - 1, nodo.y, nodo.costo + matriz[nodo.x - 1][nodo.y], nodo)
        vecinos.append(vecino_izq)
    if nodo.x < len(matriz) - 1:
        vecino_der = Nodo(nodo.x + 1, nodo.y, nodo.costo + matriz[nodo.x + 1][nodo.y], nodo)
        vecinos.append(vecino_der)
    if nodo.y > 0:
        vecino_arr = Nodo(nodo.x, nodo.y - 1, nodo.costo + matriz[nodo.x][nodo.y - 1], nodo)
        vecinos.append(vecino_arr)
    if nodo.y < len(matriz[0]) - 1:
        vecino_abj = Nodo(nodo.x, nodo.y + 1, nodo.costo + matriz[nodo.x][nodo.y + 1], nodo)
        vecinos.append(vecino_abj) 

    return vecinos

def option_BFS():
    print('Seleccionó el button de la clase BFS')