from pathlib import Path
import pandas as pd


# ============================================================
# SISTEMA DE ANÁLISIS EMPRESARIAL CON PANDAS
# SENA - ADSO - Sesión 4
#
# Las rutas se construyen con pathlib a partir de la ubicación
# de este archivo, por lo que el programa funciona aunque el
# proyecto sea movido a otra carpeta o a otro equipo.
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

CLIENTES_FILE = DATA_DIR / "clientes(1).csv"
PRODUCTOS_FILE = DATA_DIR / "productos.xlsx"
VENTAS_FILE = DATA_DIR / "ventas(3).csv"
REPORTE_FILE = REPORTS_DIR / "reporte_final.xlsx"


def validar_archivos():
    """Verifica que los archivos de entrada existan."""
    archivos = [CLIENTES_FILE, PRODUCTOS_FILE, VENTAS_FILE]
    faltantes = [archivo for archivo in archivos if not archivo.exists()]

    if faltantes:
        print("ERROR: faltan los siguientes archivos:")
        for archivo in faltantes:
            print(f" - {archivo}")
        raise FileNotFoundError(
            "No se encontraron todos los archivos de entrada. "
            "Verifique la carpeta data."
        )


def cargar_datos():
    """Carga clientes, productos y ventas."""
    clientes = pd.read_csv(CLIENTES_FILE)
    productos = pd.read_excel(PRODUCTOS_FILE, sheet_name="Productos")
    ventas = pd.read_csv(VENTAS_FILE)

    # Conversión explícita de tipos.
    ventas["Fecha"] = pd.to_datetime(ventas["Fecha"], errors="coerce")
    ventas["Cantidad"] = pd.to_numeric(ventas["Cantidad"], errors="coerce")
    ventas["Precio"] = pd.to_numeric(ventas["Precio"], errors="coerce")

    return clientes, productos, ventas


def explorar_dataframe(nombre, df):
    """Muestra información general del DataFrame."""
    print("\n" + "=" * 70)
    print(f"EXPLORACIÓN: {nombre}")
    print("=" * 70)

    print(f"Cantidad de registros: {df.shape[0]}")
    print(f"Número de columnas: {df.shape[1]}")
    print(f"Nombres de columnas: {list(df.columns)}")
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nPrimeros 5 registros:")
    print(df.head())
    print("\nÚltimos 5 registros:")
    print(df.tail())
    print("\nValores nulos por columna:")
    print(df.isnull().sum())


def validar_datos(clientes, productos, ventas):
    """Valida cantidades mínimas y datos esenciales."""
    print("\n" + "=" * 70)
    print("VALIDACIÓN DE DATOS")
    print("=" * 70)

    validaciones = [
        ("Clientes", len(clientes), 30),
        ("Productos", len(productos), 20),
        ("Ventas", len(ventas), 100),
    ]

    for nombre, cantidad, minimo in validaciones:
        estado = "OK" if cantidad >= minimo else "NO CUMPLE"
        print(f"{nombre}: {cantidad} registros -> mínimo {minimo}: {estado}")

    print("\nValores nulos:")
    print("Clientes:", int(clientes.isnull().sum().sum()))
    print("Productos:", int(productos.isnull().sum().sum()))
    print("Ventas:", int(ventas.isnull().sum().sum()))


def preparar_ventas(clientes, productos, ventas):
    """Agrega datos relacionados y calcula el valor de cada venta."""
    ventas = ventas.copy()

    # merge(): relaciona ventas con clientes.
    ventas = ventas.merge(
        clientes[["IDCliente", "Nombre", "Ciudad"]],
        on="IDCliente",
        how="left"
    )

    # rename(): mejora los nombres para el reporte.
    ventas = ventas.rename(columns={
        "Nombre": "Cliente",
        "Ciudad": "CiudadCliente"
    })

    # astype(): garantiza que las columnas de identificación sean texto.
    ventas["IDCliente"] = ventas["IDCliente"].astype(str)
    ventas["IDProducto"] = ventas["IDProducto"].astype(str)

    # Cálculo solicitado en el análisis.
    ventas["Total"] = ventas["Cantidad"] * ventas["Precio"]

    return ventas

def analizar_ventas(ventas):
    """Calcula los indicadores principales de ventas."""
    total = ventas["Total"].sum()
    promedio = ventas["Total"].mean()
    maxima = ventas["Total"].max()
    minima = ventas["Total"].min()
    transacciones = ventas["IDVenta"].nunique()

    resumen = {
        "Total de ventas": total,
        "Promedio por venta": promedio,
        "Venta máxima": maxima,
        "Venta mínima": minima,
        "Número de transacciones": transacciones,
    }

    return resumen


