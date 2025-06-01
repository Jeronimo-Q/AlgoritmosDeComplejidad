def factorial_iterativo(n):
    if not isinstance(n, int) or n < 0:
        return "¡Error! Ingrese un entero no negativo."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplo con manejo de errores
try:
    n = int(input("Ingrese un número entero no negativo: "))
    print(f"{n}! = {factorial_iterativo(n)}")
except ValueError:
    print("¡Error! Ingrese un número válido.")