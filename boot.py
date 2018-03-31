import RPi.GPIO as GPIO
import time
import os
import SevenSegment

time.sleep(120)

display = SevenSegment.SevenSegment()
display.begin()

i=34952
display.clear()
display.print_hex(i)
display.write_display()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state == False:
        print('Button Pressed')
        os.system('python /home/pi/SmartScale/wiiboard.py 34:AF:2C:2D:82:7E')
        time.sleep(1)