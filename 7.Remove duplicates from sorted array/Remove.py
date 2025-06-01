# Clase con un método que elimina duplicados en una lista ordenada "in place"
class Solution(object):
    def removeDuplicates(self, nums):
        # Obtenemos el largo original de la lista
        largo = len(nums)
        
        # Este índice nos sirve para mantener la posición del último número único encontrado
        numeroUnico = 0

        # Recorremos la lista desde el segundo elemento (ya que el primero siempre es único)
        for numero in range(largo):
            # Comparamos el número actual con el último número único registrado
            if nums[numero] != nums[numeroUnico]:
                numeroUnico += 1  # Avanzamos la posición del último número único
                nums[numeroUnico] = nums[numero]  # Reemplazamos el valor duplicado con el nuevo valor único

        # Eliminamos todos los elementos sobrantes (duplicados al final de la lista)
        del nums[numeroUnico+1:]
