from RPi import GPIO
from time import sleep
import json
import requests
import random
from itertools import cycle
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26,GPIO.OUT)

#Servo initialize to 50Hz(?)
p=GPIO.PWM(26,50)
p.start(2.5)

GPIO.cleanup()
