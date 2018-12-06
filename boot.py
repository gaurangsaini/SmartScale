import RPi.GPIO as GPIO
import time
import os
import gpiozero
import threading

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #front-button gpio detection
GPIO.setup(26, GPIO.OUT)

o = threading.Thread(name='onbuttonpress', target=onbuttonpress)
d = threading.Thread(name='detectbuttonpress', target=detectbuttonpress)

def onbuttonpress():
    led.value = 0
    
    print('Button Pressed')
    
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(26, GPIO.LOW)

    #status = subprocess.call("python /home/pi/SmartScale/posttophp.py 34:AF:2C:2D:9E:4B", shell=True)
    try:
        retcode = subprocess.call("python /home/pi/SmartScale/posttophp.py 34:AF:2C:2D:9E:4B", shell=True)
        if retcode < 0:
            print >>sys.stderr, "Child was terminated by signal", -retcode
        else:
            print >>sys.stderr, "Child returned", retcode
    except OSError as e:
        print >>sys.stderr, "Execution failed:", e

def detectbuttonpress():
    led = gpiozero.PWMLED(16)
    led.pulse()

    input_state = GPIO.input(21)
    if input_state == False:
        o.start()

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
