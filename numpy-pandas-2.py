import numpy as np

# Indexing y Slicing
array = np.array([10,20,30,40,50])
print(array[1])
print(array[-1])

# Subconjunto
print(array[1:4])

print("Se excede y llega hasta el último", array[1:7])

print("No toma ninguno", array[-1:-7])

# Indexación booleana

bool_index = array > 25
print(bool_index)
print(type(bool_index))


index = array[[2,0,4]]
print(index)


array = np.random.randint(1,10, size=(3,3))
print("Randint", array)
print("Posición por fila y columna", array[0,1])
print("Conjunto por fila o por columna", array[:2, :1])

