import numpy as np

matriz = np.array([[10, 20, 30],
            [40, 50, 60]])

print(matriz.shape) # Salida: (2, 3) - 2 filas y 3 columnas
print(matriz.ndim) # Salida: 2 - es una matriz de 2 dimensiones
print(matriz.size) # Salida: 6 - tiene 6 elementos
print(matriz.dtype) # Salida: int64 - los elementos son enteros de 64 bits