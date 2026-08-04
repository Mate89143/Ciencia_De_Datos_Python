import numpy as np

ventas = np.array([1500, 2200, 1800, 2400, 3100, 2800, 
                   3500, 4000, 3700, 2900, 2100, 1900])

total_anual = np.sum(ventas)

promedio_mensual = np.mean(ventas)

mes_mayor = np.argmax(ventas) + 1  

mes_menor = np.argmin(ventas) + 1

print("Total de ventas anual:", total_anual)
print("Promedio de ventas mensual:", promedio_mensual)
print("Mes con mayor venta:", mes_mayor, "valor:", ventas[mes_mayor-1])
print("Mes con menor venta:", mes_menor, "valor:", ventas[mes_menor-1])
