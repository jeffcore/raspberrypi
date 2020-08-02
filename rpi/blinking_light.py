import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

for _ in range(50):
    GPIO.output(18, True)
    sec = random.random()
    time.sleep(sec)
    GPIO.output(18, False)
    time.sleep(sec)
    
GPIO.cleanup()