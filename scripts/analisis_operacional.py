import pandas as pd
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
    df = pd.read_excel("data\\dataset_set_D_telecomunicaciones.xlsx")
    # Explorar dataset
    explorar_dataset(df)
    # Generar salidas
    df_soporte = filtro_soporte_tecnico(df)
    df_soporte.to_excel("outputs\\soporte_tecnico.xlsx", index=False)
    df_clientes = filtro_experiencia_clientes(df)
    df_clientes.to_excel("outputs\\experiencia_clientes.xlsx", index=False)
    return df_soporte, df_clientes

if __name__ == "__main__":
    main()