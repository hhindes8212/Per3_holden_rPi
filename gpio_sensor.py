from gpiozero import Button
from time import sleep
sensor = Button(2)
while 1 == 1:
    sensor.wait_for_press()
    #jump
    print('jumped')
    sleep(1)
