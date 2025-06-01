# Problema: Decidir si se puede participar en una actividad dada una condición
# Entrada: Dos números enteros s1 y s2
# Regla: Si duplicando el valor de s1 es mayor o igual a s2, se imprime "E" (Éxito)
#        De lo contrario, se imprime "N" (No se puede)

# Definimos una función lambda (función anónima) que recibe dos valores s1 y s2
# y retorna "E" si s1*2 >= s2, caso contrario "N".
facil = lambda s1, s2: "E" if s1*2 >= s2 else "N"

# Leemos dos números desde la entrada estándar, separados por espacio
s1, s2 = map(int, input().split())

# Imprimimos el resultado de aplicar la función con los valores leídos
print(facil(s1, s2))

