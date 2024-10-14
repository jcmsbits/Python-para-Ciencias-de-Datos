import numpy as np


# Paso 1: Crear arrays con datos de ventas mensuales
meses = np.array(["Enero", "Febrero", "Marzo", "Abril", 
          "Mayo", "Junio", "Julio", "Agosto", 
          "Septiembre", "Octubre", "Noviembre", "Diciembre"])

product_A = np.array([150,200,250,300,220,210,180, 190, 230, 240,280,300])
product_B = np.array([180,210,230,250,270,260,240,250,270,290,310,330])
product_C = np.array([200,220,240,260,280,300,320,340,360,380,400,420])

# Paso 2: Transformaciones básicas con Numpy
# Estadísticas básicas

mean_A = np.mean(product_A)
sum_A = np.sum(product_A)
mean_B = np.mean(product_B)
sum_B = np.sum(product_B)
mean_C = np.mean(product_C)
sum_C = np.sum(product_C)

print("Promedio de ventas Producto A: ", mean_A)
print("Total de ventas Producto A: ", sum_A)
print("Promedio de ventas Producto B: ", mean_B)
print("Total de ventas Producto B: ", sum_B)
print("Promedio de ventas Producto C: ", mean_C)
print("Total de ventas Producto C: ", sum_C)


# Manipulación y Analisis de Datos
# Calcular el total de ventas de por mes

total_ventas_mes = product_A + product_B + product_C

promedio_ventas_productos = np.array([mean_A, mean_B, mean_C])
print("Promedio de ventas por producto: ", promedio_ventas_productos)

# Identificar el mes con mayor y menor ventas

argmax_total = np.argmax(total_ventas_mes)
print("Argmax total: ", argmax_total)

mes_mayor_venta = meses[argmax_total]
print("Mes con mayor venta: ", mes_mayor_venta)

argmin_total = np.argmin(total_ventas_mes)
mes_menor_venta = meses[argmin_total]
print("Mes con menor venta: ", mes_menor_venta)


# Operaciones avanzadas con Numpy
# Reshape y Transposición
ventas_matrix = np.array([product_A, product_B, product_C])
ventas_reshaped = ventas_matrix.reshape(3,4,3)
ventas_transpose = ventas_reshaped.T
print("Ventas de Matrix:\n", ventas_matrix)

# Al hacer el reshape obtengo los precios de los 3 productos
# divido por trimestre
print("Ventas de Reshaped:\n ", ventas_reshaped)

# Al hacer la traspuesta obtengo Dividido por trimestre
# los precios de los 3 productos
print("Ventas traspuesta:\n ", ventas_transpose)
print("Shape ventas:\n ", ventas_transpose.shape)


# Invertir arrays y aplanar matrices
ventas_inverted = ventas_matrix[:, ::-1]
ventas_flatten = ventas_inverted.flatten()

print("Ventas invertidas:\n ", ventas_inverted)
print("Ventas aplanadas:\n",ventas_flatten )

# Paso 5: Análisis de elementos únicos y sus conteos
unique_ventas, counts_ventas = np.unique(ventas_flatten, return_counts = True)
print("Elementos únicos de las ventas:\n", unique_ventas)
print("Conteos de elementos únicos de la venta:\n", counts_ventas)

# Paso 6: Indexación y Slicing
# Seleccionar ventas del primer trimestre

ventas_primer_trimestre = ventas_matrix[:, :3]
print("Shape ventas matrix:\n", ventas_matrix.shape)
print("Ventas del primer trimestre:\n", ventas_primer_trimestre)

# Indexación booleana para selecionar meses con ventas totales superiores a 800
true_altas_ventas = total_ventas_mes > 800
print("Cuales fueron los meses altos en ventas (Bool):\n", true_altas_ventas)
meses_alta_ventas= meses[true_altas_ventas]
print("Cuales fueron los meses altos en ventas (Meses):\n", meses_alta_ventas)
ventas_altas = total_ventas_mes[true_altas_ventas]
print("Ventas totales superiores a 800:\n", ventas_altas)

# Selección avanzada

indices = [0,2,4,6,8,10]
ventas_indices_seleccionada = ventas_matrix[:, indices]
print("Ventas en meses seleccionados:\n", ventas_indices_seleccionada)