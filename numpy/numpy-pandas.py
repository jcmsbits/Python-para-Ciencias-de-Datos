# Arrays en Numpy

import numpy as np

escalar = np.array(42)
print(type(escalar))
print(escalar)

vector = np.array([30,29,35,31,33,36,42])
print(vector)

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix)

tensor = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [0,11,12]]])
print(tensor)

array_range = np.arange(10)
print(array_range)

eye_matrix = np.eye(6)
print(eye_matrix)

diag = np.diag([1,2,3,4,5,6])
print(diag)

random = np.random.random([2,3])
print(random)

array = np.array([[1,2,3], [4,5,6]])
print(array.ndim)
print(array.shape)
print(array.dtype)


z = np.array(3, dtype= np.uint8)
print(z)
print(z.dtype)

double_precision = np.array([1,2,3], dtype='d')
print(double_precision)
print(double_precision.dtype)

z = z.astype(np.float64)
print(z)


sum = np.sum(array)
print(sum)

mean = np.mean(array)
print(mean)

std = np.std(array)
print(std)