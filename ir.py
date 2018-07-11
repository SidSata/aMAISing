import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#right wheel
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
#left wheel
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
#IR 1
GPIO.setup(13, GPIO.IN)


def front ():
 GPIO.output(20, GPIO.HIGH)
 GPIO.output(21, GPIO.LOW)
 GPIO.output(19, GPIO.HIGH)
 GPIO.output(26, GPIO.LOW)

def stop(pin):
 GPIO.output(pin, GPIO.LOW)
 
def back ():
 GPIO.output(21, GPIO.HIGH)
 GPIO.output(20, GPIO.LOW)
 GPIO.output(26, GPIO.HIGH)
 GPIO.output(19, GPIO.LOW)


def left ():
 GPIO.output(20, GPIO.HIGH)
 GPIO.output(21, GPIO.LOW)
 GPIO.output(26, GPIO.HIGH)
 GPIO.output(19, GPIO.LOW)

 
def right ():
 GPIO.output(21, GPIO.HIGH)
 GPIO.output(20, GPIO.LOW)
 GPIO.output(19, GPIO.HIGH)
 GPIO.output(26, GPIO.LOW)
 
def IR(pin):
    if (GPIO.input(pin)== HIGH):
        return(true)
    else:
        return(false)
    
if (GPIO.input(13)== 0):
    front()
    
else:
    back()
time.sleep(3)

GPIO.cleanup()
