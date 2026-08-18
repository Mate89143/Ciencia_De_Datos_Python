import pandas as pd

datos = {
    "Nombre":[
        "Ana",
        "Carlos",
        "Luis",
        "María"
    ],
    "Edad":[
        25,
        31,
        28,
        35
    ],
    "Salario":[
        2500000,
        3200000,
        2800000,
        4000000
    ]
}

df = pd.DataFrame(datos)

print(df)