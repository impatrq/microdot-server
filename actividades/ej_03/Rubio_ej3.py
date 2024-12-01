# Servidor de la aplicación
from boot import do_connect
from microdot import Microdot, send_file
from machine import Pin, ADC
import ds18x20, onewire, time

buzzer_pin = Pin(14, Pin.OUT)
pin_ds = Pin(19)
sensor_ds = ds18x20.DS18X20(onewire.OneWire(pin_ds))
temperaturaCelsius = 24

do_connect()
app = Microdot()

@app.route('/')
async def inicio(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def static(request, dir, file):
    return send_file("/{}/{}".format(dir, file))

@app.route('/sensors/ds18b20/read')
async def medir_temperatura(request):
    global sensor_ds
    sensor_ds.convert_temp()
    time.sleep_ms(1)
    roms = sensor_ds.scan()
    for rom in roms:
        temperaturaCelsius = sensor_ds.read_temp(rom)
    
    datos_json = {'temperatura': temperaturaCelsius}
    
    return datos_json

@app.route('/setpoint/set/<int:value>')
async def ajustar_setpoint(request, valor):
    datos_json = {}
    print("Ajustando setpoint")
    if valor >= temperaturaCelsius:
        buzzer_pin.on()
        datos_json = {'buzzer': 'Encendido'}
    else:
        buzzer_pin.off()
        datos_json = {'buzzer': 'Apagado'}
    
    return datos_json

app.run(port=80)