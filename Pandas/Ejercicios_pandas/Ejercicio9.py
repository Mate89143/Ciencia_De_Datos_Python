import pandas as pd

df = pd.read_excel(
    "empleados.xlsx"
)

print("Primeros registros:")
print(df.head())

print("\nInformación:")
print(df.info())

print("\nEstadísticas:")
print(df.describe())

df.to_csv(
    "empleados_procesados.csv",
    index=False
)

df.to_excel(
    "empleados_procesados.xlsx",
    index=False
)

print("Archivos generados correctamente.")