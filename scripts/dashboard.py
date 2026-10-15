import plotly.express as px
from analisis_operacional import main as analisis_main

# Funcion Barra
def desempeno_region_servicio(df_soporte):
    dash = df_soporte.groupby(["region", "tipo_servicio"])["incidencias_reportadas"].sum().reset_index()
    fig = px.bar(dash,
                 x="region",
                 y="incidencias_reportadas",
                 color="tipo_servicio",
                 barmode="group",
                 title="Comparación de desempeño por región y tipo de servicio",
                 labels={
            "region": "Región",
            "tipo_servicio": "Tipo de Servicio",
            "incidencias_reportadas": "Incidencias Reportadas"
        })
    fig.show()
# Iniciar funcion Barra
def main():
    df_soporte, _ = analisis_main()
    desempeno_region_servicio(df_soporte)
if __name__ == "__main__":
    main()