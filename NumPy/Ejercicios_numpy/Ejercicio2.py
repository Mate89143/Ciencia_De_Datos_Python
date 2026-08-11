import numpy as np

# Ejercicio 2: Matriz de ventas

print("Matriz de ventas")

# Generar una matriz de ventas aleatorias para 12 vendedores durante 6 meses
ventas = np.random.randint(1000, 5001, size=(12, 6))
print("Matriz de ventas (filas=vendedores, columnas=meses):")
print(ventas)

# Calcular cantidad total de ventas por vendedor y por mes
total_vendedores = np.sum(ventas, axis=1)
total_meses = np.sum(ventas, axis=0)

# Identificar el mejor y peor vendedor
mejor_vendedor = np.argmax(total_vendedores) + 1
peor_vendedor = np.argmin(total_vendedores) + 1

# Calcular el promedio de ventas por mes
promedio_mensual = np.mean(ventas, axis=0)

# Imprimir resultados
print(f"Total de ventas por vendedor: {total_vendedores}")
print(f"Total de ventas por mes: {total_meses}")
print(f"Mejor vendedor: Vendedor {mejor_vendedor} con {total_vendedores[mejor_vendedor-1]} ventas")
print(f"Peor vendedor: Vendedor {peor_vendedor} con {total_vendedores[peor_vendedor-1]} ventas")
print(f"Promedio de ventas por mes: {promedio_mensual}")