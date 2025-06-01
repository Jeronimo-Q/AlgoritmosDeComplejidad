def es_valido(sudoku, fila, col, num):
    """ Verifica si num se puede colocar en (fila, col) """
    # Verificar la fila
    if num in sudoku[fila]:
        return False
    
    # Verificar la columna
    if num in [sudoku[i][col] for i in range(9)]:
        return False

    # Verificar la subcuadrícula 3x3
    inicio_fila, inicio_col = (fila // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[inicio_fila + i][inicio_col + j] == num:
                return False

    return True

def resolver_sudoku(sudoku):
    """ Resuelve un Sudoku de manera iterativa (sin recursividad) """
    vacios = []  # Lista de posiciones vacías (0)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                vacios.append((i, j))  # Guardar coordenadas de celdas vacías

    indice = 0
    while indice < len(vacios):
        fila, col = vacios[indice]
        num = sudoku[fila][col] + 1  # Intentar el siguiente número

        while num <= 9 and not es_valido(sudoku, fila, col, num):
            num += 1  # Buscar el siguiente número válido

        if num <= 9:  # Si encontramos un número válido, lo colocamos
            sudoku[fila][col] = num
            indice += 1  # Pasar al siguiente espacio vacío
        else:  # Si no encontramos un número válido, hacemos "backtracking" manual
            sudoku[fila][col] = 0  # Reiniciar celda
            indice -= 1  # Retroceder a la celda anterior y probar otro número

    return sudoku  # Devolver el Sudoku resuelto

# Sudoku de ejemplo
sudoku = [
    [1, 0, 4, 0, 2, 0, 5, 0, 3],
    [0, 8, 0, 3, 0, 1, 0, 0, 0],
    [2, 9, 3, 0, 0, 5, 0, 0, 1],
    [0, 0, 2, 0, 6, 0, 0, 0, 5],
    [0, 0, 0, 4, 0, 8, 0, 0, 0],
    [9, 0, 0, 0, 5, 0, 7, 0, 0],
    [5, 0, 0, 6, 0, 0, 8, 3, 2],
    [0, 0, 0, 5, 0, 2, 0, 4, 0],
    [4, 0, 8, 0, 3, 0, 9, 0, 6]
]

sudoku_resuelto = resolver_sudoku(sudoku)

for fila in sudoku_resuelto:
    print(fila)
