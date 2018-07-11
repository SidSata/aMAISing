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

def front (t):
 GPIO.output(20, GPIO.HIGH)
 GPIO.output(21, GPIO.LOW)
 GPIO.output(19, GPIO.HIGH)
 GPIO.output(26, GPIO.LOW)

 time.sleep(t)
 GPIO.output(20, GPIO.LOW)
 GPIO.output(19, GPIO.LOW)
 
def back (t):
 GPIO.output(21, GPIO.HIGH)
 GPIO.output(20, GPIO.LOW)
 GPIO.output(26, GPIO.HIGH)
 GPIO.output(19, GPIO.LOW)

 time.sleep(t)
 GPIO.output(21, GPIO.LOW)
 GPIO.output(26, GPIO.LOW)

def left (t):
 GPIO.output(20, GPIO.HIGH)
 GPIO.output(21, GPIO.LOW)
 GPIO.output(26, GPIO.HIGH)
 GPIO.output(19, GPIO.LOW)

 time.sleep(t)
 GPIO.output(20, GPIO.LOW)
 GPIO.output(26, GPIO.LOW)
 
def right (t):
 GPIO.output(21, GPIO.HIGH)
 GPIO.output(20, GPIO.LOW)
 GPIO.output(19, GPIO.HIGH)
 GPIO.output(26, GPIO.LOW)

 time.sleep(t)
 GPIO.output(21, GPIO.LOW)
 GPIO.output(19, GPIO.LOW)
 
left(3)
right(4)


GPIO.cleanup()