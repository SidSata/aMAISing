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
irl=2
irr=2
irf=2

def front ():
 GPIO.output(20, GPIO.HIGH)
 GPIO.output(21, GPIO.LOW)
 GPIO.output(19, GPIO.HIGH)
 GPIO.output(26, GPIO.LOW)

def stop():
 GPIO.output(21, GPIO.LOW)
 GPIO.output(20, GPIO.LOW)
 GPIO.output(26, GPIO.LOW)
 GPIO.output(19, GPIO.LOW)
    
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
    if (GPIO.input(pin)== 1):
        return(true)
    else:
        return(false)
    
if (GPIO.input(13)== 0):
    front()
    
else:
    back()
time.sleep(3)

def obstacle():
    left()
    time.sleep(rot)
    stop()
    t1= time.time()
    while(IR(irr)==1):
        front()
    stop()    
    t2= time.time()
    tside= t2-t1
    right()
    time.sleep(rot)
    stop()    
    t1= time.time()
    while(IR(irr)==1):
        front()
    stop()    
    t2= time.time()
    tfront= t2-t1
    right()
    time.sleep(rot)
    stop()    
    front()
    time.sleep(tside)
    stop()
    left()
    time.sleep(rot)
    stop()
    return (timeleft-tfront)

GPIO.cleanup()
