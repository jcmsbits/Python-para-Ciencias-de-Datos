import numpy as np



array_1 = np.array([10,20,30,40])
array_2 = np.array([1,2,3,4])

suma = array_1 + array_2
resta = array_1 - array_2
mult = array_1 * array_2
div = array_1 / array_2

print("Suma:\n", suma)
print("Resta:\n", resta)
print("Multiplicación:\n", mult)
print("División:\n", div)

#----------------------------------------------

datos = np.array([23,76,35,67, 89,45,68,79,35])

media = np.mean(datos)
mediana = np.median(datos)
varianza = np.var(datos)
std = np.var(datos)

print("Media:\n", media)
print("Mediana:\n", mediana)
print("Varianza:\n", varianza)
print("Desviación estandar:\n", std)


# Crea dos matrices de 2x2 y realiza las operaciones de suma, resta,
# multiplicación (producto matricial) y cálculo de la inversa de una de ellas.
matriz_1 = np.random.random([2,2])
matriz_2 = np.random.randint(1,10, size = (2,2))
print("Matriz 1:\n", matriz_1)
print("Matriz 2:\n", matriz_2)


suma = matriz_1 + matriz_2
resta = matriz_1 - matriz_2
dot = np.dot(matriz_1,matriz_2)
inv_matriz_2 = np.linalg.inv(matriz_2)

print("Suma:\n", suma)
print("Resta:\n", resta)
print("Multiplicación:\n", dot)
print("Inversa Matrix 2:\n", inv_matriz_2)


# Resuelve el sistema de ecuaciones lineales dado por Ax=b, 
# donde A es una matriz 2x2 y b es un vector de 2 elementos.

A = np.random.randint(1,10, size = (2,2))
b = np.array([2,3])

solve = np.linalg.solve(A, b)

print("Matrix A:\n", A)
print("Vector b", b)
print("Solución:\n", solve)
print("Solución con inversa de A y producto punto:\n", np.linalg.inv(A) @ b)

# Genera un array de 1000 números aleatorios que sigan una distribución normal
# con media 0 y desviación estándar 1. Calcula la media y desviación estándar del array generado.

datos_simulados = np.random.normal(0,1, 1000)
media_simulada = np.mean(datos_simulados)
desviacion_simulada = np.std(datos_simulados)

print("Media de los datos simulados:\n", media_simulada)
print("Desviación estandar de los datos simulados:\n", desviacion_simulada)