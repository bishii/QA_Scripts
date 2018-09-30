from time import sleep
import random

def bubble_once(theList):
    try:
            for x in range(len(theList) - 1):

                if theList[x].IntervalTimeTrue > theList[x + 1].IntervalTimeTrue:

                    # swap the coordinates of the 2 dots on the board...
                    temp = theList[x].get_coords()
                    theList[x].move_to(theList[x + 1].get_coords())
                    theList[x + 1].move_to(temp)

                    # then, swap the positions of the two objects in the list!
                    temp = theList[x]
                    theList[x] = theList[x + 1]
                    theList[x + 1] = temp

    except ButtonPressEvent:
        print "Fyi: User pressed button."
        raise

def bubble_all(theList, dotMatrix):
    try:
        for x in range(len(theList)):
            bubble_once(theList)
            sleep(0.05)
            dotMatrix.render_dots(theList)

    except ButtonPressEvent:
        raise
