# microdot-server
Repositorio con información y ejercicios sobre implementaciones de servidores embebidos en Micropython con Microdot

## docs

- [Documentación de microdot](https://microdot.readthedocs.io/en/latest/)
- [Documentación del kit](https://odoo.fanlab.com.ar/web/content/2432)
- [Referencia rápida de Micropython para ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html)

## boot.py

El boot.py es un archivo especial que normalmente se ejecuta cuando el microcontrolador se reinicia. Por eso, es un buen lugar para hacer la inicialización de periféricos que vayamos a usar o incluso, establecer la conexión a internet.

Esto último es posible con una función como la siguiente:

```python
def connect_to(ssid : str, passwd : str) -> None:
    """Conecta el microcontrolador a la red indicada.

    Parameters
    ----------
    ssid : str
        Nombre de la red a conectarse
    passwd : str
        Contraseña de la red
    """
    
    import network
    from time import sleep
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, passwd)
        while not sta_if.isconnected():
            print(".",end="")
            sleep(.05)
    
    print()
    print("Network config:", sta_if.ifconfig())
    print()
```

Luego, podemos llamar a la función como:

```python
connect_to("Cooperadora Alumnos", "")
```

Y veremos un mensaje como este:

```bash
Network config: ('192.168.126.254', '255.255.252.0', '192.168.124.1', '200.51.211.7')
```

Donde el primer elemento de la tupla es la IP que se asignó al microcontrolador y que vamos a usar para conectarnos con el navegador.