import pandas as pd
from analisis_operacional import explorar_dataset
# Cargar Excel salida de Soporte Técnico
def explorar_tecnico():
    df = pd.read_excel("outputs\\soporte_tecnico.xlsx")
    explorar_dataset(df)
def carga_tecnico():
    df = pd.read_excel("outputs\\soporte_tecnico.xlsx")