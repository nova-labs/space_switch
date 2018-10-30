Nova Labs Space Switch
======================

## SYNOPSIS
`python3 ./main.py`

## Description

Space Switch handles the hardware space switch and updating the state in the Nova Labs Event Service.  Toggling the
physical switch updates the Event Service and changes the physical LEDs.  The LEDs indicate the
current state, and transitions.

## Indicator LEDs

|Left LEDs|Right LEDs|State|
|:-------:|:--------:|:----|
| RED    | RED    |CLOSED|
| ORANGE | ORANGE |ASSOCIATE  |
| GREEN  | GREEN  |OPEN  |
| GREY   | GREY   |BOOT  |
| ANY    | GREY   |Switch changed, updating Event Service |
| GREEN  | DARK RED |Changing to CLOSED, Event Service updated, pulling from Event Service |
| ORANGE | DARK ORANGE |Changing to ASSOCIATE, Event Service updated, pulling from Event Service |
| RED    | DARK GREEN |Changing to OPEN, Event Service updated, pulling from Event Service |
| ANY    | YELLOW  |Error connecting to Event Service |

## Configuration

The script runs as root, since it needs write access to /dev/mem.  Clone the repository into /root/space_switch.

Configure Event Service URL, in main.py.  This is the base URL of the service.
```bash
EVENT_SERVICE_BASE_URL="https://event.nova-labs.org"
```

Install and enable init script.  This will start/stop on boot.
```bash
cp init.d/space_switch /etc/init.d
systemctl enable space_switch
```

Manually start/stop.
```bash
systemctl start space_switch
systemctl stop space_switch
```


## State Transition Details
### Boot
1. Script starts
2. Initializes hardware
3. LEDs changed to boot color (grey)
4. Switch position read
5. Update state

### Switch change
1. Switch position changed, value read (OPEN/CLOSED)
2. Update state

### Update state
1. Right LEDs changed to "state changing" color (grey)
3. Event with new state added to Event Service (RESTful POST call)
4. Right LEDs changed with "state changed" color
    * Dark Green - successfully updated Event Service to OPEN
    * Dark Orange - successfully updated Event Service to ASSOCIATE
    * Dark Red - successfully updated Event Service to CLOSED
    * Yellow - error communicating with Event Service
5. Latest event fetched from Event Service (RESTful GET call)
6. All LEDs changed to current state color
    * Red - CLOSED
    * Orange - Associate
    * Green - OPEN
    
## Dependencies
* python >= 3.0
* python modules
    * json
    * logging
    * math
    * requests
    * requests
    * signal
    * sys
    * time
    * RPi.GPIO - install via pip3
    * adafruit-circuitpython-neopixel - install via pip3
    * rpi_ws281x

### NeoPixel library ([rpi_ws281x](https://github.com/jgarff/rpi_ws281x))
The NeoPixel library controls the LEDs.

### RPi.GPIO library ([RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/))
The RPi.GPIO library reads the switch position using the GPIO pin outs.

### Adafruit CircuitPython Neopixel library ([adafruit-circuitpython-neopixel](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel))
The CircuitPython library is now the preferred setup for accessing neopixels
