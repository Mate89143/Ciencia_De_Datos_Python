import numpy as np

# Ejercicio 9: Simulación financiera

print("Simulación financiera")

# Generar un arreglo de precios de acciones simulados para 100 días
precios = np.zeros(100)
precios[0] = 100  # precio inicial
for i in range(1, 100):
    precios[i] = precios[i-1] + np.random.uniform(-2, 2)
    
# Asegurarse de que los precios no sean negativos y redondear a dos decimales
precios = np.maximum(precios, 10)  # Asegurarse de que los precios no sean negativos
precios = np.round(precios, 2)

print("Precios de acciones simulados (100 días):")
print(precios[:10], "...")  # Mostrar solo los primeros 10 días para no saturar la salida

# Calcular estadísticas de los precios
promedio_precio = np.mean(precios)
maximo_precio = np.max(precios)
minimo_precio = np.min(precios)
variacion_precio = ((precios[-1] - precios[0]) / precios[0]) * 100

dias_superior = np.where(precios > promedio_precio)[0] + 1

print(f"Promedio de precio: {promedio_precio:.2f}")
print(f"Precio máximo: {maximo_precio:.2f}")
print(f"Precio mínimo: {minimo_precio:.2f}")
print(f"Variación porcentual del precio: {variacion_precio:.2f}%")
print(f"Días con precio superior al promedio: {dias_superior}")