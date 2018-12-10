import RPi.GPIO as GPIO
import time
import os
import gpiozero
import threading
import subprocess, signal

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #front-button gpio detection
GPIO.setup(26, GPIO.OUT)

led = gpiozero.PWMLED(16)

def pulseled():
    led.pulse()

p = threading.Thread(name='pulseled', target=pulseled)

def killprocesses():
    p = subprocess.Popen(['ps', '-aux'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    for line in out.splitlines():
        if 'posttophp.py' in line:
            pid = int(line.split(None, 2)[1])
            os.kill(pid, signal.SIGKILL)

def onbuttonpress():
    led.value = 0
    
    print('Button Pressed')
    
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(26, GPIO.LOW)

    def posttophp():
        killprocesses()
        posttophp = os.system('python /home/pi/SmartScale/posttophp.py 34:AF:2C:2C:5A:60')

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