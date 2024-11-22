# assistant.py

from functions.generar_insert_sql import generar_insert_sql

def get_assistant_answer(genero, edad, estado_salud, sintoma_principal, tiempo_evolucion):
    """
    Genera una consulta SQL INSERT para almacenar los datos de la entrevista.
    """
    sql = generar_insert_sql(genero, edad, estado_salud, sintoma_principal, tiempo_evolucion)
    return sql
