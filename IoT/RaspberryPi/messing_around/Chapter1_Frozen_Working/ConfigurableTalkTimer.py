import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GREEN_LED = 14
GREEN_LED_BLINK_RATES = (10,0.10)

YELLOW_LED = 15
YELLOW_LED_BLINK_RATES = (10,0.10)

RED_LED_1 = 18
RED_LED_1_BLINK_RATES = (1,0.10)

RED_LED_2 = 23
RED_LED_2_BLINK_RATES = (1,0.10)

RED_LED_3 = 24
RED_LED_3_BLINK_RATES = (1,0.10)

BUZZER_1 = 12

GPIO.setup(GREEN_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YELLOW_LED, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(RED_LED_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RED_LED_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RED_LED_3, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(BUZZER_1, GPIO.OUT)

def LED_Blink(ledId, ledBlinkRates, blink=False, blinkNum=1, buzzer=False):

	if blink:
		eachInterval = ledBlinkRates[0] / blinkNum
		for a in range(blinkNum):
			if buzzer:
				GPIO.output(BUZZER_1, True)
				sleep(0.10)
				GPIO.output(BUZZER_1, False)	
			GPIO.output(ledId, GPIO.HIGH)
			sleep(eachInterval)
			GPIO.output(ledId,GPIO.LOW)
			sleep(0.10)
	else:
		GPIO.output(ledId, GPIO.HIGH)
		sleep(ledBlinkRates[0])
		GPIO.output(ledId, GPIO.LOW)
		sleep(ledBlinkRates[1])

while True:

	LED_Blink(GREEN_LED, (2,0.10))
	LED_Blink(GREEN_LED, (2,0.10))

	LED_Blink(YELLOW_LED, (5,0.10))
	LED_Blink(YELLOW_LED, (5,0.10), True, 20)
	
	LED_Blink(RED_LED_1, (3,0.10), True, 3, True)
	LED_Blink(RED_LED_2, (3,0.10), True, 10, True)
	LED_Blink(RED_LED_3, (3,0.10), True, 20, True)
