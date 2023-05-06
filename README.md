# Garage Parking Assistant

## Shopping List

Based on items available at [Mirco Center](https://www.microcenter.com "Micro Center's Homepage")

| Item | Description | Chip | Cost
| --- | --- | --- | --- |
| [Raspbery Pi Pico](https://www.microcenter.com/product/661033/raspberry-pi-pico-microcontroller-development-board) | micro controller | RP2040 | $3.99 |
| [Neo Pixel 24 LED ring](https://www.microcenter.com/product/655088/adafruit-industries-neopixel-ring-24-x-5050-rgb-led) | LEDs | WS2812 5050 | $16.95 |
| [Inland ultrasonic 3x](https://www.microcenter.com/product/613881/inland-hr-sr04-blue-ultrasonic-module-3-pack) | ultra sonic sensor | HR-SR04 | $7.99 |

## Requirements

 - https://github.com/rsc1975/micropython-hcsr04


## PINS

1. GP0: WS2812: DIN
6. GP4: HC-SR04: Trig (I2C0 SDA)
7. GP5: HC-SR04: Echo (I2C0 SCL)
11. GP8: eInk: D/C (SPI1 RX)
12. GP9: eInk: CS  (SPI1 CSn)
14. GP10: eInk: CLK  (SPI1 SCK)
15. GP11: eInk: SDI (SPI1 TX) 
16. GP12: eInk: RES
17. GP13: eInk: BUSY
40. VBUS - power other devices
38. Ground


## Inspiration Videos

https://youtu.be/HqqlY4_3kQ8

 - 1st video I saw
 - I liked the representation of parking zones on the LED light bar
 - Will likely skip the IoT aspects

https://youtu.be/pScwL8NoMn4

 - I like the push button knob and OLED display
