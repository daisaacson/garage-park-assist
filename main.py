from time import sleep
from hcsr04.hcsr04 import HCSR04

# GPIO PINs
HCSR04_TRIGGER = 4
HCSR04_ECHO = 5

sensor = HCSR04(trigger_pin=HCSR04_TRIGGER, echo_pin=HCSR04_ECHO)

while True:
    try:
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm')
    except OSError as ex:
        print('ERROR getting distance:', ex)
    sleep(0.1)
