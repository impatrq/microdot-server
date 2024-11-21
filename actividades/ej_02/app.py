# Aplicacion del servidor
# Aplicacion del servidor
from boot import do_connect
from microdot import Microdot, send_file
from machine import Pin
import neopixel

led_pin1 = Pin(32, Pin.OUT, value=0)
led_pin2 = Pin(33, Pin.OUT, value=0)
led_pin3 = Pin(25, Pin.OUT, value=0)

np = neopixel.NeoPixel(Pin(27), 4)
for i in range(4):
    np[i] = (0, 0, 0)

np.write()

do_connect()
app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def static(request, dir, file):
    return send_file("/{}/{}".format(dir, file))

@app.route('/led/toggle/<led>')
async def led_toggle(request, led):
    global led_pin1, led_pin2, led_pin3
    
    if led == 'LED1':
        led_pin1.value(not led_pin1.value())
    elif led == 'LED2':
        led_pin2.value(not led_pin2.value())
    elif led == 'LED3':
        led_pin3.value(not led_pin3.value())
        
    return {"status":"OK"}

@app.route('/rgbled/change/red/<int:red>')
async def rgb_led(request, red):
    global np
    green = np[0][1]
    blue = np[0][2]
    
    for pixel in range(4):
        np[pixel] = (red, green, blue)
        
    np.write()
    
@app.route('/rgbled/change/blue/<int:blue>')
async def rgb_led(request, blue):
    global np
    
    red = np[0][0]
    green = np[0][1]
    
    for pixel in range(4):
        np[pixel] = (red, green, blue)
        
    np.write()
    
@app.route('/rgbled/change/green/<int:green>')
async def rgb_led(request, green):
    global np
    
    red = np[0][0]
    blue = np[0][2]
    
    for pixel in range(4):
        np[pixel] = (red, green, blue)
        
    np.write()

app.run(port=80)
