import config

def do_wifi_connect(ssid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def create_access_point(ssid, password):
    import network
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)
    print('network config:', ap.ifconfig())

def setup_system_lib():
    import sys
    sys.path.remove("/lib")
    sys.path.append("/lib/microdot")
    sys.path.append("/lib/pca9685")
    sys.path.append("/lib/picoweb")
    print(f"Set new sys path: {sys.path}")

if config.CREATE_AP:
    create_access_point(config.AP_SSID, config.AP_PASSWORD)
else:
    do_wifi_connect(config.WIFI_SSID, config.WIFI_PASSWORD)

setup_system_lib()