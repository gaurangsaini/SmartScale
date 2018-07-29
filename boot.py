import RPi.GPIO as GPIO
import time
import os
import SevenSegment

display = SevenSegment.SevenSegment()
display.begin()
display.clear()
display.set_colon(True)
display.write_display()

time.sleep(15)


i=34952
display.clear()
display.set_colon(False)
display.print_hex(i)
display.write_display()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state == False:
        print('Button Pressed')
        os.system('python /home/pi/SmartScale/posttophp.py 34:AF:2C:2E:B9:7E')
        time.sleep(1)
