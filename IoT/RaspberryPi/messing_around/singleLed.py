import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
#Red LED 1
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

# Button 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Buzzer
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)

while True:

	if GPIO.input(10) == GPIO.HIGH:
		GPIO.output(8, GPIO.HIGH)
		GPIO.output(12, GPIO.HIGH)

	else:
		GPIO.output(8, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
