def cambio_greedy(monto, monedas):
    # Ordenamos las monedas de mayor a menor para aplicar la estrategia voraz
    monedas = sorted(monedas, reverse=True)

    # Creamos un diccionario para guardar cuántas monedas usamos de cada tipo
    resultado = {}

    # Recorremos las monedas y usamos tantas como podamos de cada una
    for moneda in monedas:
        if monto >= moneda:
            cantidad = (
                monto // moneda
            )  # Cuántas monedas de este valor caben en el monto
            monto -= cantidad * moneda  # Restamos ese valor del monto total
            resultado[moneda] = cantidad  # Guardamos cuántas usamos

    # Si no pudimos devolver el monto exacto con las monedas disponibles
    if monto != 0:
        print("No se pudo dar el cambio exacto con las monedas dadas.")
    else:
        # Si el cambio fue exitoso, mostramos el desglose
        print("Cambio óptimo encontrado (estrategia voraz):")
        for m, c in resultado.items():
            print(f"{c} moneda(s) de {m}")

    return resultado


# Pedimos al usuario que ingrese las monedas disponibles, separadas por comas
monedas = input(
    "Ingresa las denominaciones de las monedas separadas por comas (ej. 1000,500,100): "
)
# Convertimos esa cadena en una lista de enteros
monedas = [int(m.strip()) for m in monedas.split(",")]

# Pedimos al usuario el monto a devolver
monto = int(input("Ingresa el monto total a devolver: "))

# --- Llamada a la función para calcular el cambio ---
cambio_greedy(monto, monedas)
