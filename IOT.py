#to check the i/o ports
from gpiozero import Button
from time import sleep

button = Button(2)

while True:
    if button.is_pressed:
        print("Button Press")
    else:
        print("Button Release")
    sleep(1)
