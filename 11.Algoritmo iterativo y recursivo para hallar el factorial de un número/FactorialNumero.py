def factorial_iterativo(n):
    #Se verifica que el numero sea mayor 
    if not isinstance(n, int) or n < 0:
        return "¡Error! Ingrese un entero no negativo."
    #Se marca un numero como el valor minimo=1
    resultado = 1
    #Se aplica un for para multiplicar todos los números desde 1 hasta el número que se ingreso
    for i in range(1, n + 1):
        #Se multiplican todos los números
        resultado *= i
        #Se muestra el resultado
    return resultado


def factorialRecursivo(n):
    #Si el n es diferente de 1 se multiplica el numero ingresado y usando recursicidad de hace hasta que sea igual que uno
    if n != 1:
        return n * factorialRecursivo(n - 1)
    #Una vez que el número es 1 , se retorna el uno para no afectar la multiplicacion y retornar la respuesta
    else:
        return 1

#Se hace ejemplo de uso
try:
    n = int(input("Ingrese un número entero no negativo: "))
    print(f"{n}! = {factorial_iterativo(n)}")
    print(factorialRecursivo(n))
except ValueError:
    print("¡Error! Ingrese un número válido.")
