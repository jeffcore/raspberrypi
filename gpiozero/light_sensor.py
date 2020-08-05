from gpiozero import LightSensor

sensor = LightSensor(25,threshold=.001)
print('start working')

while True:
    sensor.wait_for_light()
    print('got here')
    print("It's light! :)")
    sensor.wait_for_dark()
    print("It's dark :(")

# from gpiozero import LineSensor
# from signal import pause

# sensor = LineSensor(25)
# sensor.when_line = lambda: print('Line detected')
# sensor.when_no_line = lambda: print('No line detected')
# pause()