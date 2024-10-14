import numpy as np

survey_responses = np.array([
    "bueno", "excelente", "malo",
    "bueno", "malo", "excelente",
    "bueno", "bueno", 
    "excelente"
])

print("Usando el método Unique para no obtener elementos repetidos: ", np.unique(survey_responses))

unique_elements, counts = np.unique(survey_responses, return_counts= True)
print("Unicos elementos: ", unique_elements)
print("Cantidad de cada elemento: ", counts)


# La vista hace referencia al array original
array_x = np.arange(10)
view_y = array_x[1:3]
print("Array original: ", array_x)
print("Vista de elementos del array: ", view_y)
print("Dirección en memoria del array: ", id(array_x[1:3]))
print("Dirección en memoria de view: ", id(view_y))
array_x[1:3] = [10,11]

print("Array modificado: ", array_x)
print("Vista modificada", view_y)

print("Metodo base: ", view_y.base)

print('*'* 100)
# De esta manera hace una copia
array_x = np.arange(10)
copy_x = array_x[[1,2]]
print("Segundo Array original: ", array_x)
print("Copy de elementos del array: ", copy_x)
array_x[1:3] = [10,11]
print("Array modificado: ", array_x)
print("Copia sin modificar", copy_x)

print("Metodo base: ", copy_x.base)