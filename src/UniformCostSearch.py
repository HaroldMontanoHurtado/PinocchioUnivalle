import heapq

# Definir una clase Nodo para representar cada estado en la matriz
class Nodo:
    def __init__(self, x, y, costo, padre):
        self.x = x
        self.y = y
        self.costo = costo
        self.padre = padre

    # Método que permite comparar nodos para ordenarlos en la cola de prioridad
    def __lt__(self, otro):
        return self.costo < otro.costo

    # Método que devuelve una representación en cadena del nodo
    def __str__(self):
        return f"({self.x}, {self.y}): {self.costo}"

# Función que realiza la búsqueda por costo uniforme
def busqueda_costo_uniforme(matriz, inicio, fin):
    # Crear una cola de prioridad vacía y agregar el nodo de inicio
    cola_prioridad = []
    heapq.heappush(cola_prioridad, inicio)

    # Crear un conjunto vacío para almacenar los nodos visitados
    visitados = set()

    # Bucle principal de búsqueda
    while cola_prioridad:
        # Sacar el nodo de menor costo de la cola de prioridad
        nodo_actual = heapq.heappop(cola_prioridad)

        # Comprobar si el nodo actual es el nodo final
        if nodo_actual.x == fin[0] and nodo_actual.y == fin[1]:
            # Si es así, construir el camino y devolverlo
            camino = []
            while nodo_actual:
                camino.append((nodo_actual.x, nodo_actual.y))
                nodo_actual = nodo_actual.padre
            camino.reverse()
            return camino

        # Si no es el nodo final, agregarlo al conjunto de nodos visitados
        visitados.add((nodo_actual.x, nodo_actual.y))

        # Expandir el nodo actual y agregar sus vecinos a la cola de prioridad
        for vecino in obtener_vecinos(matriz, nodo_actual):
            if (vecino.x, vecino.y) not in visitados:
                heapq.heappush(cola_prioridad, vecino)

    # Si se llega aquí, significa que no se encontró un camino
    return None

# Función que devuelve una lista de los vecinos de un nodo en la matriz
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

def leer_matriz_desde_archivo(nombre_archivo):
    matriz = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = [int(x) for x in linea.split()]
        matriz.append(fila)
    return matriz

def option_UCS():
    print('Seleccionó el button de la clase UCS')