from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Variables para almacenar el setpoint de temperatura y el estado del buzzer
setpoint = 15.0
buzzer_status = False

# Simulación de la lectura de temperatura desde un sensor
def leer_temp_real():
    # Aquí deberías leer la temperatura real desde tu sensor
    # Para este ejemplo, vamos a simularlo con un valor aleatorio
    return round(random.uniform(0, 30), 1)

# Ruta para actualizar el setpoint
@app.route('/update_setpoint')
def update_setpoint():
    global setpoint
    valor = request.args.get('value', default=15.0, type=float)
    setpoint = valor
    return jsonify({"setpoint": setpoint})

# Ruta para obtener la temperatura real y el estado del buzzer
@app.route('/get_temp_real')
def get_temp_real():
    global buzzer_status
    temp_real = leer_temp_real()
    buzzer_status = temp_real > setpoint
    return jsonify({"temp_real": temp_real, "buzzer_status": buzzer_status})

# Ejecución de la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
