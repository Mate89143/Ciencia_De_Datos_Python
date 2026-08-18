import pandas as pd

df = pd.read_csv("ventas(1).csv")

print(df)

print("\nInformación")
print(df.info())

print("\nEstadísticas")
print(df.describe())