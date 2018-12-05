import RPi.GPIO as GPIO
import time
import os

GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.HIGH)

#time.sleep(15)

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO CHANGED FROM 4 TO 17, to 27, to 21(!)
while True:
    input_state = GPIO.input(21)
    if input_state == False:
        print('Button Pressed')
        
        GPIO.setup(26, GPIO.OUT)
        GPIO.output(26, GPIO.HIGH)

        time.sleep(0.25)

        GPIO.output(26, GPIO.LOW)
        
        os.system('python /home/pi/SmartScale/posttophp.py 34:AF:2C:2D:9E:4B')
        time.sleep(1)