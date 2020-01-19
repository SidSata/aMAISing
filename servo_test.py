import RPi.GPIO as GPIO
import time

# testing servo motor when connected to Raspberry Pi

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

# GPIO 17 for PWM with 50Hz
p = GPIO.PWM(servoPIN, 50)

# Initialization
p.start(2.5) 
try:
  while True:
    p.ChangeDutyCycle(2.5)
    time.sleep(2)
    p.ChangeDutyCycle(7)
    time.sleep(2)
    p.ChangeDutyCycle(11.5)
    time.sleep(2)
    p.ChangeDutyCycle(7.1)
    time.sleep(2)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
