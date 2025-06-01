# Ordenamiento de números grandes representados como cadenas
# Comparación: Bubble Sort manual vs sorted() con lambda


# Opción 1: Implementación manual usando Bubble Sort
def bigSortingManual(unsorted):
    n = len(unsorted)

    # Bubble Sort: Recorre múltiples veces la lista y compara elementos adyacentes
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara primero por longitud (número de dígitos)
            # Si las longitudes son iguales, compara lexicográficamente
            if len(unsorted[j]) > len(unsorted[j + 1]) or \
               (len(unsorted[j]) == len(unsorted[j + 1]) and unsorted[j] > unsorted[j + 1]):
                # Intercambia los elementos si están en el orden incorrecto
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
    
    return unsorted

#DESVENTAJA:
#Complejidad O(n²), muy lento cuando hay muchos elementos.
#Solo útil para aprender cómo funcionan los algoritmos básicos de ordenamiento.


#Opción 2: Versión más eficiente usando sorted() con clave personalizada
def bigSortingPythonic(unsorted):
    #Usa la función built-in sorted() de Python con una lambda que ordena por:
    #longitud del número (menos dígitos va primero)
    #valor lexicográfico si la longitud es igual
    listaOrdenada = sorted(unsorted, key=lambda x: (len(x), x))
    return listaOrdenada

#VENTAJAS:
#Mucho más rápido: Complejidad O(n log n)
#Más legible, más conciso y más pythonic
#Recomendado para problemas reales y listas grandes