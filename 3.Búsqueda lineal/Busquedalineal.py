#Se define una función que recibe como parametros la lista y el valor a buscar
def busquedaLineal(lista, valor):
    #se declara un ciclo for para recorrer uno a uno la lista
    for i in range(len(lista)):
        #una vez se encuentra el valor , comparando la losta en una posicion i con el valor que queremos se retorna la posiscion del elemento 
        if lista[i] == valor:
            return i
    #Sino se encuentra el elemento se retorna un None 
    return None

#Se ingresa los valores de la lista
lista = input("ingresa los valores de la lista separados por coma")
#se convierte en una lista todos los elementos que tienen una coma
lista = lista.split(",")
#se ingresa el valor a buscar
valor = input("ingresa el número a buscar")

#se llama la función
resultado = busquedaLineal(lista, valor)

#se analizan los resiltados de la funcion
if resultado != None:
    print("elemento encontrado en la posición", resultado)
else:
    print("el elemento no estaba en la lista")
