import pandas as pd

datos = {
    "Código": [
        "001", "002", "003", "004", "005",
        "006", "007", "008", "009", "010",
        "011", "012", "013", "014", "015"
    ],

    "Nombre": [
        "Ana", "Carlos", "Luis", "María", "Pedro",
        "Laura", "Sofía", "Juan", "Camila", "Andrés",
        "Valentina", "Daniel", "Paula", "Mateo", "Sara"
    ],

    "Edad": [
        20, 21, 19, 22, 20,
        23, 21, 19, 22, 20,
        21, 24, 20, 22, 19
    ],

    "Programa": [
        "Ciencia de Datos", "ADSO", "Ciencia de Datos",
        "ADSO", "Ciencia de Datos", "ADSO",
        "Ciencia de Datos", "ADSO", "Ciencia de Datos",
        "ADSO", "Ciencia de Datos", "ADSO",
        "Ciencia de Datos", "ADSO", "Ciencia de Datos"
    ],

    "Nota final": [
        4.5, 3.8, 2.9, 4.0, 3.2,
        2.5, 4.7, 3.0, 2.8, 4.2,
        3.6, 2.7, 4.8, 3.4, 2.9
    ]
}

df = pd.DataFrame(datos)

print("DataFrame de estudiantes:")
print(df)

# Estudiantes aprobados
aprobados = df.loc[df["Nota final"] >= 3.0]

# Estudiantes reprobados
reprobados = df.loc[df["Nota final"] < 3.0]

print("\nEstudiantes aprobados:")
print(aprobados)

print("\nEstudiantes reprobados:")
print(reprobados)

print("\nPromedio general:", df["Nota final"].mean())
print("Nota máxima:", df["Nota final"].max())
print("Nota mínima:", df["Nota final"].min())

# Ejemplo usando iloc
print("\nPrimer estudiante:")
print(df.iloc[0])