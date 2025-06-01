# Búsqueda binaria recursiva
def buscar(lista, inicio, fin, objetivo):
    # Si ya no hay más elementos para revisar
    if inicio > fin:
        return -1
    
    # Calcula el punto medio
    medio = (inicio + fin) // 2
    
    # Si encontramos el objetivo
    if lista[medio] == objetivo:
        return medio
    
    # Si el objetivo está en la mitad derecha
    elif lista[medio] < objetivo:
        return buscar(lista, medio + 1, fin, objetivo)
    
    # Si el objetivo está en la mitad izquierda
    else:
        return buscar(lista, inicio, medio - 1, objetivo)



    
# Pedir lista ordenada
entrada = input("Ingresa números separados por comas")
numeros = [int(x) for x in entrada.split(",")]
numeros.sort()
    
# Pedir número a buscar
objetivo = int(input("qué número quieres buscar?"))
    
 # Llamar a la función de búsqueda
posicion = buscar(numeros, 0, len(numeros)-1, objetivo)
    
# Mostrar resultados
if posicion == -1:
        print(f"El número {objetivo} no está en la lista")
else:
        print(f"Encontrado! Posición: {posicion}")
        print(f"Lista: {numeros}")
        print(f"En la posición {posicion} está el número {numeros[posicion]}")