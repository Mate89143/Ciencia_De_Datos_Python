import numpy as np

# Ejercicio 7: Simulación de sensores IoT

print("Simulación de sensores IoT")

# Generar un arreglo de 100 mediciones aleatorias de sensores entre 0 y 100
mediciones = np.random.uniform(0, 100, size=100)
mediciones = np.random.randint(0, 101, size=100)
print("Mediciones de sensores (100 valores):")
print(mediciones)

# Identificar mediciones fuera del rango aceptable (20-80)
fuera_de_rango = np.where((mediciones < 20) | (mediciones > 80))

# Calcular mediciones promedio y desviación estándar
promedio_mediciones = np.mean(mediciones)
desviacion_mediciones = np.std(mediciones)

# Calcular la cantidad de mediciones críticas (fuera del rango aceptable)
criticos = len(fuera_de_rango)

print(f"Sensores fuera del rango aceptable (20-80): {fuera_de_rango[0]}")
print(f"Promedio de mediciones: {promedio_mediciones:.2f}")
print(f"Desviación estándar de mediciones: {desviacion_mediciones:.2f}")
print(f"Cantidad de sensores críticos (fuera del rango aceptable): {criticos}")
