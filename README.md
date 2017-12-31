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
| RED   | RED   |CLOSED|
| GREEN | GREEN |OPEN  |
| GREY  | GREY  |BOOT  |
| ANY   | GREY  |Switch changed, updating Event Service |
| GREEN | DARK RED |Changing to CLOSED, Event Service updated, pulling from Event Service |
| RED   | DARK GREEN |Changing to OPEN, Event Service updated, pulling from Event Service |
| ANY   | YELLOW  |Error connecting to Event Service |

## Configuration

Provide code examples and explanations of how to get the project.
```bash
WIFI_SSID = "<WiFi SSID>"
WIFI_PASSWORD = "<password>"
EVENT_SERVICE_BASE_URL = "http://event_service.domain:port"
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
    * Dark Red - successfully updated Event Service to CLOSED
    * Yellow - error communicating with Event Service
5. Latest event fetched from Event Service (RESTful GET call)
6. All LEDs changed to current state color
    * Red - CLOSED
    * Green - OPEN
    
## Dependencies
* python >= 3.0
* python modules
    * json
    * math
    * network
    * requests
    * time
    * Pin
    * neopixel
