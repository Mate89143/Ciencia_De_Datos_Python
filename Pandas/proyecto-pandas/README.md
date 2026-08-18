# Sistema de Análisis Empresarial con Pandas

Proyecto correspondiente a la Actividad de Aprendizaje #4 – Sistema de Análisis Empresarial con Pandas, del módulo Ciencia de Datos con Python, ADSO – SENA.

# Objetivo

Construir una aplicación en Python y Pandas que permita cargar, explorar, analizar y generar reportes a partir de información empresarial almacenada en CSV y Excel.

# Estructura

proyecto-pandas/
├── data/
│   ├── clientes.csv
│   ├── productos.xlsx
│   └── ventas.csv
├── src/
│   └── analisis.py
├── reports/
│   └── reporte_final.xlsx
├── README.md
└── requirements.txt

# Datos

clientes.csv: 30 clientes.

productos.xlsx: 20 productos.

ventas.csv: 120 ventas.

reporte_final.xlsx: reporte generado por el programa.

# Requisitos

Python 3.10 o superior recomendado.

# Instalar dependencias:

pip install -r requirements.txt

# Ejecución

Desde la carpeta raíz proyecto-pandas:

python src/analisis.py

También puede ejecutarse con la ruta completa al archivo:

python src/analisis.py

El programa utiliza pathlib y determina automáticamente la carpeta raíz del proyecto a partir de la ubicación de analisis.py. Por eso no es necesario modificar rutas absolutas de Windows.

# Funcionalidades

Carga de clientes, productos y ventas.

Validación de archivos.

Exploración de DataFrames.

Creación y uso de Series.

Cálculo de indicadores de ventas.

Análisis de clientes.

Análisis de productos.

Uso de filtros y agrupaciones.

Generación de reporte_final.xlsx.

Uso de métodos adicionales de Pandas.

# Métodos investigados

Se utilizan más de los cinco métodos solicitados:

value_counts(): cuenta la frecuencia de valores.

nunique(): cuenta valores únicos.

drop_duplicates(): elimina registros duplicados.

rename(): cambia nombres de columnas.

astype(): convierte tipos de datos.

query(): filtra registros mediante expresiones.

merge(): une DataFrames mediante una columna relacionada.

concat(): concatena DataFrames.

pivot_table(): genera tablas dinámicas.

groupby(): agrupa datos para realizar cálculos.

# Reporte

reporte_final.xlsx contiene las hojas:

Resumen

Ventas

Clientes

Productos

# Ventajas de automatizar el proceso

Ahorro de tiempo: los cálculos y reportes se realizan automáticamente.

Menor cantidad de errores manuales: se reducen operaciones repetitivas hechas directamente en Excel.

Actualización rápida: al reemplazar los archivos de entrada por nuevos datos con la misma estructura, el análisis puede ejecutarse nuevamente.

Reproducibilidad: el mismo código permite obtener el mismo proceso de análisis cada vez.

# Posible riesgo

Si los archivos de entrada contienen datos incorrectos, incompletos o con formatos inesperados, el programa puede producir resultados incorrectos o presentar errores. Por esta razón el proyecto incluye validaciones y conversiones básicas de tipos.

# Nota sobre las rutas

No se utilizan rutas como:

C:/Users/MATEO/...

La aplicación usa rutas relativas calculadas con Path(__file__), por lo que el proyecto puede copiarse a otra carpeta sin tener que modificar analisis.py.

# Conclusión

La implementación de Python y Pandas permitió automatizar el análisis de datos empresariales, facilitando la carga, exploración, transformación y generación de reportes. Este proceso reduce el trabajo manual, mejora la organización de la información y permite obtener resultados de manera más rápida y reproducible.