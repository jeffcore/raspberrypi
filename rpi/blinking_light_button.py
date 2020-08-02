import RPi.GPIO as GPIO
import time
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

for _ in range(50):
    if GPIO.input(25):
        print('button on')
        GPIO.output(18, True)       
        time.sleep(2)
        GPIO.output(18, False)
        time.sleep(2)
    else:
        print('button off')
        GPIO.output(18, True)       
        time.sleep(.2)
        GPIO.output(18, False)
        time.sleep(.2)
GPIO.cleanup()