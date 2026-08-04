import numpy as np

# Ejercicio 5: Sistema de producción

print("Sistema de producción")

# Generar una matriz de producción aleatoria para 30 días en 3 líneas de producción
produccion = np.random.randint(0, 1001, size=(30, 3))
print("Producción diaria (filas=días, columnas=líneas de producción):")
print(produccion)

# Calcular estadísticas
producción_diaria = np.sum(produccion, axis=1)

# Identificar la produccion semanal (4 semanas de 7 días y 3 líneas de producción)
semanas = produccion[:28].reshape(4, 7, 3) 

# suma por semana
prod_semanal = np.sum(semanas, axis=(1, 2))  

# Identificar la produccion mensual
producción_mensual = np.sum(produccion)

# Identificar la línea con mayor producción
total_por_linea = np.sum(produccion, axis=0)
mejor_linea = np.argmax(total_por_linea) + 1

# Imprimir resultados
print(f"Producción diaria: {producción_diaria}")
print(f"Producción semanal: {prod_semanal}")
print(f"Producción mensual: {producción_mensual}")
print(f"Línea con mayor producción: Línea {mejor_linea} con {total_por_linea[mejor_linea-1]} unidades")