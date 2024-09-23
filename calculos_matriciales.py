import numpy as np

matrix_A = np.array([[1,2], [3,4]])
matrix_B = np.array([[5,6], [7,8]])

# Suma
print("A:\n", matrix_A)
print("B:\n", matrix_B)
sum = matrix_A + matrix_B
print("Suma:\n", sum)

# Multiplicación

product = np.dot(matrix_A, matrix_B)
print("Producto punto:\n", product)

# Determinante
det_A = np.linalg.det(matrix_A)
inv_A = np.linalg.inv(matrix_A)
print("Determinante de A:\n", det_A)
print("Inversa de A:\n", inv_A)
ident_matrix = matrix_A @ inv_A
print("Matrix A por su inversa:\n", ident_matrix)

# Resolver Ax = b
b = np.array([9,11])
x = np.linalg.solve(matrix_A,b)
print("La solución es:\n", x)
solution = inv_A @ b
print("La solución tambien es:\n", solution)