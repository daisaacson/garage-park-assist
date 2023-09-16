import neopixel
from machine import Pin
from time import sleep
import math

NEOPIXEL_PIN = 0
NEOPIXEL_NUMBER = 24

ZONE0_RGB = (0,0,1)                # Idle
ZONE1_RGB = (0,255,0)              # Parking attempt detected, 
ZONE2_RGB_BACKGROUND = (0,0,0)     # Progress to bar to Zone 3
ZONE2_RGB_FOREGROUND = (255,255,0) # Progress to bar to Zone 3
ZONE3_RGB = (255,0,0)		       # Stop point reach
ZONE4_RGB = (255,255,255)	       # Stop point exceeded, flash this color with ZONE3_RGB

neopixel = neopixel.NeoPixel(machine.Pin(NEOPIXEL_PIN),NEOPIXEL_NUMBER)

while True:
    neopixel.fill(ZONE1_RGB)
    neopixel.write()
    sleep(1)
    for i in range (0,101):
        try:
            partially_lit_pixel_percent,fully_lit_pixels = math.modf(i/100*(NEOPIXEL_NUMBER/2))
            print (i, ": ", fully_lit_pixels, " | ", partially_lit_pixel_percent)
            
            neopixel.fill(ZONE2_RGB_BACKGROUND)
            for pixel_index in range (0,fully_lit_pixels):
                neopixel[pixel_index] = ZONE2_RGB_FOREGROUND
                neopixel[NEOPIXEL_NUMBER-pixel_index-1] = ZONE2_RGB_FOREGROUND
            if partially_lit_pixel_percent != 0:
                R,G,B = ZONE2_RGB_FOREGROUND
                ZONE2_RGB_FOREGROUND_PARTIALLY_LIT = (int(R * partially_lit_pixel_percent),
                                                      int(G * partially_lit_pixel_percent),
                                                      int(B * partially_lit_pixel_percent))
                neopixel[int(fully_lit_pixels)] = ZONE2_RGB_FOREGROUND_PARTIALLY_LIT
                neopixel[int(NEOPIXEL_NUMBER-fully_lit_pixels)-1] = ZONE2_RGB_FOREGROUND_PARTIALLY_LIT
            neopixel.write()
            sleep(.01)
        except KeyboardInterrupt as e:
            neopixel.fill(ZONE0_RGB)
            neopixel.write()
            machine.soft_reset()
    neopixel.fill(ZONE3_RGB)
    neopixel.write()
    sleep(1)
    for i in range (101,-1,-1):
        try:
            partially_lit_pixel_percent,fully_lit_pixels = math.modf(i/100*(NEOPIXEL_NUMBER/2))
            print (i, ": ", fully_lit_pixels, " | ", partially_lit_pixel_percent)
            
            neopixel.fill(ZONE2_RGB_BACKGROUND)
            for pixel_index in range (0,fully_lit_pixels):
                neopixel[pixel_index] = ZONE2_RGB_FOREGROUND
                neopixel[NEOPIXEL_NUMBER-pixel_index-1] = ZONE2_RGB_FOREGROUND
            if partially_lit_pixel_percent != 0:
                R,G,B = ZONE2_RGB_FOREGROUND
                ZONE2_RGB_FOREGROUND_PARTIALLY_LIT = (int(R * partially_lit_pixel_percent),
                                                      int(G * partially_lit_pixel_percent),
                                                      int(B * partially_lit_pixel_percent))
                neopixel[int(fully_lit_pixels)] = ZONE2_RGB_FOREGROUND_PARTIALLY_LIT
                neopixel[int(NEOPIXEL_NUMBER-fully_lit_pixels)-1] = ZONE2_RGB_FOREGROUND_PARTIALLY_LIT
            neopixel.write()
            sleep(.01)
        except KeyboardInterrupt as e:
            neopixel.fill(ZONE0_RGB)
            neopixel.write()
            machine.soft_reset()
    sleep(1)
