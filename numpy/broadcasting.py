import numpy as np
prices = np.array([100,200,300])
discount = np.array([0.9])
discount_prices = prices * discount
print(discount_prices)


prices_matrix = np.random.randint(100,500, size = (3,3))
print("Matrix con precios aleatorios",prices_matrix)
discount = np.array([10,20,30])
print("Discount sin forma de matrix", discount)
discount_prices = prices_matrix - discount
print("Variable modificada en cada fila por el broadcasting: ", discount_prices)


array = np.array([1,2,3,4,5])
print("Saber si todos cumplen con la condición: ", np.all(array>0))

print("Saber si al menos 1 elemento es mayor a 4", np.any(array>4))

array_a = np.array([1,2,3])
array_b = np.array([4,5,6])

concatenated_a = np.concatenate((array_a, array_a))
concatenated_b = np.concatenate((array_a, array_b))

print("Concatenando el mismo array: ", concatenated_a )
print('Concatenando dos arrays el método concatenate: ',concatenated_b)

stacked_v = np.vstack((array_a, array_b))

print("Array apilados verticalmente: ",stacked_v)

stacked_h = np.hstack((array_a, array_b))
print("Array apilados horizontalmente: ", stacked_h )

array_c = np.arange(1, 10)
split_array = np.split(array_c, 3)
print("Array_c sin dividir: ", array_c)
print("Array_c dividido: ",split_array)


array_d = np.arange(1, 12)
split_array_d = np.split(array_c, 3)
print("Array_d sin dividir: ", array_d)
print("Array_d dividido: ",split_array_d)