import pandas as pd

# Leer archivo Excel
df = pd.read_excel("inventario.xlsx")

print("Inventario:")
print(df)

# Productos con stock inferior a 10
stock_bajo = df[df["Stock"] < 10]

print("\nProductos con stock inferior a 10:")
print(stock_bajo)

# Valor total del inventario
df["Valor_Total"] = df["Stock"] * df["Precio"]

valor_inventario = df["Valor_Total"].sum()

print("\nValor total del inventario:", valor_inventario)

# Producto más costoso
producto_costoso = df.loc[df["Precio"].idxmax()]

print("\nProducto más costoso:")
print(producto_costoso)

# Ordenar por stock
df_ordenado = df.sort_values("Stock")

print("\nProductos ordenados por stock:")
print(df_ordenado)

# Exportar resultado
df_ordenado.to_excel(
    "inventario_analizado.xlsx",
    index=False
)

print("\nArchivo inventario_analizado.xlsx creado correctamente.")