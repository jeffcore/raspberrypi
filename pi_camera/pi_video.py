from picamera import PiCamera
from time import sleep
from gpiozero import Button, LED  

button = Button(16)
red = LED(21)

button.wait_for_press()
red.on() 
print('button pressed recording')
camera = PiCamera()
camera.rotation = 180
camera.resolution = (1024, 980)
camera.framerate = 15
camera.start_recording('/home/pi/Desktop/video.h264')

button.wait_for_press()
red.off()
print('button pressed recording stopped')
camera.stop_recording()
camera.stop_preview()