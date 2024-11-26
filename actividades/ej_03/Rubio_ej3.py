import network
import socket
import json
import machine
from time import sleep
import _thread

# Configuración de pines y sensor de temperatura
buzzer_pin = machine.Pin(15, machine.Pin.OUT)
temp_sensor = machine.ADC(machine.Pin(32))
temp_sensor.atten(machine.ADC.ATTN_11DB)

# Variable global para el setpoint
setpoint_temperature = 0

def start_server():
    # Configurar dirección del servidor
    server_address = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    server_socket = socket.socket()
    server_socket.bind(server_address)
    server_socket.listen(1)

    print('Servidor escuchando en', server_address)

    while True:
        client_socket, client_address = server_socket.accept()
        print('Cliente conectado desde', client_address)
        request_data = client_socket.recv(1024)
        request_str = str(request_data)
        
        if "GET /temperature" in request_str:
            # Leer y responder con la temperatura actual
            current_temperature = (temp_sensor.read() / 4095) * 100
            response = json.dumps({"temperature": current_temperature})
            client_socket.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n' + response)

        elif "POST /setpoint" in request_str:
            # Actualizar setpoint a partir de la solicitud
            start_index = request_str.find('setpoint=') + len('setpoint=')
            end_index = request_str.find(' ', start_index)
            global setpoint_temperature
            setpoint_temperature = int(request_str[start_index:end_index])
            client_socket.send('HTTP/1.1 200 OK\r\n\r\n')
        
        elif "GET /buzzer" in request_str:
            # Responder con el estado actual del buzzer
            buzzer_status = json.dumps({"buzzer_state": buzzer_pin.value()})
            client_socket.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n' + buzzer_status)

        elif "GET /" in request_str or "GET /index.html" in request_str:
            # Enviar contenido HTML de la página principal
            with open("index.html", "r") as file:
                html_content = file.read()
            client_socket.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + html_content)
        
        client_socket.close()

def monitor_temperature():
    global setpoint_temperature
    while True:
        current_temperature = (temp_sensor.read() / 4095) * 100
        if current_temperature > setpoint_temperature:
            buzzer_pin.value(1)
        else:
            buzzer_pin.value(0)
        sleep(1)

# Iniciar el monitoreo de la temperatura en un hilo separado
_thread.start_new_thread(monitor_temperature, ())

# Iniciar el servidor web
start_server()