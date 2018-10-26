import RPi.GPIO as GPIO
import time
import os
#import seven_segment_display
#import seven_segment_i2c

#bus = seven_segment_i2c.SevenSegmentI2c(1)
#display = seven_segment_display.SevenSegmentDisplay(bus)

#display.clear_display()
#display.set_brightness_level(100)
#display.clear_display()

#colon = [0b00010000]
#display.set_nondigits(colon)

#time.sleep(15)

#display.clear_display()
#display.write_int(8888)

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO CHANGED FROM 4 TO 17, to 27 (!)
while True:
    input_state = GPIO.input(27)
    if input_state == False:
        print('Button Pressed')
        os.system('python /home/pi/SmartScale/posttophp.py 34:AF:2C:2E:76:00')
        time.sleep(1)
