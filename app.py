from flask import Flask, request, jsonify
from assistant import get_assistant_answer
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Ruta principal para verificar que el servidor está funcionando
@app.route('/', methods=['GET'])
def home():
    return "Entrevistador Médico AI está funcionando correctamente."

# Ruta para manejar las solicitudes de generación de consultas SQL
@app.route('/generar_insert_sql', methods=['POST'])
def generar_insert_sql():
    data = request.json
    required_fields = ["genero", "edad", "estado_salud", "sintoma_principal", "tiempo_evolucion"]

    # Verificar que todos los campos requeridos estén presentes
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Falta el campo '{field}'"}), 400

    # Extraer los datos del usuario
    genero = data['genero']
    edad = data['edad']
    estado_salud = data['estado_salud']
    sintoma_principal = data['sintoma_principal']
    tiempo_evolucion = data['tiempo_evolucion']

    # Llamar a la función del asistente para generar la consulta SQL
    try:
        sql = get_assistant_answer(genero, edad, estado_salud, sintoma_principal, tiempo_evolucion)
        return jsonify({"sql": sql}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Obtener el puerto desde la variable de entorno o usar el puerto 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
