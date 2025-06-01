def fibonacci_iterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1  # Inicializamos F(0) y F(1)
    for _ in range(2, n + 1):
        c = a + b  # Calculamos el siguiente número
        a, b = b, c  # Actualizamos los valores anteriores
    
    return b

# Se ingresa el numeropara calcular fibonacci
n = int(input("Ingrese un número para calcular Fibonacci: "))
print(f"F({n}) = {fibonacci_iterativo(n)}")