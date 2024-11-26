def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('CONECTANDO')
        sta_if.active(True)
        sta_if.connect('Cooperadora Alumnos', '')
        while not sta_if.isconnected():
            print(".", end="")
            sleep(.25)
    print('network config:', sta_if.ifconfig())

do_connect()