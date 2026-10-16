import joblib
def guardar_resultados(objeto, ruta):
    joblib.dump(objeto, ruta)
def cargar_resultados(ruta):
    return joblib.load(ruta)