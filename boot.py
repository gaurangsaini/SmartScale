import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state == False:
        print('Button Pressed')
	os.system('python wiiboard.py 34:AF:2C:2D:82:7E')
        time.sleep(1)