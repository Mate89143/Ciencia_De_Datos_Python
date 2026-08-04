import numpy as np

# Ejercicio 1: Registro de temperaturas

print("Registro de temperaturas")

# Generar un arreglo de 30 temperaturas aleatorias entre 15 y 35 grados Celsius
temperaturas = np.random.uniform(15, 35, size=30)

# Redondear las temperaturas a un decimal
temperaturas = np.round(temperaturas, 1)

# Calcular estadísticas
prom = np.mean(temperaturas)
máxima = np.max(temperaturas)
mínima = np.min(temperaturas)
desviación = np.std(temperaturas)
varianza = np.var(temperaturas)

# Identificar los días con la temperatura más alta y más baja
dia_caluroso = np.argmax(temperaturas) + 1
dia_fresco = np.argmin(temperaturas) + 1

# Imprimir resultados
print(f"Temperaturas registradas: {temperaturas}")
print(f"Promedio de temperaturas: {prom:.2f}°C")
print(f"Temperatura máxima: {máxima:.1f}°C (Día {dia_caluroso})")
print(f"Temperatura mínima: {mínima:.1f}°C (Día {dia_fresco})")
print(f"Desviación estándar: {desviación:.2f}")
print(f"Varianza: {varianza:.2f}")
print(f"Día más caluroso: Día {dia_caluroso} con {máxima:.1f}°C")
print(f"Día más fresco: Día {dia_fresco} con {mínima:.1f}°C")