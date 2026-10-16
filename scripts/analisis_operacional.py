import pandas as pd
from modulo.Joblib_utilidad import guardar_resultados, cargar_resultados
from modulo.NumPy_utilidad import promedio_latencia, desviacion_latencia
from modulo.SciPy_utilidad import prueba_diferencia_latencia, correlacion_latencia_clientes

# Explorar dataset
def explorar_dataset(df):
    print("Consulta de metadatos")
    print(df.info())
    print("Obtener estadísticas descriptivas")
    print(df.describe())
    print("Visualizar primeras filas de DataFrame")
    print(df.head())
    print("Revisar nombre de columnas")
    print(df.columns)
    print("Mostrar valores faltantes")
    print(df.isnull().sum())

# Área de Soporte Técnico
def filtro_soporte_tecnico(df):
    # Filtrar columnas relevantes para Soporte Técnico
    soporte_cols = [
        "fecha_registro",
        "region",
        "tipo_servicio",
        "incidencias_reportadas",
        "tickets_soporte",
        "tiempo_resolucion_hr"
    ]
    return df[soporte_cols]

# Área de Experiencia de Clientes
def filtro_experiencia_clientes(df):
    # Filtrar columnas relevantes para Experiencia de Clientes
    clientes_cols = [
        "fecha_registro",
        "tipo_servicio",
        "clientes_afectados",
        "latencia_ms",
        "cumplimiento_sla"
    ]
    return df[clientes_cols]

def main():
    # Cargar dataset
    df = pd.read_excel("data/dataset_set_D_telecomunicaciones.xlsx")
    # Explorar dataset
    explorar_dataset(df)
    # Generar salidas
    df_soporte = filtro_soporte_tecnico(df)
    df_soporte.to_excel("outputs/soporte_tecnico.xlsx", index=False)
    df_clientes = filtro_experiencia_clientes(df)
    df_clientes.to_excel("outputs/experiencia_clientes.xlsx", index=False)
    # Funciones de modulos utilizables:
    # Numpy
    # latencias = df_clientes["latencia_ms"].dropna().values
    # print("Promedio latencia:", promedio_latencia(latencias))
    # print("Desviación estándar:", desviacion_latencia(latencias))

    # Selección de servicios para comparar con SciPy
    # internet_hogar = df_clientes[df_clientes["tipo_servicio"] == "Internet Hogar"]["latencia_ms"].dropna()
    # movil = df_clientes[df_clientes["tipo_servicio"] == "Móvil"]["latencia_ms"].dropna()
    # empresa = df_clientes[df_clientes["tipo_servicio"] == "Empresas"]["latencia_ms"].dropna()
    # Seleccion de ejemplo: internet hogar y movil 
    # resultado_ttest = prueba_diferencia_latencia(internet_hogar, movil)
    # print("Prueba diferencia Internet Hogar vs Móvil:")
    # print("t-stat:", resultado_ttest.statistic, "p-value:", resultado_ttest.pvalue)

    # Correlación latencia vs clientes afectados
    # resultado_corr = correlacion_latencia_clientes(df_clientes["latencia_ms"].dropna(),
    # df_clientes["clientes_afectados"].dropna())
    # print("Correlación latencia-clientes:", resultado_corr)

    # Joblib: guardar y cargar resultados
    # guardar_resultados(df_clientes, "outputs/df_clientes.pkl")
    # df_clientes_cargado = cargar_resultados("outputs/df_clientes.pkl")
    # print("Clientes cargados desde Joblib:", df_clientes_cargado.shape)

    return df_soporte, df_clientes
if __name__ == "__main__":
    main()
