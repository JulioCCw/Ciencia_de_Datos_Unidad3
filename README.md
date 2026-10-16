# Ciencia_de_Datos_Unidad3
## Documentación Técnica - RedConecta Telecom S.A
### Objetivo del proyecto:
- Interactuar con los datos de origen
- Separar datos por área objetivo Soporte Técnico y Experiencia de Clientes
- Visualizar un gráfico de barras de incidencias reportadas por región y tipo de servicio

### Descripción de datos
- *dataset_set_D_telecomunicaciones.xlsx* Archivo de origen con registros completos y sin filtrar.
- Variables filtradas:
  - Soporte Técnico: fecha_registro, region, tipo_servicio, incidencias_reportadas, tickets_soporte, tiempo_resolucion_hr.
  - Experiencia de Clientes: fecha_registro, tipo_servicio, clientes_afectados, latencia_ms, cumplimiento_sla.

### Metodología aplicada
1. Carga de datos: Lectura de carpeta data/ dataset_set_D_telecomunicaciones.xlsx
2. Exploración inicial: Función de exploración integrada en main() del script analisis_operacional.py para revisión de datos.
3. Proceso de filtrado: Función de filtrado integrado en main() para exportación de Excel con destino a outputs/
4. Análisis de datos: Función de visualización por medio de dashboard utilizando plotly.express
5. Documentación: Actualizar README.md cada vez que se implemente una nueva función o cambio de parámetros en GitHub

### Principales resultados
- Exportación de dos archivos Excel filtrados según las variables definidas
- Visualización de dashboard

### Instrucciones de uso
1. Clonar el repositorio de GitHub
2. Ejecutar analisis_operacional.py
3. Visualizar resultados con dashboard.py

### Actualizaciones
- Se implementa carpetas de guardado para dashboards.
- Se añade notebooks sobre el proyecto.
- Integracion de modulos reutilizables en script/modulo
  - Ejemplos de uso integrados en main() de analisis_operacional.py, comentados con # para ejecucion selectiva.
