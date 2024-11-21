# Aplicacion del servidor
from boot import do_connect
from microdot import Microdot, send_file
from machine import Pin
from machine import ADC
import ds18x20
import onewire
import time

buzzer_pin = Pin(14, Pin.OUT)
ds_pin = Pin(19)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
temperatureCelsius = 24

do_connect()
app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def static(request, dir, file):
    return send_file("/{}/{}".format(dir, file))

@app.route('/sensors/ds18b20/read')
async def temperature_measuring(request):
    global ds_sensor
    ds_sensor.convert_temp()
    time.sleep_ms(1)
    roms = ds_sensor.scan()
    for rom in roms:
        temperatureCelsius = ds_sensor.read_temp(rom)
    
    json = {'temperature': temperatureCelsius};
    
    return json

@app.route('/setpoint/set/<int:value>')
async def setpoint_calculation(request, value):
    json = {}
    print("Calculate setpoint")
    if value >= temperatureCelsius:
        buzzer_pin.on()
        json = {'buzzer': 'On'}
    else:
        buzzer_pin.off()
        json = {'buzzer': 'Off'}
    
    return json

app.run(port=80)
