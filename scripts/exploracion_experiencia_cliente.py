import pandas as pd
from analisis_operacional import explorar_dataset
# Cargar Excel salida de Experiencia de Clientes
def explorar_cliente():
    df = pd.read_excel("outputs\\experiencia_clientes.xlsx")
    explorar_dataset(df)
def carga_cliente():
    df = pd.read_excel("outputs\\experiencia_clientes.xlsx")