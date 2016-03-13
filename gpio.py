import RPi.GPIO as GPIO
import time

def blink(times, delay):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)

    while times>0:
        if 0==times%2:
            GPIO.output(25, GPIO.HIGH) #or output(11, GPIO.True)
        else:
            GPIO.output(25, GPIO.LOW)
        time.sleep(delay)
        times-=1
    return