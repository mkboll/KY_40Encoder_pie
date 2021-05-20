#https://tutorials-raspberrypi.de/raspberry-pi-ky040-drehregler-lautstaerkeregler/

import RPi.GPIO as GPIO
from KY040 import KY040
import os, time


rotation = 0

def rotaryChange(direction):
    step = 5
    if direction == 1:
        print(rotation + step)
    else:
        print(rotation - step)


def switchPressed():
    print
    "button pressed"


if __name__ == "__main__":

    CLOCKPIN = 5
    DATAPIN = 6
    SWITCHPIN = 13

    GPIO.setmode(GPIO.BCM)

    ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange, switchPressed)

    ky040.start()

    try:
        while True:
            time.sleep(0.05)
    finally:
        ky040.stop()
        GPIO.cleanup()