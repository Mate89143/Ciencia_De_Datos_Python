import pandas as pd

datos = {
    "Nombre": ["Ana", "Carlos", "Luis"],
    "Edad": [20, 25, 30],
    "Ciudad": ["Medellín", "Cali", "Bogotá"]
}

df = pd.DataFrame(datos)

# Crea una nueva columna "MayorEdad"
df["MayorEdad"] = df["Edad"] >= 18

# Modifica una columna
df["Edad"] = df["Edad"]+1

print(df)