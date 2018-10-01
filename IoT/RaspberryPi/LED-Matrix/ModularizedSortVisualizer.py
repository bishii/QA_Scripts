import DotMatrix
import boto3
from dot import Dot
from random import randrange
#from RPi import GPIO
import random
import timeit
import SelectionSort
import BubbleSort
import GPIO_Module

# Selection Sort:
FALSE_MIN = 30
FALSE_MAX = 31

TRUE_MIN = 40
TRUE_MAX = 50

# GPIO Wire Assignments:
# LED MAXTRIX:
#       DIN --> 9 (MISO)
#       CS  --> 8
#       CLK --> 11 (SCLK)
#GPIO_NUM_WHITE_BUTTON = 2

# SETUPS
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(GPIO_NUM_WHITE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

dotMatrix = DotMatrix.DotMatrixModule()
dotsVariants = [32,64,96,128]

db = boto3.resource('dynamodb')
dbTable = db.Table('APPLICATION_DATA')


################
###MAIN LOOP####
################

while True:

	numDots = random.choice(dotsVariants)
	dotsSource, dotsSourceOrig = dotMatrix.create_dot_instances(numDots)

	for duration in range(11):

		dotMatrix.render_dots(dotsSourceOrig)
                #y = dotMatrix.check_button_events([GPIO_NUM_WHITE_BUTTON])
                #if y == False:
                #        raise ButtonPressEvent("Button was pressed, and bubbled up!")

		if duration == 5:
			LOG_DATE_TIME, MODULE_NAME, COMPLETION_TIME, NUMBER_OF_SWAPS, TOTAL_DOTS = \
				SelectionSort.run_selection_sort(dotsSource, dotsSourceOrig, dotMatrix)
			theResponse = {'NUMBER_OF_ELEMENTS': int(TOTAL_DOTS), 'LOG_DATE_TIME': int(LOG_DATE_TIME), \
				'NUMBER_OF_SWAPS': int(NUMBER_OF_SWAPS), 'MODULE_NAME': 'SELECTION_SORT', 'COMPLETION_TIME': int(COMPLETION_TIME)}
			
			dbTable.put_item(Item=theResponse)

		if duration == 10:
			numDots = random.choice(dotsVariants)
			dotsSource, dotsSourceOrig = dotMatrix.create_dot_instances(numDots)

			LOG_DATE_TIME, MODULE_NAME, COMPLETION_TIME, NUMBER_OF_SWAPS, TOTAL_DOTS = \
				BubbleSort.bubble_all(dotsSource, dotMatrix)

			theResponse = {'NUMBER_OF_ELEMENTS': int(TOTAL_DOTS), 'LOG_DATE_TIME': int(LOG_DATE_TIME), \
				'NUMBER_OF_SWAPS': int(NUMBER_OF_SWAPS), 'MODULE_NAME': 'BUBBLE_SORT', 'COMPLETION_TIME': int(COMPLETION_TIME)}

			dbTable.put_item(Item = theResponse)
