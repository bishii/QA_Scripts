import time


def run_selection_sort(dotsSource, dotsSourceOrig, dotMatrix):

    newX = 0
    newY = 4
    sortIntervalCounter = 0

    totalDots = len(dotsSource)

    while len(dotsSource) > 0:

            sortIntervalCounter +=1
            if sortIntervalCounter > 2:
                sortIntervalCounter = 0

                currentSmallestTrueValue = dotsSource[0].get_interval_time_true()

                for d in dotsSource:
                    curr = d.get_interval_time_true()
                    if curr < currentSmallestTrueValue:
                        currentSmallestTrueValue = curr

                for d in dotsSource:
                        if d.get_interval_time_true() == currentSmallestTrueValue:

                            d.move_to((newX, newY))

                            if newX == 31:
                                 newX = 0
                                 newY += 1
                            else:
                                 newX += 1

                            dotsSource.remove(d)
                            currentSmallestTrueValue=1000
                            dotMatrix.render_dots(dotsSourceOrig)
    return ( time.time(), 'SELECTION_SORT', time.time(), totalDots, totalDots)
