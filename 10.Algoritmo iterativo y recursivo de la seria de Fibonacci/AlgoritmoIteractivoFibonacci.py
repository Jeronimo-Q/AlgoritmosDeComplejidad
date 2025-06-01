def fibonacci_iterativo(n):
    # Para los dos primeros casos, devolvemos directamente el valor
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Empezamos desde 0 y 1, y vamos sumando los anteriores
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursivo(n):
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Llamamos a la función a sí misma sumando los dos anteriores
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

if __name__ == '__main__':
    n = int(input("Ingresa la posición n de la serie de Fibonacci: "))

    print("\nMétodo iterativo:")
    print(f"Fibonacci({n}) = {fibonacci_iterativo(n)}")

    print("\nMétodo recursivo:")
    print(f"Fibonacci({n}) = {fibonacci_recursivo(n)}")
