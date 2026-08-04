import numpy as np

matriz = np.array([[10, 20, 30],[40, 50, 60]])

matriz_reshape = matriz.reshape(3, 2)

matriz_flatten = matriz.flatten()

matriz_transpose = matriz.transpose()

print(matriz.reshape(3, 2))
print(matriz.flatten())
print(matriz.transpose())