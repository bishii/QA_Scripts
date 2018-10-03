import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#control_pins = [7,11,13,15]
control_pins = [13,19,26]
# GPIO-13 = ON/OFF   IN3 relay 
# GPIO-19 = MOTOR POS IN1 relay
# GPIO-26 = MOTOR NEG IN2 relay



for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)


ans="start"
while ans != 'exit':
	r = input("Relay #1 (Positive at Battery) ON or OFF ?")
	s = input("Relay #2 (Negative at Battery) ON or OFF ?")
	q = input("POWER (Circuit between Relay #2 and Positive Terminal of Battery) ON or OFF ?")

	input("Ready ?")


	if r == "ON":
		GPIO.output(19,GPIO.HIGH)
	elif r =="OFF":
		GPIO.output(19,GPIO.LOW)	

	if s == "ON":
		GPIO.output(26,GPIO.HIGH)
	elif s == "OFF":
		GPIO.output(26,GPIO.LOW)	

	if q == "ON":
		if r == s:
			GPIO.output(13,GPIO.HIGH)
	elif q =="OFF":
		GPIO.output(13,GPIO.LOW)	
		
	print("SET!!!")

	ans = input("Try again ? (exit to close):")


GPIO.cleanup()
