# Función para realizar la búsqueda por profundidad iterativa
def buscar_profundidad_iterativa(matriz, objetivo, profundidad_maxima):
    # Inicializa la pila con la raíz del árbol de búsqueda
    pila = [(matriz, [])]

    # Itera hasta que se encuentre el objetivo o se alcance la profundidad máxima
    while pila:
        # Extrae el último elemento de la pila (es decir, el último nodo visitado)
        nodo, ruta = pila.pop()

        # Comprueba si el nodo actual es el objetivo
        if nodo == objetivo:
            return ruta + [nodo]

        # Comprueba si se ha alcanzado la profundidad máxima
        if len(ruta) == profundidad_maxima:
            continue

        # Genera los hijos del nodo actual
        hijos = generar_hijos(nodo)

        # Añade los hijos a la pila
        for hijo in hijos:
            pila.append((hijo, ruta + [nodo]))

    # Si no se encuentra el objetivo, devuelve None
    return None

# Función para generar los hijos de un nodo dado (es decir, las matrices vecinas)
def generar_hijos(matriz):
    hijos = []
    # Genera los hijos cambiando un elemento de la matriz por un número diferente
    for i in range(5):
        for j in range(5):
            for n in range(1, 10):
                if n != matriz[i][j]:
                    hijo = matriz.copy()
                    hijo[i][j] = n
                    hijos.append(hijo)
    return hijos