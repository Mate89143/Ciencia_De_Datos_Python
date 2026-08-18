import pandas as pd

# Leer archivos
clientes = pd.read_csv("clientes.csv")
ventas = pd.read_excel("ventas(1).xlsx")

# Inspeccionar DataFrames
print("Clientes:")
print(clientes)

print("\nVentas:")
print(ventas)

# Calcular total vendido por cliente
totales = (
    ventas.groupby("IDCliente")["Valor"]
    .sum()
    .reset_index()
)

totales = totales.rename(
    columns={"Valor": "Total_Comprado"}
)

# Unir clientes con sus ventas
reporte = clientes.merge(
    totales,
    on="IDCliente",
    how="left"
)

# Clientes sin ventas tendrán valor 0
reporte["Total_Comprado"] = reporte["Total_Comprado"].fillna(0)

# Identificar clientes sin ventas
sin_ventas = reporte[reporte["Total_Comprado"] == 0]

print("\nClientes sin ventas:")
print(sin_ventas)

# Ordenar de mayor a menor
reporte = reporte.sort_values(
    "Total_Comprado",
    ascending=False
)

print("\nReporte ordenado:")
print(reporte)

# Crear archivo Excel
reporte.to_excel(
    "reporte_clientes.xlsx",
    index=False
)

print("\nReporte generado correctamente.")