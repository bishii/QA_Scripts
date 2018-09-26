import boto3
import json

sqs = boto3.resource('sqs')
queue = sqs.Queue("http://sqs.us-west-2.amazonaws.com/410936176879/Automation_Events")

res = [1]
finalList = []
while len(res) > 0:
	res = queue.receive_messages(QueueUrl="http://sqs.us-west-2.amazonaws.com/410936176879/Automation_Events",MaxNumberOfMessages=10,VisibilityTimeout=123,ReceiveRequestAttemptId='string')
	finalList += [msg.body for msg in res]

x = json.loads(finalList[0])
print(x)
