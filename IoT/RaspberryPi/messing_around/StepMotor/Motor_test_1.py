import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#control_pins = [7,11,13,15]
control_pins = [1,7,17,27]



for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

direction=[8]

while True:
	for i in range(1500):
		for halfstep in range(*direction):
			for pin in range(4):
				GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
			time.sleep(0.001)

	direction = [7,-1,-1] if direction == [8] else [8]

GPIO.cleanup()
