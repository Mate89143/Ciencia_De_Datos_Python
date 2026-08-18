import pandas as pd

ventas=pd.Series(
    [1500000, 2300000, 1800000, 3100000, 2700000]
)

print("Ventas")
print(ventas)

print("Total:", ventas.sum())
print("Promedio:", ventas.mean())
print("Mayor:", ventas.max())
print("Menor:", ventas.min())