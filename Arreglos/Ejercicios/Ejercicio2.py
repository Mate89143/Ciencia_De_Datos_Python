import numpy as np

notas = np.random.randint(0, 21, size=(5, 4))
print("Matriz de notas (filas=estudiantes, columnas=notas):")
print(notas)

promedio_estudiante = np.mean(notas, axis=1)

promedio_general = np.mean(notas)

nota_maxima = np.max(notas)

nota_minima = np.min(notas)

print("Promedio de cada estudiante:", promedio_estudiante)
print("Promedio general de la clase:", promedio_general)
print("Nota máxima en la clase:", nota_maxima)
print("Nota mínima en la clase:", nota_minima)