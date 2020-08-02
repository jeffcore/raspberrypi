from gpiozero import Button
from signal import pause

def say_hello():
    print('hello yo!')

button = Button(26)


while True:
  
    
    if button.is_pressed:
        print('button is pressed')
    else:
        print('button is not pressed')
    
    # button.wait_for_press()
    button.when_pressed = say_hello

   
    pause()