# Clase con un método que elimina todas las ocurrencias de un valor específico de una lista
class Solution(object):
    def removeElement(self, nums, val):
        # Se usa comprensión de listas para filtrar todos los elementos que NO son iguales a 'val'
        # nums[:] permite modificar la lista original (in place)
        nums[:] = [x for x in nums if x != val]
