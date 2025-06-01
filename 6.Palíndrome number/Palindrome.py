# Clase que contiene un método para verificar si un número entero es palíndromo
class solution(object):
    def __init__(self,x):
        self.x=x
    def isPalindrome(self):
        # Convertimos el número a string, y lo comparamos con su reverso
        return str(self.x) == str(self.x)[::-1]

#Se ingres el número a verificar
x=int(input("Ingresa un numero"))
#Se crea la instancia
ejecucion=solution(x)
#se realizan las verificaciones
if (ejecucion==True):
    print(x , "No es un número palindromo")
else:
    print(x, "Es palindromo")
