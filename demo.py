import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
servoPIN = 17
GPIO.setup(servoPIN, GPIO.OUT)

#right wheel
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
#left wheel
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
#IR 1
GPIO.setup(13, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(5, GPIO.IN)
irl=13
irr=6
irf=5
rot=1.43
#timetotal=0

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
        return(1)
    else:
        return(0)
    
#if (GPIO.input(13)== 0):
    #front()
    
#else:
    #back()
#time.sleep(3)

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
    #return (timeleft-tfront)
stop()
time.sleep(30)

front()
time.sleep(8)
right()
time.sleep(1.4)
front()
time.sleep(6)
stop()

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5)
p.ChangeDutyCycle(2.5)
time.sleep(2)
p.ChangeDutyCycle(11.5)
time.sleep(2)

#while (1):
 #if(IR(irf)==0):
  #front()
 #else:
  #obstacle()

GPIO.cleanup()
