# Clase que genera combinaciones de letras a partir de una secuencia de dígitos (como en los teclados antiguos de celular)
class Solution(object):
    def letterCombinations(self, digits):
        # Si la entrada está vacía, no hay combinaciones posibles
        if not digits:
            return []
        
        # Mapeo de dígitos a letras como en un teclado telefónico
        teclado = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        resultado = []  # Lista para almacenar todas las combinaciones posibles
        
        # Función auxiliar que explora recursivamente todas las combinaciones
        def buscar(indice, actual):
            # Si ya hemos recorrido todos los dígitos, agregamos la combinación actual al resultado
            if indice == len(digits):
                resultado.append(actual)
                return
            
            # Por cada letra que corresponde al dígito actual, continuamos la búsqueda
            for letra in teclado[digits[indice]]:
                buscar(indice + 1, actual + letra)  # Avanzamos al siguiente dígito
        
        # Iniciamos la búsqueda desde el primer dígito con una cadena vacía
        buscar(0, "")
        
        return resultado
