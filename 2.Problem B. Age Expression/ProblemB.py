# Problema: ¿Se puede formar un número "dro" exacto sumando múltiplos de "konari" y "analisa"?
# Entrada: Tres enteros: dro, konari y analisa
# Objetivo: Verificar si existen enteros positivos a y k tales que:
#           analisa * a + konari * k == dro

# Función que resuelve el problema
def solucion(dro, konari, analisa):
    # Recorremos todas las posibles cantidades de veces que se puede usar analisa (de 1 hasta dro//analisa)
    for a in range(1, dro // analisa + 1):
        # Recorremos todas las posibles cantidades de veces que se puede usar konari (de 1 hasta dro//konari)
        for k in range(1, dro // konari + 1):
            # Si la suma exacta de estos productos da dro, entonces existe una solución
            if analisa * a + konari * k == dro:
                return 1  # Retornamos 1 si encontramos una combinación válida
    # Si terminan los ciclos y no se encuentra ninguna combinación, no hay solución
    return 0

# Bloque principal: aquí se ejecuta el programa
if __name__ == "__main__":
    # Leemos los tres valores de entrada
    dro, konari, analisa = map(int, input().split())
    # Llamamos a la función para saber si existe una combinación válida
    if solucion(dro, konari, analisa):
        print("si")  # Si hay solución, se imprime YES
    else:
        print("no")   # Si no hay solución, se imprime NO
