from queue import Queue

# Clase Nodo para almacenar información sobre cada estado en nuestro grafo
class Nodo:
    def __init__(self, x, y, costo, padre=None):
        self.x = x # columnas
        self.y = y # filas
        self.costo = costo
        self.padre = padre

# Función para obtener los vecinos de un nodo en la matriz
def obtener_vecinos(matriz, nodo):
    vecinos = []

    # Comprobar los vecinos a la izquierda, derecha, arriba y abajo del nodo
    if nodo.x > 0: # solo entra si tiene izquierda
        vecino_izq = Nodo(nodo.x - 1, nodo.y, nodo.costo + matriz[nodo.x - 1][nodo.y], nodo)
        vecinos.append(vecino_izq)
    if nodo.x < len(matriz) - 1:  # solo entra si tiene derecha
        vecino_der = Nodo(nodo.x + 1, nodo.y, nodo.costo + matriz[nodo.x + 1][nodo.y], nodo)
        vecinos.append(vecino_der)
    if nodo.y > 0:  # solo entra si tiene arriba
        vecino_arr = Nodo(nodo.x, nodo.y - 1, nodo.costo + matriz[nodo.x][nodo.y - 1], nodo)
        vecinos.append(vecino_arr)
    if nodo.y < len(matriz[0]) - 1:  # solo entra si tiene abajo
        vecino_abj = Nodo(nodo.x, nodo.y + 1, nodo.costo + matriz[nodo.x][nodo.y + 1], nodo)
        vecinos.append(vecino_abj)
    """ REVISAR.
    Para el caso de Gepetto NO hay que sumar su valor=5.
    Agregar condicion para solo sumar 1, y que finalice el codigo"""

    return vecinos

# Función para buscar el camino más corto utilizando la técnica de búsqueda amplitud
def busqueda_amplitud(matriz):
    # Crear una cola para almacenar los nodos que debemos visitar
    cola = Queue()

    # Crear un nodo para la posición inicial en la matriz
    nodo_inicial = Nodo(0, 0, matriz[0][0])
    """Se debe inicializar respecto al mapa. Esta es la ubicacion de Pinocchio"""

    # Agregar el nodo inicial a la cola de nodos por visitar
    cola.put(nodo_inicial)

    # Crear un conjunto para almacenar los nodos ya visitados
    visitados = set()

    # Mientras la cola no esté vacía, seguir visitando nodos
    while not cola.empty():
        # Obtener el siguiente nodo de la cola
        nodo_actual = cola.get()

        # Si el nodo actual es el objetivo, regresar el camino hasta él
        if nodo_actual.x == len(matriz) - 1 and nodo_actual.y == len(matriz[0]) - 1:
            camino = []
            while nodo_actual:
                camino.append((nodo_actual.x, nodo_actual.y))
                nodo_actual = nodo_actual.padre
            return list(reversed(camino))

        # Obtener los vecinos del nodo actual
        vecinos = obtener_vecinos(matriz, nodo_actual)

        # Añadir los vecinos a la cola de nodos por visitar si no han sido visitados ya
        for vecino in vecinos:
            if vecino not in visitados:
                cola.put(vecino)
                visitados.add(vecino)

    # Si no se encontró un camino hasta el objetivo, regresar None
    return None
