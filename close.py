from urllib.request import urlopen
import RPi.GPIO as GPIO
import json
import time
import sys

pinPHP = sys.argv[1]

def angle_calcul (angle):
	if angle > 180 or angle < 0:
		return False
	start = 1.5
	end = 10
	ratio = (end - start)/180
	angle_percent = angle * ratio
	
	return start + angle_percent



def close_lock(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	
	frequence = 40
	GPIO.setup(int(pin), GPIO.OUT)
	pwm = GPIO.PWM(int(pin), frequence)
	
	pwm.start(angle_calcul(0))
	time.sleep(0.5)
	
	pwm.stop()
	GPIO.cleanup()
	
close_lock(pinPHP) 
