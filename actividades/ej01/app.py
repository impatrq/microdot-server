# Aplicacion del servidor
from microdot import Microdot
from microdot import send_file

app = Microdot()

@app.route('/')
async def index(request):
    return send_file("index.html")

@app.route('/<dir>/<file>')
async def static (request,dir,file):
    return send_file('/' + dir + '/' + file)

app.run(port = 80)
