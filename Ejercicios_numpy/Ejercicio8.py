import numpy as np

# Ejercicio 8: Encuesta nacional

print("Encuesta nacional")

# Generar un arreglo de 500 edades aleatorias entre 18 y 80 años
edades = np.random.randint(18, 81, size=500)
print("Primeras 10 edades:", edades[:10])

# Calcular estadísticas de las edades
promedio_edad = np.mean(edades)
mediana_edad = np.median(edades)
maxima_edad = np.max(edades)
minima_edad = np.min(edades)

# Identificar la moda de las edades
valores_unicos, conteo_edades = np.unique(edades, return_counts=True)
moda_edad = valores_unicos[np.argmax(conteo_edades)]
frecuencia_moda = np.max(conteo_edades)

# Ordena las edades para mostrar un resumen ordenado
edades_ordenadas = np.sort(edades)
print("Edades ordenadas:", edades_ordenadas[:10])

# Imprimir resultados
print(f"Promedio de edad: {promedio_edad:.2f} años")
print(f"Mediana de edad: {mediana_edad} años")
print(f"Moda de edad: {moda_edad} años (frecuencia: {frecuencia_moda})")
print(f"Edad máxima: {maxima_edad} años")
print(f"Edad mínima: {minima_edad} años")
print(f"Mayoría de edad: {np.sum(edades >= 18)} personas")