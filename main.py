from time import sleep
from hcsr04.hcsr04 import HCSR04

sensor = HCSR04(trigger_pin=4, echo_pin=5)
distance = sensor.distance_cm()

while True:
    try:
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm')
    except OSError as ex:
        print('ERROR getting distance:', ex)
    sleep(0.1)
