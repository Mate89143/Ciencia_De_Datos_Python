import numpy as np

# Ejercicio 4: Inventario inteligente

print("Inventario inteligente")

# Generar una matriz de existencias aleatorias para 15 productos en 8 sucursales
existencias = np.random.randint(0, 101, size=(15, 8))
print("Matriz de existencias (filas=productos, columnas=sucursales):")
print(existencias)

# Calcular estadísticas
total_productos = np.sum(existencias, axis=1)
total_sucursales = np.sum(existencias, axis=0)

# Identificar el producto con más existencias y la sucursal con menor inventario
producto_mas_existencias = np.argmax(total_productos) + 1
sucursal_menor_inventario = np.argmin(total_sucursales) + 1

# Calcular inventario total y promedio
inventario_total = np.sum(existencias)
inventario_promedio = np.mean(existencias)

# Identificar productos agotados (existencias=0)
agotados = np.where(existencias == 0)
productos_agotados = np.unique(agotados[0])

# Imprimir resultados
print(f"Total de existencias por producto: {total_productos}")
print(f"Total de existencias por sucursal: {total_sucursales}")
print(f"Producto con más existencias: Producto {producto_mas_existencias} con {total_productos[producto_mas_existencias-1]} unidades")
print(f"Sucursal con menor inventario: Sucursal {sucursal_menor_inventario} con {total_sucursales[sucursal_menor_inventario-1]} unidades")
print(f"Inventario total: {inventario_total} unidades")
print(f"Inventario promedio por producto: {inventario_promedio:.2f} unidades")
print(f"Productos agotados (existencias=0): {productos_agotados}")
