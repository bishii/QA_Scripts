from time import sleep
import random
import time

def bubble_once(theList):

	numberOfSwapsFound = 0
	for x in range(len(theList) - 1):

		if theList[x].IntervalTimeTrue > theList[x + 1].IntervalTimeTrue:
		    numberOfSwapsFound += 1

		    # swap the coordinates of the 2 dots on the board...
		    temp = theList[x].get_coords()
		    theList[x].move_to(theList[x + 1].get_coords())
		    theList[x + 1].move_to(temp)

		    # then, swap the positions of the two objects in the list!
		    temp = theList[x]
		    theList[x] = theList[x + 1]
		    theList[x + 1] = temp

	return numberOfSwapsFound


def bubble_all(theList, dotMatrix):
	numSwaps = 0
	for x in range(len(theList)):
            res = bubble_once(theList)
            numSwaps += res
            sleep(0.05)
            dotMatrix.render_dots(theList)
	return (time.time(), 'BUBBLE_SORT', time.time(), numSwaps, len(theList))