def analizar_clientes(clientes, ventas):
    """Analiza compras y comportamiento de clientes."""
    compras = ventas.groupby(["IDCliente", "Cliente", "CiudadCliente"]).agg(
        NumeroCompras=("IDVenta", "count"),
        DineroGastado=("Total", "sum"),
        PromedioCompra=("Total", "mean")
    ).reset_index()

    # Cliente con mayor número de compras.
    mayor_numero_compras = compras.loc[compras["NumeroCompras"].idxmax()]

    # Cliente que más dinero ha gastado.
    mayor_gasto = compras.loc[compras["DineroGastado"].idxmax()]

    # Ciudad con mayor cantidad de clientes.
    ciudad_clientes = (
        clientes.groupby("Ciudad")
        .size()
        .reset_index(name="CantidadClientes")
        .sort_values("CantidadClientes", ascending=False)
    )
    ciudad_mayor_clientes = ciudad_clientes.iloc[0]

    return compras, mayor_numero_compras, mayor_gasto, ciudad_mayor_clientes


def analizar_productos(productos, ventas):
    """Analiza unidades e ingresos por producto."""
    productos_analisis = ventas.groupby(
        ["IDProducto", "Producto", "Categoria"]
    ).agg(
        UnidadesVendidas=("Cantidad", "sum"),
        IngresoTotal=("Total", "sum")
    ).reset_index()

    # concat(): se utiliza para construir una vista con los extremos.
    mas_vendido = productos_analisis.loc[
        productos_analisis["UnidadesVendidas"].idxmax()
    ]
    menos_vendido = productos_analisis.loc[
        productos_analisis["UnidadesVendidas"].idxmin()
    ]
    mayor_ingreso = productos_analisis.loc[
        productos_analisis["IngresoTotal"].idxmax()
    ]
    menor_ingreso = productos_analisis.loc[
        productos_analisis["IngresoTotal"].idxmin()
    ]

    extremos = pd.concat([
        pd.DataFrame([mas_vendido]).assign(Tipo="Más vendido"),
        pd.DataFrame([menos_vendido]).assign(Tipo="Menos vendido"),
        pd.DataFrame([mayor_ingreso]).assign(Tipo="Mayor ingreso"),
        pd.DataFrame([menor_ingreso]).assign(Tipo="Menor ingreso"),
    ], ignore_index=True)

    return productos_analisis, extremos


def demostrar_metodos_pandas(clientes, ventas):
    """
    Demostración de métodos investigados.
    Se utilizan más de cinco métodos solicitados en la actividad:
    value_counts, nunique, drop_duplicates, rename, astype,
    query, merge, concat, pivot_table y groupby.
    """
    print("\n" + "=" * 70)
    print("MÉTODOS DE PANDAS INVESTIGADOS")
    print("=" * 70)

    # value_counts(): cuenta frecuencias.
    print("\n1. value_counts() - clientes por ciudad:")
    print(clientes["Ciudad"].value_counts())

    # nunique(): cuenta valores únicos.
    print("\n2. nunique() - clientes únicos con ventas:")
    print(ventas["IDCliente"].nunique())

    # drop_duplicates(): elimina duplicados.
    clientes_unicos = clientes.drop_duplicates(subset=["IDCliente"])
    print("\n3. drop_duplicates() - registros únicos de clientes:")
    print(len(clientes_unicos))

    # rename(): cambia nombres.
    ventas_renombradas = ventas.rename(columns={"Total": "ValorVenta"})
    print("\n4. rename() - ejemplo de columna renombrada:")
    print(ventas_renombradas[["IDVenta", "ValorVenta"]].head())

    # astype(): cambia tipo.
    ventas_tipos = ventas.copy()
    ventas_tipos["IDCliente"] = ventas_tipos["IDCliente"].astype(str)
    print("\n5. astype() - tipo de IDCliente:")
    print(ventas_tipos["IDCliente"].dtype)

    # query(): filtra usando una expresión.
    ventas_altas = ventas.query("Total > 1000000")
    print("\n6. query() - ventas superiores a $1.000.000:")
    print(ventas_altas[["IDVenta", "Producto", "Total"]].head())

    # merge(): ya fue utilizado para unir ventas y clientes.
    print("\n7. merge() - ventas relacionadas con clientes: realizado.")

    # concat(): ya fue utilizado para consolidar extremos de productos.
    print("8. concat() - extremos de productos: realizado.")

    # pivot_table(): tabla dinámica.
    tabla_pivote = pd.pivot_table(
        ventas,
        values="Total",
        index="CiudadCliente",
        columns="Categoria",
        aggfunc="sum",
        fill_value=0
    )
    print("\n9. pivot_table() - ventas por ciudad y categoría:")
    print(tabla_pivote)

    # groupby(): agrupación.
    ventas_ciudad = ventas.groupby("CiudadCliente")["Total"].sum()
    print("\n10. groupby() - total vendido por ciudad:")
    print(ventas_ciudad.sort_values(ascending=False))


