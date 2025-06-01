def knapsack(valores, pesos, capacidad):
    n = len(valores)  # Número total de objetos
    # Creo una tabla (matriz) con filas = objetos + 1 y columnas = capacidad + 1
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
    # Recorro cada objeto (de 1 a n)
    for i in range(1, n + 1):
        # Recorro cada capacidad posible (de 1 hasta la capacidad total)
        for w in range(1, capacidad + 1):
            if pesos[i-1] <= w:
                # Elijo entre no tomar el objeto actual o tomarlo (y sumarle su valor al mejor valor anterior)
                dp[i][w] = max(dp[i-1][w], valores[i-1] + dp[i-1][w - pesos[i-1]])
            else:
                # No cabe en la mochila, así que heredo el valor de arriba (sin usar este objeto)
                dp[i][w] = dp[i-1][w]
    # Al final, el valor óptimo está en la esquina inferior derecha de la matriz
    return dp[n][capacidad]
