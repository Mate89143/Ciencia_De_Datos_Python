import pandas as pd

# Leer archivo CSV
df = pd.read_csv("ventas.csv")

print(df.head())

# Leer archivo Excel
alo = pd.read_excel(
    "ventas.xlsx",
    sheet_name="Sheet1"
)

print(alo.head())