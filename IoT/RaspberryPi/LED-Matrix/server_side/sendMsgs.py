import boto3
from random import randrange
import time
import json


def CreateTicker():

    y = ""
    for a in range(4):
        y += chr(randrange(65, 90))

    return y


queue = boto3.resource('sqs').Queue(
    'https://sqs.us-west-2.amazonaws.com/410936176879/Automation_Events')

for x in range(1):
    baseJson = {"stocks": {}}

    eDate = time.time()
    rTicker = CreateTicker()

    for x in range(256):
        baseJson['stocks'][CreateTicker()] = \
            {
                "epoch_date": str(eDate),
                "high_value": str(randrange(1, 100)),
                "low_value": str(randrange(101, 200))}
    theBody = baseJson
    x = json.dumps(theBody)
    type(x)
    print(x)
    queue.send_message(MessageBody=x)
    print("Just sent: %s" % x)