def generar_reporte(resumen, ventas, compras_clientes, productos_analisis):
    """Genera reporte_final.xlsx con las cuatro hojas requeridas."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    resumen_df = pd.DataFrame(
        list(resumen.items()),
        columns=["Indicador", "Valor"]
    )

    with pd.ExcelWriter(REPORTE_FILE, engine="openpyxl") as writer:
        resumen_df.to_excel(writer, sheet_name="Resumen", index=False)
        ventas.to_excel(writer, sheet_name="Ventas", index=False)
        compras_clientes.to_excel(writer, sheet_name="Clientes", index=False)
        productos_analisis.to_excel(writer, sheet_name="Productos", index=False)

    print(f"\nReporte generado correctamente en:\n{REPORTE_FILE}")


def main():
    print("=" * 70)
    print("SISTEMA DE ANÁLISIS EMPRESARIAL CON PANDAS")
    print("=" * 70)

    validar_archivos()
    clientes, productos, ventas = cargar_datos()

    print("\nArchivos cargados correctamente.")

    # Exploración de los tres DataFrames.
    explorar_dataframe("CLIENTES", clientes)
    explorar_dataframe("PRODUCTOS", productos)
    explorar_dataframe("VENTAS", ventas)

    validar_datos(clientes, productos, ventas)

    # Preparar datos de ventas.
    ventas = preparar_ventas(clientes, productos, ventas)

    # Series: se crea una Series con el total de ventas.
    serie_ventas = pd.Series(ventas["Total"], name="Ventas")
    print("\n" + "=" * 70)
    print("SERIES DE VENTAS")
    print("=" * 70)
    print(serie_ventas.head())
    print(f"Promedio: ${serie_ventas.mean():,.0f}")
    print(f"Máxima: ${serie_ventas.max():,.0f}")
    print(f"Mínima: ${serie_ventas.min():,.0f}")

    # Análisis principal.
    resumen = analizar_ventas(ventas)
    compras_clientes, mayor_numero_compras, mayor_gasto, ciudad_mayor_clientes = \
        analizar_clientes(clientes, ventas)
    productos_analisis, extremos_productos = analizar_productos(productos, ventas)

    print("\n" + "=" * 70)
    print("ANÁLISIS DE VENTAS")
    print("=" * 70)
    for indicador, valor in resumen.items():
        if isinstance(valor, (int, float)) and "transacciones" not in indicador.lower():
            print(f"{indicador}: ${valor:,.0f}")
        else:
            print(f"{indicador}: {valor}")

    print("\n" + "=" * 70)
    print("ANÁLISIS DE CLIENTES")
    print("=" * 70)
    print(
        f"Cliente con más compras: {mayor_numero_compras['Cliente']} "
        f"({int(mayor_numero_compras['NumeroCompras'])} compras)"
    )
    print(
        f"Cliente que más dinero gastó: {mayor_gasto['Cliente']} "
        f"(${mayor_gasto['DineroGastado']:,.0f})"
    )
    print(
        f"Ciudad con mayor número de clientes: {ciudad_mayor_clientes['Ciudad']} "
        f"({int(ciudad_mayor_clientes['CantidadClientes'])} clientes)"
    )
    print(
        f"Promedio de compra del cliente con más compras: "
        f"${mayor_numero_compras['PromedioCompra']:,.0f}"
    )

    print("\n" + "=" * 70)
    print("ANÁLISIS DE PRODUCTOS")
    print("=" * 70)
    print(
        f"Producto más vendido: "
        f"{extremos_productos.loc[extremos_productos['Tipo'] == 'Más vendido', 'Producto'].iloc[0]}"
    )
    print(
        f"Producto menos vendido: "
        f"{extremos_productos.loc[extremos_productos['Tipo'] == 'Menos vendido', 'Producto'].iloc[0]}"
    )
    print(
        f"Producto con mayor ingreso: "
        f"{extremos_productos.loc[extremos_productos['Tipo'] == 'Mayor ingreso', 'Producto'].iloc[0]}"
    )
    print(
        f"Producto con menor ingreso: "
        f"{extremos_productos.loc[extremos_productos['Tipo'] == 'Menor ingreso', 'Producto'].iloc[0]}"
    )

    demostrar_metodos_pandas(clientes, ventas)

    generar_reporte(
        resumen,
        ventas,
        compras_clientes.sort_values("DineroGastado", ascending=False),
        productos_analisis.sort_values("IngresoTotal", ascending=False)
    )

    print("\nProceso finalizado sin errores.")


if __name__ == "__main__":
    main()