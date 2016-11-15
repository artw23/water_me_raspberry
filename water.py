import RPi.GPIO as GPIO
import time
import sys


seconds = sys.argv[1];

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

print "watering plant"
GPIO.output(18,GPIO.HIGH)
print "waiting... " + str(seconds) + "seconds"
time.sleep(seconds)

print "LED off"
GPIO.output(18,GPIO.LOW)
