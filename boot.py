import RPi.GPIO as GPIO
import time
import os
import gpiozero
import threading
import subprocess

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #front-button gpio detection
GPIO.setup(26, GPIO.OUT)

led = gpiozero.PWMLED(16)

def pulseled():
    led.pulse()

p = threading.Thread(name='pulseled', target=pulseled)

def onbuttonpress():
    led.value = 0
    
    print('Button Pressed')
    
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(26, GPIO.LOW)

    def posttophp():
        #posttophp = os.system('python /home/pi/SmartScale/posttophp.py 34:AF:2C:2D:9E:4B')
        subprocess.Popen(["python", "/home/pi/SmartScale/posttophp.py 34:AF:2C:2D:9E:4B"])

    pp = threading.Thread(name='posttophp', target=posttophp)
    pp.start()

def detectbuttonpress():
    while True:
        input_state = GPIO.input(21)
        if input_state == False:
            onbuttonpress()

d = threading.Thread(name='detectbuttonpress', target=detectbuttonpress)

p.start()
d.start()
