from scipy import stats

def prueba_diferencia_latencia(servicio_a, servicio_b):
    # t-test para comparar latencias entre dos servicios
    return stats.ttest_ind(servicio_a, servicio_b)
# Relacion entre latencia y clientes afectados
def correlacion_latencia_clientes(latencias, clientes_afectados):
    return stats.pearsonr(latencias, clientes_afectados)