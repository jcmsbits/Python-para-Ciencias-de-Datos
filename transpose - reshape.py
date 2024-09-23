import numpy as np


# Matrix transpuesta
matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
transpose_matrix = matrix.T
print("Matrix original: ", matrix)
print("Matrix Transpuesta: ", transpose_matrix)

# Reshape

array = np.arange(1,13)
reshaped_array = array.reshape(3,4)    
print("Array original: ", array)
print("Array reshaped: ", reshaped_array)


# Invertir un array
reversed_array = array[::-1]
print("Array sin invertir: ", array)
print("Array invertido: ", reversed_array) 

# Aplanando Matrices

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
flatten_matrix = matrix.flatten()
print("Matrix sin aplanar: ", matrix)
print("Matrix aplanada: ", flatten_matrix)