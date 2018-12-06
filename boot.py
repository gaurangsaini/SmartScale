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

    posttophp = os.system('python /home/pi/SmartScale/posttophp.py 34:AF:2C:2D:9E:4B')

    #status = subprocess.call("python /home/pi/SmartScale/posttophp.py 34:AF:2C:2D:9E:4B", shell=True)
    #try:
    #    retcode = subprocess.call("python /home/pi/SmartScale/posttophp.py 34:AF:2C:2D:9E:4B", shell=True)
    #    if retcode < 0:
    #        print >>sys.stderr, "Child was terminated by signal", -retcode
    #    else:
    #        print >>sys.stderr, "Child returned", retcode
    #except OSError as e:
    #    print >>sys.stderr, "Execution failed:", e

#o = threading.Thread(name='onbuttonpress', target=onbuttonpress)

def detectbuttonpress():
    while True:
        input_state = GPIO.input(21)
        if input_state == False:
            onbuttonpress()

d = threading.Thread(name='detectbuttonpress', target=detectbuttonpress)

p.start()
d.start()

#GPIO.add_event_detect(21, GPIO.FALLING, callback=onbuttonpress, bouncetime=300)

#time.sleep(15)

#while True:
    

#        print('Button Pressed')
        
        
#        GPIO.output(26, GPIO.HIGH)

#        time.sleep(0.25)

#        GPIO.output(26, GPIO.LOW)
        
#        GPIO.cleanup()

#        os.system('python /home/pi/SmartScale/posttophp.py 34:AF:2C:2D:9E:4B')
#        time.sleep(1)
