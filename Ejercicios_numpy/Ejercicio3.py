import numpy as np

# Ejercicio 3: Análisis académico

notas = np.random.randint(0, 15, size=(40, 5))
print("Matriz de notas (filas=estudiantes, columnas=asignaturas):")
print(notas)

promedio_estudiantes = np.mean(notas, axis=1)
promedio_asignaturas = np.mean(notas, axis=0)

mejor_estudiante = np.argmax(promedio_estudiantes) + 1
peor_estudiante = np.argmin(promedio_estudiantes) + 1

aprobados_por_estudiantes = np.sum(notas >= 11, axis=1)

aprobados = np.sum(aprobados_por_estudiantes >= 1)
reprobados = np.sum(aprobados_por_estudiantes < 1)

print(f"Promedio de cada estudiante: {promedio_estudiantes}")
print(f"Promedio de cada asignatura: {promedio_asignaturas}")
print(f"Mejor estudiante: Estudiante {mejor_estudiante} con promedio {promedio_estudiantes[mejor_estudiante-1]}")
print(f"Peor estudiante: Estudiante {peor_estudiante} con promedio {promedio_estudiantes[peor_estudiante-1]}")
print(f"Cantidad de estudiantes aprobados: {aprobados}")
print(f"Cantidad de estudiantes reprobados: {reprobados}")