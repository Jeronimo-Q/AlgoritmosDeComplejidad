def superDigit(n, k):
    ##Se convierten los valores n y k en números y despues se suma
    suma = sum(int(d) for d in n) * k
    #Se retorna el calculo del supergisito con la suma
    return calcularSuperDigito(suma)


def calcularSuperDigito(n):
    #Si el número es menor de 10 , solo tiene 1 cifra
    if n < 10:
        #se retorna el número
        return n
    #Si tiene más de una cifra se aplica recursividad , se suma las cifras del número n
    else:
        return calcularSuperDigito(sum(int(d) for d in str(n)))
