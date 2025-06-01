import random
import tkinter as tk

# Parámetros principales
nPoblacion = 100          # Número de soluciones por generación
nGeneraciones = 10000     # Límite de generaciones
probabilidadMutacion = 0.1  # Probabilidad de mutar un hijo

# Crea una población inicial aleatoria
def generarPoblacion():
    soluciones = []
    for _ in range(nPoblacion):
        # Cada índice representa una fila y el valor es la columna donde está la reina
        solucion = [random.randint(0, 7) for _ in range(8)]
        soluciones.append(solucion)
    return soluciones

# Calcula cuántas reinas se atacan entre sí
def fitness(solucion):
    ataques = 0
    for i in range(len(solucion)):
        for j in range(i + 1, len(solucion)):
            # Mismo columna o misma diagonal
            if solucion[i] == solucion[j] or abs(i - j) == abs(solucion[i] - solucion[j]):
                ataques += 1
    return ataques

# Busca si alguna solución de la población no tiene ataques
def buscarSolucion(poblacion):
    for solucion in poblacion:
        if fitness(solucion) == 0:
            return solucion
    return False

# Selecciona las mejores soluciones (las que tienen menos ataques)
def seleccion(poblacion):
    puntajes = [fitness(sol) for sol in poblacion]
    mejores_indices = sorted(range(len(puntajes)), key=lambda i: puntajes[i])[:30]
    return [poblacion[i] for i in mejores_indices]

# Cruza dos soluciones para generar hijos combinando partes de ambas
def cruce(padre1, padre2):
    punto = random.randint(1, 7)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2

# Cambia una posición de la solución aleatoriamente
def mutacion(hijo):
    if random.random() < probabilidadMutacion:
        indice = random.randint(0, 7)
        hijo[indice] = random.randint(0, 7)
    return hijo

# Muestra el tablero con las reinas en rojo
def mostrarTablero(solucion):
    for widget in frame_tablero.winfo_children():
        widget.destroy()

    for i in range(8):
        for j in range(8):
            color = 'burlywood' if (i + j) % 2 == 0 else 'saddlebrown'
            if solucion[i] == j:
                casilla = tk.Label(frame_tablero, width=4, height=2, bg='red', relief='solid')
            else:
                casilla = tk.Label(frame_tablero, width=4, height=2, bg=color, relief='solid')
            casilla.grid(row=i, column=j)

# Ejecuta el algoritmo genético hasta encontrar una solución o agotar generaciones
def algoritmoGenetico():
    global ciclo
    ciclo = True
    while ciclo:
        poblacion = generarPoblacion()
        for i in range(nGeneraciones):
            generacion = i + 1
            solucion = buscarSolucion(poblacion)
            if solucion:
                print("Solución encontrada")
                mostrarTablero(solucion)
                print("Generación:", generacion)
                ciclo = False
                break

            seleccionados = seleccion(poblacion)
            nuevaPoblacion = []

            while len(nuevaPoblacion) < nPoblacion:
                padre1 = random.choice(seleccionados)
                padre2 = random.choice(seleccionados)
                hijo1, hijo2 = cruce(padre1, padre2)
                hijo1 = mutacion(hijo1)
                hijo2 = mutacion(hijo2)
                nuevaPoblacion.append(hijo1)
                if len(nuevaPoblacion) < nPoblacion:
                    nuevaPoblacion.append(hijo2)

            poblacion = nuevaPoblacion

        if ciclo:
            print("No se encontró solución.")
            ciclo = False

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Problema de las 8 Reinas - Algoritmo Genético")
ventana.geometry("600x650")

frame_tablero = tk.Frame(ventana)
frame_tablero.pack()

boton_iniciar = tk.Button(ventana, text="Iniciar Algoritmo Genético", command=algoritmoGenetico)
boton_iniciar.pack(pady=20)

ventana.mainloop()
