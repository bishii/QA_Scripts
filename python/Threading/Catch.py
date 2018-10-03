import time
import threading
from Player import Player

listOfPlayers = []
listOfThreads = []

for x in range(10):
	listOfPlayers.append(Player(str(x), 5))

for y in range(10):
	listOfThreads.append(threading.Thread(target=listOfPlayers[y].start_polling, args=()))

for z in listOfThreads:
	print("Starting: %s" % z.name)
	z.start() 