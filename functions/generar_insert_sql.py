def generar_insert_sql(genero, edad, estado_salud, sintoma_principal, tiempo_evolucion):
    """
    Genera una consulta SQL INSERT para almacenar los datos de la entrevista.
    """
    def escape_sql(value):
        return value.replace("'", "''") if isinstance(value, str) else value

    genero = escape_sql(genero)
    edad = escape_sql(edad)
    estado_salud = escape_sql(estado_salud)
    sintoma_principal = escape_sql(sintoma_principal)
    tiempo_evolucion = escape_sql(tiempo_evolucion)

    sql = f"""
    INSERT INTO entrevistas (genero, edad, estado_salud, sintoma_principal, tiempo_evolucion)
    VALUES ('{genero}', '{edad}', '{estado_salud}', '{sintoma_principal}', '{tiempo_evolucion}');
    """
    return sql.strip()
