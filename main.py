
import network, socket, time
from machine import Pin
import neopixel

SWITCH_GPIO = 15

PIXEL_GPIO = 4
PIXEL_COUNT = 12

NOTIFY_URL = "http://lumisense.com/nova-labs/status/SetStatus.php?switch=%d&author=spaceswitch"

def novalabs_connect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    #sta_if.scan()                          # Scan for available access points
    while not sta_if.isconnected():
        sta_if.connect("Nova Labs", "robots4u") # Connect to an AP
    print("Connected to wifi")


def shine_all(color):
    print("shining color %s" % repr(color))
    for i in range(PIXEL_COUNT):
        np[i] = color
    np.write()

def shine_green(): shine_all((0, 255, 0))
def shine_red():   shine_all((255, 0, 0))
def shine_off():   shine_all((0, 0, 0))


def update_leds(sw_on):
    if sw_on: shine_green()
    else: shine_red()


def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if not data: break
        #print(str(data, 'utf8'), end='')


def notify_switch_changed(newstate):
    print("Connecting to wifi...")
    novalabs_connect()
    print("Notifying server of new state")
    http_get(NOTIFY_URL % newstate)
    print("Notified server of new state")


def switch_changed(sw_on):
    shine_off()
    notify_switch_changed(sw_on)
    update_leds(sw_on)


np = neopixel.NeoPixel(Pin(PIXEL_GPIO), PIXEL_COUNT)
print("set up %d neopixels on GPIO %d" % (PIXEL_COUNT, PIXEL_GPIO))

switch = Pin(SWITCH_GPIO, Pin.IN, pull=Pin.PULL_UP)
#switch.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING, handler=notify_switch_changed)
print("set up switch on GPIO %d" % (SWITCH_GPIO))

old = switch.value()
update_leds(old)

print("Initial value is %d" % old)
while True:
    cur = switch.value()
    if old == cur:
        time.sleep_ms(100)
        continue
    old = cur
    print("New value is %d" % old)
    switch_changed(cur)

