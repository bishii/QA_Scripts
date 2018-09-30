import DotMatrix
from dot import Dot
from random import randrange
from RPi import GPIO
import random
import timeit
import SelectionSort
import BubbleSort

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
GPIO_NUM_WHITE_BUTTON = 2

# SETUPS
GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_NUM_WHITE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

dotMatrix = DotMatrix.DotMatrixModule()

dotsVariants = [32,64,96,128]

################
###MAIN LOOP####
################

while True:

        numDots = random.choice(dotsVariants)
        dotsSource, dotsSourceOrig = dotMatrix.create_dot_instances(numDots)

        for duration in range(50):

                dotMatrix.render_dots(dotsSourceOrig)
                y = dotMatrix.check_button_events([GPIO_NUM_WHITE_BUTTON])
                if y == False:
                        raise ButtonPressEvent("Button was pressed, and bubbled up!")

                if duration == 25:
                        SelectionSort.run_selection_sort(dotsSource, dotsSourceOrig, dotMatrix)

		if duration == 49:
        		numDots = random.choice(dotsVariants)
        		dotsSource, dotsSourceOrig = dotMatrix.create_dot_instances(numDots)
                        BubbleSort.bubble_all(dotsSource, dotMatrix)
