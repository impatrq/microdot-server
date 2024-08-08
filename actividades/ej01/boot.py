# Configuracion inicial
def do_connect ():
    import network
    from time import sleep
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect("Cooperadora Alumnos", "")
        while not sta_if.isconnected():
            print(".", end="")
            sleep(.25)
    print("Network config:", sta_if.ifconfig())
    
do_connect()