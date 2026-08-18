import numpy as np

edades = np.array([18, 22, 19, 25, 30, 21, 19, 28, 35, 40, 22, 26, 31, 24, 27])

promedio = np.mean(edades)

edad_mayor = np.max(edades)

edad_menor = np.min(edades)

cantidad = len(edades)

print("Promedio de edades:", promedio)
print("Edad mayor:", edad_mayor)
print("Edad menor:", edad_menor)
print("Cantidad de edades:", cantidad)
