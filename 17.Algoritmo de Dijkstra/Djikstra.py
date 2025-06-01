import heapq

def dijkstra(grafo, inicio):
    #Inicialización de distancias: infinito para todos los nodos excepto el origen
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0  # La distancia del nodo inicial a sí mismo es 0

    # Cola de prioridad (min-heap) para procesar nodos en orden de distancia ascendente
    cola_prioridad = [(0, inicio)]  # (distancia, nodo)

    while cola_prioridad:
        #Extraemos el nodo con la menor distancia actual
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        #Si ya registramos una distancia mejor, ignoramos este nodo
        if distancia_actual > distancias[nodo_actual]:
            continue

        #Explorar vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            distancia_nueva = distancia_actual + peso

            # Si encontramos un camino más corto, actualizamos la distancia
            if distancia_nueva < distancias[vecino]:
                distancias[vecino] = distancia_nueva
                heapq.heappush(cola_prioridad, (distancia_nueva, vecino))

    return distancias  #Devuelve las distancias mínimas desde el inicio

# Definición del grafo 
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Nodo de inicio y ejecución del algoritmo
nodo_inicio = 'A'
distancias = dijkstra(grafo, nodo_inicio)


print("Distancias más cortas desde el nodo", nodo_inicio + ":")
for nodo, distancia in distancias.items():
    print(f"{nodo}: {distancia}")