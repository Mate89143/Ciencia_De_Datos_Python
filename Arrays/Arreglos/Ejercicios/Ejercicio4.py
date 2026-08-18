import numpy as np

matriz = np.arange(1, 37).reshape(6, 6)
print("Matriz 6x6:")
print(matriz)

tercera_fila = matriz[2, :]
print("\nTercera fila:", tercera_fila)

cuarta_columna = matriz[:, 3]
print("Cuarta columna:", cuarta_columna)

diagonal = np.diag(matriz)
print("Diagonal principal:", diagonal)

pares = matriz[matriz % 2 == 0]
print("Números pares:", pares)