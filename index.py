from urllib.request import urlopen
import RPi.GPIO as GPIO
import json
import time
import sys



pinPHP = sys.argv[1]
codePHP = sys.argv[2]

def angle_calcul (angle):
	if angle > 180 or angle < 0:
		return False
	start = 1.5
	end = 10
	ratio = (end - start)/180
	angle_percent = angle * ratio
	
	return start + angle_percent

def open_lock(pin):
	print("pin = " + str(pin))
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
		
	frequence = 40
	GPIO.setup(int(pin), GPIO.OUT)
	pwm = GPIO.PWM(int(pin), frequence)

	pwm.start(angle_calcul(80))
	time.sleep(0.5)
	
	pwm.stop()
	GPIO.cleanup()
	



open_lock(pinPHP) 

