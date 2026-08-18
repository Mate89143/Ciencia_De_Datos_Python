import pandas as pd

# Leer archivo CSV
df = pd.read_csv("ventas(2).csv")

print("Primeros registros:")
print(df.head())

# Crear columna Total
df["Total"] = df["Cantidad"] * df["Precio"]

# Total vendido
total_vendido = df["Total"].sum()

# Promedio de ventas
promedio_ventas = df["Total"].mean()

# Producto más vendido
producto_mas_vendido = (
    df.groupby("Producto")["Cantidad"]
    .sum()
    .idxmax()
)

# Venta más alta
venta_mas_alta = df["Total"].max()

# Venta más baja
venta_mas_baja = df["Total"].min()

print("\nTotal vendido:", total_vendido)
print("Promedio de ventas:", promedio_ventas)
print("Producto más vendido:", producto_mas_vendido)
print("Venta más alta:", venta_mas_alta)
print("Venta más baja:", venta_mas_baja)

print("\nDataFrame completo:")
print(df)