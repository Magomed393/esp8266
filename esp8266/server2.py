
from micro import MicroPyServer
import esp
import network
from machine import Pin

wlan_id = "Sergeev"
wlan_pass = "25051991"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if wlan.isconnected() == False:
    wlan.connect(wlan_id, wlan_pass)
    while wlan.isconnected() == False:
        time.sleep(1)
print('Device IP:', wlan.ifconfig()[0])

def show_message(request):
    ''' request handler '''
    server.send("HELLO WORLD!")

def do_on(request):
    ''' on request handler '''
    led.value(0)
    server.send("ON")

def do_off(request):
    ''' off request handler '''
    led.value(1)
    server.send("OFF")

led = Pin(2,Pin.OUT)

server = MicroPyServer()
''' add request handler '''
server.add_route("/", show_message)
server.add_route("/on", do_on)
server.add_route("/off", do_off)

''' start server '''
server.start()