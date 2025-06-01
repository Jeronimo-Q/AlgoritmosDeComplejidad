# Clase que contiene un método para verificar si un número entero es palíndromo
class solution(object):
    def isPalindrome(self, x):
        # Convertimos el número a string, y lo comparamos con su reverso
        return str(x) == str(x)[::-1]
        # Si son iguales, entonces es un palíndromo y retornamos True
        # Si no, retornamos False
